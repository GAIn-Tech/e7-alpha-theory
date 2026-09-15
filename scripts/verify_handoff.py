"""Byte-integrity verification and optional restoration; not scientific proof."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def safe_path(root, relative):
    parts = PurePosixPath(relative)
    if parts.is_absolute() or '..' in parts.parts or ':' in relative or '\\' in relative:
        raise ValueError('Unsafe relative path: ' + relative)
    return root.joinpath(*parts.parts)


def materialize_archive(root, tool):
    archive = safe_path(root, tool['archive'])
    if not archive.exists() and tool.get('chunks'):
        import os
        import tempfile
        archive.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(dir=archive.parent, prefix='assembly-', delete=False) as out:
                temporary = Path(out.name)
                for chunk in tool['chunks']:
                    source = safe_path(root, chunk['path'])
                    if source.stat().st_size != chunk['size'] or digest(source) != chunk['sha256']:
                        raise ValueError('Chunk mismatch: ' + chunk['path'])
                    with source.open('rb') as stream:
                        while data := stream.read(1024 * 1024):
                            out.write(data)
            if temporary.stat().st_size != tool['archive_bytes'] or digest(temporary) != tool['archive_sha256']:
                raise ValueError('Reassembled archive mismatch')
            if archive.exists():
                raise ValueError('Archive appeared during assembly; refusing overwrite')
            os.replace(temporary, archive)
            temporary = None
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
    return archive


def verify(root, manifest_path, restore=False, check_toolchain=False):
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    if manifest['schema'] != 'e7-research-handoff-v1' or not manifest['files']:
        raise ValueError('Invalid or empty research manifest')
    seen = set()
    for row in manifest['files']:
        name = row['path']
        if name in seen:
            raise ValueError('Duplicate path: ' + name)
        seen.add(name)
        path = safe_path(root, name)
        if not path.is_file() or path.stat().st_size != row['size'] or digest(path) != row['sha256']:
            raise ValueError('Missing, unhydrated or changed file: ' + name)
    tool = json.loads((root / 'handoff-artifacts/toolchain-manifest.json').read_text(encoding='utf-8'))
    archive = materialize_archive(root, tool)
    if archive.stat().st_size != tool['archive_bytes'] or digest(archive) != tool['archive_sha256']:
        raise ValueError('Toolchain archive hash mismatch')
    expected = {r['path']: r for r in tool['files']}
    if len(expected) != tool['file_count']:
        raise ValueError('Toolchain inventory count mismatch')
    with zipfile.ZipFile(archive) as z:
        if len(z.infolist()) != len(expected) or set(z.namelist()) != set(expected):
            raise ValueError('Toolchain archive membership mismatch')
        # Validate all source bytes before making any restoration writes.
        for name, row in expected.items():
            safe_path(root, name)
            if z.getinfo(name).file_size != row['size']:
                raise ValueError('Archive size mismatch: ' + name)
            with z.open(name) as stream:
                if hashlib.file_digest(stream, 'sha256').hexdigest() != row['sha256']:
                    raise ValueError('Archive member hash mismatch: ' + name)
        if restore:
            for name, row in expected.items():
                path = safe_path(root, name)
                if path.exists() and digest(path) != row['sha256']:
                    raise ValueError('Refusing to overwrite different local toolchain file: ' + name)
            for name, row in expected.items():
                path = safe_path(root, name)
                if not path.exists():
                    path.parent.mkdir(parents=True, exist_ok=True)
                    with z.open(name) as src, path.open('wb') as dst:
                        while chunk := src.read(1024 * 1024):
                            dst.write(chunk)
            check_toolchain = True
    if check_toolchain:
        for name, row in expected.items():
            path = safe_path(root, name)
            if not path.is_file() or path.stat().st_size != row['size'] or digest(path) != row['sha256']:
                raise ValueError('Restored toolchain mismatch: ' + name)
    return {'passed': True, 'scope': 'file integrity only; not proof validation',
            'research_files': len(seen), 'toolchain_files': len(expected),
            'toolchain_restored_and_verified': bool(check_toolchain)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--manifest', type=Path)
    parser.add_argument('--restore-toolchain', action='store_true')
    parser.add_argument('--check-toolchain', action='store_true')
    args = parser.parse_args()
    manifest = args.manifest or args.root / 'handoff-artifacts/research-manifest.json'
    try:
        result = verify(args.root.resolve(), manifest, args.restore_toolchain, args.check_toolchain)
    except Exception as error:
        print(json.dumps({'passed': False, 'error': str(error)}))
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
