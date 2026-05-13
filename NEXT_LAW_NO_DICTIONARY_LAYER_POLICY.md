# NO_DICTIONARY_LAYER → NO_PROVEN Policy Document

**Date:** 2026-05-08  
**Status:** Policy Definition (No Code Implementation)  
**Authority Baseline:** Archive V3 (2026-05-08)  
**Archive SHA256:** `371cea139581fb3c6c8bf6106a8d6ba508544dd5a6aa40ca2830b6ba20767106`

---

## 1. Policy Statement

### The Law

**NO_DICTIONARY_LAYER → NO_PROVEN**

A `LexiconEntry` must not be allowed to transition to or remain in `PROVEN` status if:
- Its `dictionaryLayer.kind === "UNAVAILABLE"`, OR  
- Its `dictionaryLayer.meaning` is empty or whitespace-only

### Intended Effect

The dictionary layer is a fundamental property that grounds an entry's meaning in the JEWIK system. An entry cannot be considered "proven" without this stabilization. `UNAVAILABLE` signals missing dictionary data; an empty meaning provides no grounding. Both states must block proof transitions.

### Core Principle

PROVEN status is not just about evidence existence. It requires three independent conditions:

1. **Evidence must exist:** `evidence.length > 0`
2. **Dictionary layer must be available:** `dictionaryLayer.kind !== "UNAVAILABLE"`
3. **Dictionary meaning must exist:** `dictionaryLayer.meaning.trim().length > 0`

All three must be true simultaneously. The absence of any one blocks PROVEN.

---

## 2. Policy Boundaries

### In Scope (Will Change)

The following MUST be modified to enforce this law:

1. **`validateEntry()` function**
   - Currently returns validation issues including `MISSING_DICTIONARY_MEANING`
   - Must ADD a new validation issue code: `"PROVEN_REQUIRES_DICTIONARY_LAYER"`
   - This code is raised when `proofStatus === "PROVEN"` and dictionary layer is unavailable OR meaning is empty
   - The code must NOT appear in `canMarkProven` check yet (see "Not Yet" section)

2. **`setProofStatus()` function**
   - Currently blocks PROVEN transitions only if evidence is missing
   - Must EXTEND blocking to also check dictionary layer availability and meaning
   - Return `blocked: true` if attempting PROVEN transition without:
     - Evidence, OR
     - Dictionary layer availability, OR
     - Dictionary meaning

3. **`stabilizeEntry()` function**
   - Currently downgrades PROVEN to UNDER_REVIEW if evidence becomes empty
   - Must EXTEND downgrade logic to also trigger on:
     - Dictionary layer becoming unavailable, OR
     - Dictionary meaning becoming empty
   - Must record appropriate version history message explaining the downgrade reason

4. **`createBlankEntry()` initializer**
   - Blank entries should have `dictionaryLayer.kind === "UNAVAILABLE"` by default
   - This should naturally block PROVEN transitions (no code change needed, but verify behavior)

### Out of Scope (Will NOT Change in This Phase)

The following remain unchanged:

- **`src/proof/proofCheck.ts`** — No new tests added until policy is finalized
- **`src/App.tsx`** — UI logic unchanged
- **`.github/workflows/proof-check.yml`** — CI automation unchanged
- **Export functions** — `buildJsonExport()`, `buildMarkdownExport()`, `buildCardTextExport()` behavior unchanged in this phase
- **Other validation codes** — `MISSING_TERM`, `MISSING_CUT`, `MISSING_OPERATOR_MAPPING` remain as-is
- **Evidence removal behavior** — Downgrading PROVEN when evidence is removed stays as currently implemented

---

## 3. Current Baseline State (Archive V3)

### What Archive V3 Already Has

From the locked Archive V3 baseline (2026-05-08):

**In `validateEntry()` (lines 436-487 of src/jewik-core/index.ts):**
```
Validation issues already detected:
- MISSING_TERM
- MISSING_DICTIONARY_MEANING (✅ already exists)
- MISSING_CUT
- MISSING_OPERATOR_MAPPING
- PROVEN_REQUIRES_EVIDENCE

canMarkProven check:
- Ensures entry has a term
- Ensures entry has dictionary meaning
- Ensures entry has a cut expression
- Does NOT yet check dictionary layer availability
```

