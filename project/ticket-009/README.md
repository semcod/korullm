# Ticket 009: adopt-wellman-standard-packs

- **ID**: ticket-009
- **Owner**: agent:antigravity
- **Status**: IN_PROGRESS
- **Workflow state**: EDIT
- **Created**: 2026-10-17

## Goal and scope

Install `.governance/standard-packs.json`, `.governance/standard_pack_check.py`, and `.governance/standard-adoption.json` to adopt `wellmanifest/wellman` baseline standard packs in `korullm`.

## Acceptance criteria

- [x] AC-01: `python3 .governance/standard_pack_check.py --root .` passes with `findings=0`.
- [x] AC-02: `./project/governance-check.sh` passes with 0 errors.

## Participants

- Human participant: unresolved; no user-* file was created by this script.
- Agent participant: [ai-antigravity.md](ai-antigravity.md)
