# Phase 1 Browser Smoke

Date: 2026-05-08

Environment:
- app served with `vite preview -- --host 127.0.0.1 --port 4173`
- browser surface: Codex In-app Browser

Active surface under test:
- `src/main.tsx`
- `src/App.tsx`
- `src/jewik-core/index.ts`
- `src/proof/proofCheck.ts`

Smoke loop:
1. Open app.
2. Confirm Phase 1 screen loads.
3. Click `New Entry`.
4. Fill dictionary meaning.
5. Fill JEWIK cut.
6. Attempt `PROVEN` without evidence.
7. Confirm block.
8. Add evidence.
9. Set `PROVEN`.
10. Remove last evidence.
11. Confirm downgrade to `UNDER_REVIEW`.
12. Click `Download Markdown`.
13. Click `Download JSON`.
14. Verify export previews show proof state and evidence trace.

Observed UI signals:
- Phase 1 screen loaded with `Entries List`, `Dictionary Layer`, `JEWIK Cut`, `Proof / Evidence`, `Export`.
- `New Entry` selected a blank entry and allowed direct editing.
- `Blocked: PROVEN requires evidence.` was shown when `PROVEN` was attempted without evidence.
- After adding evidence, `Proof status is now PROVEN.` was shown.
- After removing the last evidence item, `Evidence removed. Proof status downgraded to UNDER_REVIEW.` was shown.
- Markdown preview showed `- proofStatus: UNDER_REVIEW` and `- evidenceCount: 0`.
- JSON preview showed `"proofStatus": "UNDER_REVIEW"` and preserved `exportText` with `EVIDENCE COUNT: 0`.
- Clicking `Download Markdown` and `Download JSON` updated the app message and version history with export events.

Known browser limitation:
- Codex In-app Browser does not expose download events for direct file-transfer verification.
- Export logic was therefore verified by UI state change, version history, and preview content, not by captured download payloads.

Result:
- Phase 1 browser smoke passed at the application level.
- Download transport remains only partially observable in this browser runtime.