**In `setProofStatus()` (lines 489-514):**
```
Blocking logic:
- Blocks PROVEN if evidence.length === 0
- Records "Blocked PROVEN attempt without evidence." in version history
- Does NOT check dictionary layer
```

**In `stabilizeEntry()` (lines 233-279):**
```
Downgrade logic:
- Downgrades PROVEN → UNDER_REVIEW if evidence.length === 0
- Records "Proof status downgraded to UNDER_REVIEW because evidence was removed."
- Does NOT check dictionary layer availability
```

### What This Means

1. **Partial enforcement exists:** `MISSING_DICTIONARY_MEANING` is already a validation issue
2. **But enforcement is incomplete:** `canMarkProven` does not block PROVEN based on dictionary layer availability
3. **And setProofStatus doesn't block:** Entry can transition to PROVEN even with `dictionaryLayer.kind === "UNAVAILABLE"`
4. **And stabilizeEntry doesn't downgrade:** Entry stays PROVEN even if dictionary layer becomes unavailable

---

## 4. What Is Missing (Enforcement Gaps)

### Gap 1: Validation Code for Dictionary Layer Unavailability

**Current state:** `MISSING_DICTIONARY_MEANING` exists (meaning is empty)  
**Missing:** A validation code for dictionary layer kind being unavailable  
**Needed:** New code `"PROVEN_REQUIRES_DICTIONARY_LAYER"` to distinguish:
- Empty meaning (already `MISSING_DICTIONARY_MEANING`)
- Unavailable layer kind (new code needed)

### Gap 2: `canMarkProven` Enforcement

**Current state:** Returns `true` if entry has term, meaning, and cut  
**Missing:** Check that `dictionaryLayer.kind !== "UNAVAILABLE"`  
**Needed:** Extend canMarkProven logic to include:
```typescript
const hasDictionaryLayer = entry.dictionaryLayer.kind !== "UNAVAILABLE";
return evidence && meaning && cut && dictionaryLayer;
```

### Gap 3: `setProofStatus()` Blocking

**Current state:** Only blocks if evidence is missing  
**Missing:** Blocks if dictionary layer is unavailable or meaning is empty  
**Needed:** Extend setProofStatus to check:
```typescript
if (newStatus === "PROVEN") {
  const hasEvidence = entry.evidence.length > 0;
  const hasMeaning = entry.dictionaryLayer.meaning.trim().length > 0;
  const hasLayer = entry.dictionaryLayer.kind !== "UNAVAILABLE";
  
  if (!hasEvidence || !hasMeaning || !hasLayer) {
    return { blocked: true, entry, reason: "..." };
  }
}
```

### Gap 4: `stabilizeEntry()` Downgrading

**Current state:** Only downgrades if evidence is removed  
**Missing:** Downgrades if dictionary layer becomes unavailable  
**Needed:** Extend stabilizeEntry to check after sync:
```typescript
if (synced.proofStatus === "PROVEN") {
  const hasEvidence = synced.evidence.length > 0;
  const hasMeaning = synced.dictionaryLayer.meaning.trim().length > 0;
  const hasLayer = synced.dictionaryLayer.kind !== "UNAVAILABLE";
  
  if (!hasEvidence || !hasMeaning || !hasLayer) {
    // Downgrade to UNDER_REVIEW with appropriate message
  }
}
```

---

## 5. Test-First Plan (Tests to Add Later)

### Tests That Should Fail First

Before any patch is implemented, these test cases should be added to `src/proof/proofCheck.ts` and should FAIL:

#### Test Set 1: Validation Code for Dictionary Layer

