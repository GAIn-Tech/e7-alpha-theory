"""Storage test fixtures only; no mathematical or physical evidence."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('handoff_check', ROOT / 'scripts/verify_handoff.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def record(root, name):
    path = root / name
    return {'path': name, 'size': path.stat().st_size,
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


class IntegrityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.artifacts = self.root / 'handoff-artifacts'
        self.artifacts.mkdir()
        (self.root / 'research.txt').write_bytes(b'explicit integrity-test fixture\n')
        self.member = 'toolchain/test-data.bin'
        data = b'toolchain test fixture, not a real executable'
        arc = self.artifacts / 'fixture.zip'
        with zipfile.ZipFile(arc, 'w') as z:
            z.writestr(self.member, data)
        tool = {'archive': 'handoff-artifacts/fixture.zip', 'archive_bytes': arc.stat().st_size,
                'archive_sha256': hashlib.sha256(arc.read_bytes()).hexdigest(), 'file_count': 1,
                'files': [{'path': self.member, 'size': len(data), 'sha256': hashlib.sha256(data).hexdigest()}]}
        (self.artifacts / 'toolchain-manifest.json').write_text(json.dumps(tool))
        self.manifest = self.artifacts / 'research-manifest.json'
        self.payload = {'schema': 'e7-research-handoff-v1',
                        'files': [record(self.root, 'research.txt'), record(self.root, 'handoff-artifacts/fixture.zip'),
                                  record(self.root, 'handoff-artifacts/toolchain-manifest.json')]}
        self.save()

    def tearDown(self):
        self.tmp.cleanup()

    def save(self):
        self.manifest.write_text(json.dumps(self.payload))

    def test_roundtrip_and_restore(self):
        result = module.verify(self.root, self.manifest, restore=True)
        self.assertTrue(result['passed'])
        self.assertTrue(result['toolchain_restored_and_verified'])
        self.assertTrue((self.root / self.member).is_file())

    def test_partitioned_archive_reassembly(self):
        toolpath = self.artifacts / 'toolchain-manifest.json'
        tool = json.loads(toolpath.read_text())
        archive = self.artifacts / 'fixture.zip'
        data = archive.read_bytes()
        part = self.artifacts / 'part001'
        part.write_bytes(data)
        tool['archive'] = '.handoff-local/reassembled.zip'
        tool['chunks'] = [record(self.root, 'handoff-artifacts/part001')]
        toolpath.write_text(json.dumps(tool))
        self.payload['files'] = [record(self.root, 'research.txt'),
                                 record(self.root, 'handoff-artifacts/part001'),
                                 record(self.root, 'handoff-artifacts/toolchain-manifest.json')]
        self.save()
        result = module.verify(self.root, self.manifest, restore=True)
        self.assertTrue(result['passed'])
        self.assertEqual((self.root / tool['archive']).read_bytes(), data)

    def test_bad_partitions_leave_no_cached_archive(self):
        data = (self.artifacts / 'fixture.zip').read_bytes()
        for mode in ['missing', 'changed', 'reordered']:
            with self.subTest(mode=mode):
                tool = json.loads((self.artifacts / 'toolchain-manifest.json').read_text())
                tool['archive'] = '.handoff-local/' + mode + '.zip'
                parts = [self.artifacts / (mode + '.part1'), self.artifacts / (mode + '.part2')]
                middle = len(data) // 2
                parts[0].write_bytes(data[:middle])
                parts[1].write_bytes(data[middle:])
                tool['chunks'] = [record(self.root, part.relative_to(self.root).as_posix()) for part in parts]
                if mode == 'missing':
                    parts[0].unlink()
                elif mode == 'changed':
                    parts[0].write_bytes(b'changed')
                else:
                    tool['chunks'].reverse()
                with self.assertRaises((ValueError, FileNotFoundError)):
                    module.materialize_archive(self.root, tool)
                self.assertFalse((self.root / tool['archive']).exists())
                self.assertEqual(list((self.root / '.handoff-local').glob('assembly-*')), [])

    def test_missing_manifest_fails(self):
        self.manifest.unlink()
        with self.assertRaises(FileNotFoundError):
            module.verify(self.root, self.manifest)

    def test_tamper_fails(self):
        (self.root / 'research.txt').write_bytes(b'changed')
        with self.assertRaises(ValueError):
            module.verify(self.root, self.manifest)

    def test_duplicate_fails(self):
        self.payload['files'].append(self.payload['files'][0])
        self.save()
        with self.assertRaises(ValueError):
            module.verify(self.root, self.manifest)

    def test_unsafe_path_fails(self):
        self.payload['files'][0]['path'] = '../research.txt'
        self.save()
        with self.assertRaises(ValueError):
            module.verify(self.root, self.manifest)

    def test_restore_refuses_overwrite(self):
        target = self.root / self.member
        target.parent.mkdir(parents=True)
        target.write_bytes(b'preserve unrelated local value')
        with self.assertRaises(ValueError):
            module.verify(self.root, self.manifest, restore=True)
        self.assertEqual(target.read_bytes(), b'preserve unrelated local value')


if __name__ == '__main__':
    unittest.main()
