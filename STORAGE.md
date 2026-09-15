# Research handoff and storage

## Receiver quick start

Install Python 3.11 or newer and Git. Git LFS is not required: the account LFS budget was exhausted, so the handoff uses ordinary Git partitions. From a new directory:

```sh
git clone --branch rigorous-openai-style-release --single-branch https://github.com/GAIn-Tech/e7-alpha-theory.git
cd e7-alpha-theory
python scripts/verify_handoff.py
```

For the preserved Windows Lean installation:

```sh
python scripts/verify_handoff.py --restore-toolchain
```

The verifier assembles the checksummed chunks into an ignored `.handoff-local/` cache and checks every archive member. The restoration option then restores the selected installation to `gap-investigation/adjoint-radial-rxi-lean-gate/toolchain/`. Existing files with different hashes are never silently overwritten. It is the exact previously installed subset, **not a complete Lean/Mathlib environment or evidence that a theorem compiles**. Use the upstream installer and the relevant gate's declarations to establish any missing environment separately.

The eight chunk files are ordinary Git blobs, each at most 32 MiB. No LFS budget, release download, external cache, credentials beyond repository access, or manual concatenation is required.

## Why the original push failed

The unpublished Git object inventory contained 2,069,317,332 bytes of blobs. Most came from installation, not authored research:

- `distribution-catalog.zip`: 832,108,412 logical bytes. The range installer constructs a sparse ZIP catalog with only selected downloaded bodies, not a complete distribution. GitHub rejected its normal Git blob over the per-file limit.
- Extracted `toolchain/`: 783,236,591 bytes, duplicating downloaded content.
- `download-parts/`: 243,269,632 bytes of redundant HTTP-range cache.
- `lean-4.32.1-windows.zip`: 10,518,528 bytes of an incomplete download; ZIP inspection fails.
- Actual research also includes sizeable saved tensors and chain certificates; those are preserved as their exact original files, not discarded.

The 50 MiB warning is advisory; GitHub's 100 MiB normal-file cap is the hard failure seen here. This is not a 100 MB total-repository limit. Increasing `http.postBuffer`, adding an ignore rule, bypassing hooks or retrying an unchanged push cannot remove oversized objects already in commit ancestry.

## Storage policy

An actual LFS upload was attempted after pointer/hash verification. GitHub returned: "This repository exceeded its LFS budget." Nothing was published through LFS. The fallback replaces the unpublished LFS-pointer snapshot with an ordinary Git snapshot sharing the original published parent; it does not hide missing payloads behind pointers.

The exact 3,016 tracked toolchain files were packed once as a 236,410,949-byte ZIP and partitioned into eight files under `handoff-artifacts/toolchain-parts/`, and each archive member was CRC/SHA-256 verified. The original installation files and disposable caches remain locally in the source checkout and backup history; they are omitted from the new published tree. Their paths and hashes are recorded in `toolchain-manifest.json` and `omitted-installer-cache.json`.

Research source, reports, frozen predecessors, certificates, large numerical data and the previously ignored source PDFs/PNG are retained. Some historical downloaded `.pdf` files are error pages, not valid PDFs: the manifest marks them as failed retrieval evidence, and they must not be cited as the source paper. Presence in the handoff does not certify a source's scientific validity.

`.gitattributes` prevents newline conversion from changing frozen bytes. All payloads are ordinary Git objects below the hard per-file cap. No executable research source or certificate is removed merely because it is large.

Only unpublished history was consolidated, using the existing remote commit as parent. The old local commits and dirty files were backed up before editing. No shared remote history or other branch is force-rewritten.

## Verification layers

- `research-manifest.json`: retained file paths, exact byte sizes and SHA-256s. It excludes itself to avoid circular hashing; the enclosing Git commit pins it.
- `toolchain-manifest.json`: archive digest and every restored file digest.
- `omitted-installer-cache.json`: exact omitted cache inventory and reasons.
- `scripts/verify_handoff.py`: verifies the manifests and archive contents; optional fail-safe restoration.
- `tests/test_handoff_integrity.py`: missing, changed, duplicate and unsafe-path rejection tests.
- `HANDOFF.md`: corrected unresolved scientific frontier.

File transfer, byte verification, tests of storage machinery and numerical arithmetic tests are separate from mathematical proof checking, physical derivation, hosted CI and peer review. The E8 bracket remains uncomputed; the invented E7 "NS" proof is retracted.

## Useful checks

```sh
git status --short --branch
git rev-parse HEAD
git ls-remote origin refs/heads/rigorous-openai-style-release
python -m unittest discover -s tests -p test_handoff_integrity.py -v
```

Before any publication claim, verify that the local commit matches the exact remote branch and that a fresh checkout reassembles its toolchain archive and passes the integrity checker. This document by itself is not evidence of a completed upload.