```javascript
// Test: Entry with UNAVAILABLE dictionary layer should report PROVEN_REQUIRES_DICTIONARY_LAYER
const entryUnavailableLayer = {
  ...createBlankEntry(),
  term: "example",
  dictionaryLayer: { kind: "UNAVAILABLE", meaning: "", notes: "" },
  evidence: [{ id: "e1", text: "proof", source: "test" }],
  proofStatus: "PROVEN"
};

const validation = validateEntry(entryUnavailableLayer);
assert.ok(
  validation.issues.some((issue) => issue.code === "PROVEN_REQUIRES_DICTIONARY_LAYER"),
  "PROVEN with UNAVAILABLE dictionary layer must report PROVEN_REQUIRES_DICTIONARY_LAYER."
);
```

#### Test Set 2: setProofStatus Blocking on Dictionary Layer

```javascript
// Test: Cannot transition to PROVEN if dictionary layer is UNAVAILABLE
const entryNoLayer = createBlankEntry();
entryNoLayer.term = "test";
entryNoLayer.dictionaryLayer = { kind: "UNAVAILABLE", meaning: "", notes: "" };
addEvidence(entryNoLayer, { text: "evidence", source: "test" });

const result = setProofStatus(entryNoLayer, "PROVEN");
assert.equal(
  result.blocked,
  true,
  "PROVEN transition must be blocked if dictionary layer is UNAVAILABLE."
);
assert.equal(
  result.entry.proofStatus,
  "DRAFT",
  "Blocked PROVEN attempt must not change proof status."
);
```

#### Test Set 3: stabilizeEntry Downgrading on Dictionary Layer Loss

```javascript
// Test: PROVEN entry downgrades if dictionary layer becomes UNAVAILABLE
const provenEntry = { ...createBlankEntry(), proofStatus: "PROVEN" };
provenEntry.evidence = [{ id: "e1", text: "proof", source: "test" }];
provenEntry.dictionaryLayer = { kind: "OFFICIAL", meaning: "stable", notes: "" };

const madeLossEntry = { ...provenEntry };
madeLossEntry.dictionaryLayer.kind = "UNAVAILABLE";

const downgraded = stabilizeEntry(madeLossEntry, false, "general");
assert.equal(
  downgraded.proofStatus,
  "UNDER_REVIEW",
  "PROVEN entry must downgrade if dictionary layer becomes UNAVAILABLE."
);
```

#### Test Set 4: canMarkProven Logic

```javascript
// Test: canMarkProven must return false if dictionary layer is UNAVAILABLE
const blankEntry = createBlankEntry();
blankEntry.term = "test";
blankEntry.dictionaryLayer = { kind: "UNAVAILABLE", meaning: "some meaning", notes: "" };
blankEntry.evidence = [{ id: "e1", text: "proof", source: "test" }];

const validation = validateEntry(blankEntry);
assert.equal(
  validation.canMarkProven,
  false,
  "canMarkProven must be false even with evidence if dictionary layer is UNAVAILABLE."
);
```

#### Test Set 5: Empty Meaning Blocking

```javascript
// Test: Cannot transition to PROVEN if dictionary meaning is empty
const entryNoMeaning = createBlankEntry();
entryNoMeaning.term = "test";
entryNoMeaning.dictionaryLayer = { kind: "OFFICIAL", meaning: "   ", notes: "" };
entryNoMeaning.evidence = [{ id: "e1", text: "evidence", source: "test" }];

const result = setProofStatus(entryNoMeaning, "PROVEN");
assert.equal(
  result.blocked,
  true,
  "PROVEN transition must be blocked if dictionary meaning is empty/whitespace."
);
```

---

## 6. Proposed Patch (Pseudocode for Later Implementation)

### File: `src/jewik-core/index.ts`

#### Change 1: Add Validation Code to Union Type

**Location:** Line ~64 (ValidationIssue type definition)

```typescript
code:
  | "MISSING_TERM"
  | "MISSING_DICTIONARY_MEANING"
  | "MISSING_CUT"
  | "MISSING_OPERATOR_MAPPING"
  | "PROVEN_REQUIRES_EVIDENCE"
  | "PROVEN_REQUIRES_DICTIONARY_LAYER"  // ← ADD THIS LINE
```

#### Change 2: Update `validateEntry()` Function

**Location:** Lines ~436-487

**Add after existing validation checks:**

```typescript
// Check if PROVEN without dictionary layer
if (
  entry.proofStatus === "PROVEN" &&
  (entry.dictionaryLayer.kind === "UNAVAILABLE" ||
    entry.dictionaryLayer.meaning.trim().length === 0)
) {
  issues.push({
    code: "PROVEN_REQUIRES_DICTIONARY_LAYER",
    severity: "error",
    message: "PROVEN status requires a stable dictionary layer.",
  });
}

// Update canMarkProven calculation
const hasDictionaryLayer = entry.dictionaryLayer.kind !== "UNAVAILABLE";
canMarkProven =
  !!entry.term &&
  !!entry.dictionaryLayer.meaning.trim() &&
  !!entry.jewikCut?.expression &&
  hasDictionaryLayer; // ← ADD THIS CONDITION
```

#### Change 3: Update `setProofStatus()` Function

**Location:** Lines ~489-514

**Extend blocking logic:**

```typescript
if (newStatus === "PROVEN") {
  const hasEvidence = entry.evidence.length > 0;
  const hasMeaning = entry.dictionaryLayer.meaning.trim().length > 0;
  const hasLayer = entry.dictionaryLayer.kind !== "UNAVAILABLE";

  if (!hasEvidence) {
    return {
      blocked: true,
      entry,
      reason: "PROVEN requires evidence.",
    };
  }

  if (!hasLayer) {
    return {
      blocked: true,
      entry,
      reason: "PROVEN requires dictionary layer to be available.",
    };
  }

  if (!hasMeaning) {
    return {
      blocked: true,
      entry,
      reason: "PROVEN requires dictionary meaning to be non-empty.",
    };
  }
}
```

#### Change 4: Update `stabilizeEntry()` Function

**Location:** Lines ~233-279

**Extend downgrade logic to handle dictionary layer:**

```typescript
export function stabilizeEntry(
  entry: LexiconEntry,
  touch: boolean = false,
  proofContractContext: "general" | "sanitize" | "remove-evidence" = "general",
): LexiconEntry {
  const synced = syncEntry(entry, touch);

  if (synced.proofStatus !== "PROVEN") {
    return synced;
  }

  // Check all three conditions for PROVEN validity
  const hasEvidence = synced.evidence.length > 0;
  const hasMeaning = synced.dictionaryLayer.meaning.trim().length > 0;
  const hasLayer = synced.dictionaryLayer.kind !== "UNAVAILABLE";

  if (!hasEvidence || !hasMeaning || !hasLayer) {
    let downgradeReason: string;

    if (!hasEvidence) {
      downgradeReason =
        proofContractContext === "remove-evidence"
          ? "evidence was removed"
          : "evidence is missing";
    } else if (!hasLayer) {
      downgradeReason = "dictionary layer became unavailable";
    } else {
      downgradeReason = "dictionary meaning became empty";
    }

    return syncEntry(
      appendHistoryIfMissing(
        {
          ...synced,
          proofStatus: "UNDER_REVIEW",
        },
        `Proof status downgraded to UNDER_REVIEW because ${downgradeReason}.`,
      ),
      false,
    );
  }

  return synced;
}
```

---

## 7. Implementation Risks & Mitigation

### Risk 1: Breaking Existing Workflows

**Risk:** Entries currently marked PROVEN with UNAVAILABLE dictionary layers will become invalid.

**Mitigation:**
- Scan database for entries with `proofStatus === "PROVEN"` and `dictionaryLayer.kind === "UNAVAILABLE"`
- Plan data migration to downgrade these entries before deployment
- Add entry in version history explaining why downgrade occurred

### Risk 2: Proof Gate False Positives

**Risk:** Existing test suite might expect PROVEN entries with empty dictionary meaning.

**Mitigation:**
- Run new test cases in test environment first
- Verify all 18+ existing assertions in Archive V3 still pass after patch
- If any fail, adjust test expectations (don't weaken the policy)

### Risk 3: UI Confusion

**Risk:** Users might not understand why PROVEN transitions are blocked.

**Mitigation:**
- Error messages must be clear: "Cannot mark as PROVEN without dictionary layer"
- UI should show validation issues preventing proof
- Documentation should explain the three-condition requirement

### Risk 4: Export Inconsistency

**Risk:** Export functions might show PROVEN status for invalid entries if stabilizeEntry is bypassed.

**Mitigation:**
- All export functions must call `stabilizeEntry()` before export
- Current implementation already does this; verify it's preserved

### Risk 5: Sanitization Edge Case

**Risk:** Imported entries with PROVEN status but no dictionary layer should be downgraded.

**Mitigation:**
- `sanitizeWorkbenchState()` must call stabilizeEntry() with "sanitize" context
- Current implementation already does this; verify it's preserved

---

## 8. STOP Rule

### Do Not Proceed If:

1. **Any code is modified** before explicit approval on this policy document
2. **src/jewik-core/index.ts is changed** without a new policy review cycle
3. **src/proof/proofCheck.ts is modified** without test-first methodology approval
4. **Tests are added** before this document is reviewed and approved
5. **setProofStatus() blocking logic is weakened** to pass old tests (the old tests must be updated, not the law)
6. **Three-condition enforcement is split across different contexts** without explicit justification

### Must Re-Review If:

- New validation codes are added beyond what's listed here
- Dictionary layer behavior changes in `createBlankEntry()`
- Export functions change their stabilization behavior
- Version history message format changes
- Test cases reveal the policy is impossible to enforce

---

## 9. Authority Chain

### Current Policy Authority

**Archive V3:** `371cea139581fb3c6c8bf6106a8d6ba508544dd5a6aa40ca2830b6ba20767106` (locked, immutable)

**This Document:** Policy definition only; no code changes until explicit approval

**Next Phase:** Test-driven implementation (add tests → verify they fail → implement patch → verify tests pass)

### What This Document Does NOT Do

- Does not implement any code
- Does not modify any source files
- Does not add or modify tests
- Does not change CI/CD configuration
- Does not affect project structure

### What This Document Prepares

- Clear policy statement for the law
- Test-first plan (tests to be added later)
- Pseudocode patches (to be implemented later)
- Risk assessment and mitigation
- Stop conditions to prevent scope drift

---

## 10. Summary Table

| Aspect | Status | Detail |
|--------|--------|--------|
| **Policy Definition** | ✅ Complete | NO_DICTIONARY_LAYER → NO_PROVEN |
| **Authority Baseline** | ✅ Locked | Archive V3 (2026-05-08) |
| **Current Code State** | ✅ Restored | All contamination removed |
| **Validation Code** | ⏳ Planned | PROVEN_REQUIRES_DICTIONARY_LAYER (not added yet) |
| **setProofStatus() Patch** | ⏳ Planned | Three-condition blocking (not implemented yet) |
| **stabilizeEntry() Patch** | ⏳ Planned | Dictionary layer downgrade logic (not implemented yet) |
| **Tests** | ⏳ Planned | 5 test sets ready to be added (not added yet) |
| **Proof Gate** | ✅ Passing | Archive V3 baseline still passes (18+ assertions) |

---

## 11. Next Recommended Phase

### Phase 1: Policy Review (Current)
- ✅ This document created
- ⏳ Stakeholder review of policy intent
- ⏳ Approval of three-condition requirement
- ⏳ Confirmation of test-first approach

### Phase 2: Test-Driven Development (After Approval)
1. Add all 5 test sets to `src/proof/proofCheck.ts`
2. Run `pnpm proof` → verify tests FAIL
3. Implement patches from Section 6
4. Run `pnpm proof` → verify tests PASS
5. Verify all 18+ Archive V3 tests still PASS
6. Create new Archive (V4) with locked baseline

### Phase 3: Deployment (After All Tests Pass)
1. Data migration for existing PROVEN entries with UNAVAILABLE layers
2. Version history audits for downgraded entries
3. Documentation update for users

---

**End of Policy Document**

**Status:** Ready for Review  
**Created:** 2026-05-08  
**No Code Changes Made:** ✅ Verified
