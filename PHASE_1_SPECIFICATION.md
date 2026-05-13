# JEWIK TRUTHBASE WORKBENCH — PHASE 1 SPECIFICATION

**Document Status:** CODEX BUILD PLAN  
**Target Date:** Phase 1 Completion  
**Repo Root:** `C:\Users\Luka\Documents\Library\06_UI_APLIKACIJE\JEWIK_TRUTHBASE_STUDIO`  
**Boundary:** Phase 1 only. One entry. One dictionary layer. One JEWIK cut. One proof rule. One export. Max 3–5 file changes unless HOLD declared.

---

## 1. INVENTAR

**What exists (assumed, must verify):**
- Repo directory exists: `JEWIK_TRUTHBASE_STUDIO`
- Package manager (npm or yarn) may be initialized
- TypeScript configuration may exist
- React setup may exist
- Tauri setup may not exist

**What Codex must verify FIRST:**
- Is package.json present? What manager (npm/yarn/pnpm)?
- Is tsconfig.json present?
- Is src/ directory present?
- Is there an existing React app? (package.json with react dependency)
- Is Tauri installed? (Cargo.toml, tauri config present)
- Is SQLite library present? (package.json or Cargo.toml)
- How many files currently exist?

**What Phase 1 creates (minimum):**
```
jewik-core/src/
  ├── types.ts          (data model)
  ├── operators.ts      (JEWIK operator definitions)
  ├── validators.ts     (proof and entry validation)
  └── sampleEntry.ts    (one working example entry)

jewik-desktop/src/
  ├── App.tsx           (main React component)
  └── components/
      └── EntryDetail.tsx  (single entry UI)

storage/
  └── schema.sql        (SQLite schema for Phase 1A fallback)

exports/
  ├── sample-entry.md
  └── sample-entry.json

Root:
  ├── PHASE_1_SPECIFICATION.md (this file)
  ├── package.json (updated or created)
  └── tsconfig.json (verified or created)
```

**File change policy:**
- If repo is clean: create 5–7 new files ✓
- If repo has existing structure: integrate into src/, minimum changes ✓
- If Tauri setup would exceed 3 files: declare HOLD on Tauri, proceed with library + React only ✓
- If SQLite setup would exceed 3 files: Phase 1A builds library + file export, Phase 1B adds SQL ✓

---

## 2. PRODUCT GOAL

**JEWIK Truthbase Workbench — Phase 1**

Build a local-first, reusable TypeScript library (`jewik-core`) + a simple React UI (`jewik-desktop`) that proves this loop works:

1. **Create** one JEWIK lexical entry
2. **Classify** it as ordinary word OR internal operator
3. **Ground it** with a dictionary layer (manual or Fran/SSKJ reference)
4. **Cut it** with JEWIK/APD operator mapping
5. **Prove it** by adding evidence (cannot be PROVEN without evidence)
6. **Validate** it (blocked if proof is missing for ordinary words)
7. **Export** it as Markdown, JSON, or card text

**Success = one person can:**
- Open the app
- See or create one JEWIK entry with all layers visible
- Add/edit dictionary meaning
- Add/check JEWIK operator mapping
- Add proof evidence
- See validation status
- Export the entry
- Understand that the logic is in a reusable library, not the UI

**This is not:**
- A full lexicon
- A proof engine
- A cloud system
- An agent
- A philosophy manifesto

**This is:**
- A working tool
- A verified loop
- A foundation for Phase 2

---

## 3. TARGET STRUCTURE

**Root directory:**
```
JEWIK_TRUTHBASE_STUDIO/
├── package.json
├── tsconfig.json
├── README.md
├── PHASE_1_SPECIFICATION.md
├── CODEX_BUILD_PLAN.md
│
├── jewik-core/
│   ├── package.json (if monorepo, optional)
│   └── src/
│       ├── types.ts
│       ├── operators.ts
│       ├── validators.ts
│       ├── sampleEntry.ts
│       └── index.ts
│
├── jewik-desktop/
│   ├── package.json (if monorepo, optional)
│   ├── src/
│   │   ├── main.tsx
│   │   ├── App.tsx
│   │   └── components/
│   │       ├── EntryList.tsx
│   │       └── EntryDetail.tsx
│   └── index.html (if standalone React)
│
├── storage/
│   └── schema.sql (for Phase 1B, optional)
│
└── exports/
    ├── sample-entry.md
    └── sample-entry.json
```

**Actual file creation order (Codex):**
1. Verify repo structure with INVENTAR checklist
2. Create or update `package.json` and `tsconfig.json`
3. Create `jewik-core/src/types.ts`
4. Create `jewik-core/src/operators.ts`
5. Create `jewik-core/src/validators.ts`
6. Create `jewik-core/src/sampleEntry.ts`
7. Create `jewik-core/src/index.ts`
8. Create `jewik-desktop/src/App.tsx` and `EntryDetail.tsx`
9. Create `exports/sample-entry.md` and `.json`

**If existing structure differs:**
- Integrate into existing src/ with minimal moving
- Preserve existing dependencies
- Update import paths only if necessary
- Do NOT refactor unrelated code

---

## 4. DATA MODEL

### 4.1 Entry Type

```typescript
// jewik-core/src/types.ts

export type EntryType = 'ORDINARY_WORD' | 'INTERNAL_OPERATOR';

export type DictionaryStatus = 
  | 'DICTIONARY_PENDING' 
  | 'DICTIONARY_CONFIRMED' 
  | 'SOURCE_NEEDED' 
  | 'REVIEW';

export type ProofStatus = 
  | 'UNPROVEN' 
  | 'PENDING_EVIDENCE' 
  | 'PROVEN';

export interface DictionaryLayer {
  status: DictionaryStatus;
  meaning: string;          // Dictionary definition text
  source: string;           // "Fran", "SSKJ", "manual", "user_excerpt"
  sourceRef?: string;       // Link or page reference
  excerptText?: string;     // Manual dictionary excerpt
  notes?: string;           // Editorial notes
  lastUpdated: string;      // ISO 8601 timestamp
}

export interface JEWIKCut {
  operator?: string;        // ⊘ ∆ ∫ ∮ ⊢ ⧖ ⊥ ∴ ⟡ or custom
  meaning?: string;         // JEWIK/APD specific meaning
  antinomies?: string[];    // Related opposing concepts
  relation?: string;        // Relation to other entries
  notes?: string;           // Editorial notes
}

export interface Proof {
  status: ProofStatus;
  evidence: Evidence[];     // Array of evidence items
  validatedAt?: string;     // ISO 8601 timestamp
  validatedBy?: string;     // User/system name
  notes?: string;
}

export interface Evidence {
  type: 'DICTIONARY_SOURCE' | 'MANUAL_EXCERPT' | 'FILE_REFERENCE' | 'NOTE' | 'SYSTEM_DEFINITION';
  text: string;             // Evidence text
  source?: string;          // Source identifier
  timestamp: string;        // ISO 8601 timestamp
}

export interface JEWIKEntry {
  id: string;               // UUID or slug (e.g., "biti-001")
  term: string;             // The Slovenian term
  type: EntryType;
  
  dictionary: DictionaryLayer;
  jewikCut: JEWIKCut;
  proof: Proof;
  
  // Metadata
  createdAt: string;        // ISO 8601
  updatedAt: string;        // ISO 8601
  version: number;          // Incremental version
  exportText?: string;      // Cached export text
}
```

### 4.2 Validation Rules (enforced in validators.ts)

See Section 8: VALIDATION RULES AND PROOF LOGIC.

---

## 5. LIBRARY MODULES

### 5.1 jewik-core/src/types.ts
- TypeScript interface definitions (see 4.1)
- No logic, only types
- Exported to desktop and export systems

### 5.2 jewik-core/src/operators.ts
```typescript
// Define the fixed JEWIK/APD operators
export const INTERNAL_OPERATORS = {
  '⊘': { name: 'Nothing', definition: '... (from canon)' },
  '∆': { name: 'Paradoxical Movement', definition: '...' },
  '∫': { name: 'Integral of Feeling', definition: '...' },
  '∮': { name: 'Ethics of Recognition', definition: '...' },
  '⊢': { name: 'Proof/Assertion', definition: '...' },
  '⧖': { name: 'Time as Pulse', definition: '...' },
  '⊥': { name: 'Body as Vertical', definition: '...' },
  '∴': { name: 'Therefore/Absolute Truth', definition: '...' },
  '⟡': { name: 'Star of Cracks', definition: '...' },
};

export const isInternalOperator = (term: string): boolean => {
  return Object.keys(INTERNAL_OPERATORS).includes(term);
};

export const getOperatorDefinition = (op: string): string | null => {
  return INTERNAL_OPERATORS[op]?.definition || null;
};
```

### 5.3 jewik-core/src/validators.ts
```typescript
// Validation rules that enforce Phase 1 proof requirements

export function validateEntry(entry: JEWIKEntry): {
  isValid: boolean;
  errors: string[];
} {
  const errors: string[] = [];

  // Rule 1: Ordinary words must have dictionary layer
  if (entry.type === 'ORDINARY_WORD' && !entry.dictionary.meaning) {
    errors.push('Ordinary words require dictionary meaning.');
  }

  // Rule 2: Cannot be PROVEN without evidence
  if (entry.proof.status === 'PROVEN' && entry.proof.evidence.length === 0) {
    errors.push('Entry cannot be PROVEN without evidence.');
  }

  // Rule 3: Internal operators do not require dictionary lookup
  // (they are automatically valid for JEWIK layer)

  return {
    isValid: errors.length === 0,
    errors,
  };
}

export function canMarkProven(entry: JEWIKEntry): boolean {
  return entry.proof.evidence.length > 0 && validateEntry(entry).isValid;
}

export function blockFakeProof(entry: JEWIKEntry): {
  allowed: boolean;
  reason?: string;
} {
  if (entry.proof.status === 'PROVEN' && entry.proof.evidence.length === 0) {
    return {
      allowed: false,
      reason: 'PROOF_REQUIRES_EVIDENCE',
    };
  }
  return { allowed: true };
}
```

### 5.4 jewik-core/src/sampleEntry.ts
```typescript
// One working example entry showing all layers

import { JEWIKEntry } from './types';

export const sampleEntry: JEWIKEntry = {
  id: 'biti-001',
  term: 'biti',
  type: 'ORDINARY_WORD',
  
  dictionary: {
    status: 'DICTIONARY_CONFIRMED',
    meaning: 'to be; to exist; to have a certain quality',
    source: 'SSKJ',
    sourceRef: 'Fran/SSKJ biti',
    excerptText: 'biti — biti je osnovna biti vida biti je osnovna biti veda biti je osnovna biti vida biti je osnovna biti veda biti je osnovna biti veda',
    notes: 'Primary Slovenian infinitive. Core to JEWIK/APD system.',
    lastUpdated: '2026-05-08T00:00:00Z',
  },
  
  jewikCut: {
    operator: '∴',
    meaning: 'biti as the absolute beginning; the paradox that from nothingness (⊘) being arises (∆)',
    antinomies: ['ne-biti', 'sprememba'],
    relation: 'foundation operator for all subsequent terms',
    notes: 'biti is not a static state but a continuous paradoxical movement.',
  },
  
  proof: {
    status: 'PROVEN',
    evidence: [
      {
        type: 'DICTIONARY_SOURCE',
        text: 'biti — to be; to exist',
        source: 'SSKJ',
        timestamp: '2026-05-08T00:00:00Z',
      },
      {
        type: 'SYSTEM_DEFINITION',
        text: 'biti as paradoxical movement (∆) arising from nothing (⊘)',
        source: 'JEWIK/APD canon',
        timestamp: '2026-05-08T00:00:00Z',
      },
    ],
    validatedAt: '2026-05-08T00:00:00Z',
    validatedBy: 'system',
    notes: 'Sample entry for Phase 1 verification.',
  },
  
  createdAt: '2026-05-08T00:00:00Z',
  updatedAt: '2026-05-08T00:00:00Z',
  version: 1,
  exportText: '(generated on export)',
};
```

### 5.5 jewik-core/src/index.ts
```typescript
// Main export file for the library

export * from './types';
export * from './operators';
export * from './validators';
export { sampleEntry } from './sampleEntry';
```

---

## 6. MVP SCREENS

### 6.1 Main App Screen (App.tsx)

**Layout:**
```
┌─────────────────────────────────────────────────────────┐
│  JEWIK TRUTHBASE WORKBENCH — Phase 1                    │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  [+ New Entry]                                           │
│                                                           │
│  Entries List:                                          │
│  ┌───────────────────────────────────────────────────┐  │
│  │ biti-001 | ORDINARY_WORD | DICTIONARY_CONFIRMED  │  │
│  │ (click to view detail)                            │  │
│  └───────────────────────────────────────────────────┘  │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

**Components:**
- Header: "JEWIK TRUTHBASE WORKBENCH"
- Button: "+ New Entry"
- List: Entries with status badges
- Clicking entry → EntryDetail view

### 6.2 Entry Detail Screen (EntryDetail.tsx)

**Layout:**
```
┌──────────────────────────────────────────────────────────┐
│ Entry: biti (ID: biti-001)  [Edit] [Save] [Export]      │
├──────────────────────────────────────────────────────────┤
│                                                            │
│ TERM CLASSIFICATION                                       │
│ ┌────────────────────────────────────────────────────┐   │
│ │ Type: [ ORDINARY_WORD ▼ ]                          │   │
│ └────────────────────────────────────────────────────┘   │
│                                                            │
│ DICTIONARY LAYER                                         │
│ ┌────────────────────────────────────────────────────┐   │
│ │ Status: [DICTIONARY_CONFIRMED]                     │   │
│ │ Meaning: [text input]                              │   │
│ │ Source: [SSKJ ▼]                                   │   │
│ │ Source Ref: [text input]                           │   │
│ │ Manual Excerpt: [textarea]                         │   │
│ │ Notes: [textarea]                                  │   │
│ └────────────────────────────────────────────────────┘   │
│                                                            │
│ JEWIK CUT                                                │
│ ┌────────────────────────────────────────────────────┐   │
│ │ Operator: [∴ ▼]                                    │   │
│ │ JEWIK Meaning: [textarea]                          │   │
│ │ Antinomies: [text input, comma-separated]          │   │
│ │ Relation: [textarea]                               │   │
│ │ Notes: [textarea]                                  │   │
│ └────────────────────────────────────────────────────┘   │
│                                                            │
│ PROOF / EVIDENCE                                          │
│ ┌────────────────────────────────────────────────────┐   │
│ │ Proof Status: [UNPROVEN ▼]                         │   │
│ │                                                     │   │
│ │ Evidence Items:                                    │   │
│ │ ┌──────────────────────────────────────────────┐   │   │
│ │ │ [+ Add Evidence]                             │   │   │
│ │ │                                              │   │   │
│ │ │ 1. biti — to be (source: SSKJ)              │   │   │
│ │ │    [Remove]                                  │   │   │
│ │ │                                              │   │   │
│ │ │ 2. biti as ∴ from ⊘ (source: JEWIK canon)   │   │   │
│ │ │    [Remove]                                  │   │   │
│ │ └──────────────────────────────────────────────┘   │   │
│ │                                                     │   │
│ │ [✓ Mark PROVEN]  [Validation Status: OK]           │   │
│ └────────────────────────────────────────────────────┘   │
│                                                            │
│ EXPORT                                                    │
│ ┌────────────────────────────────────────────────────┐   │
│ │ [Export as Markdown]  [Export as JSON]             │   │
│ │ [Copy as Card Text]                                │   │
│ └────────────────────────────────────────────────────┘   │
│                                                            │
└──────────────────────────────────────────────────────────┘
```

**Behavior:**
- Single entry displayed with all four layers visible
- Each layer is editable (forms or textareas)
- Validation happens on Save
- "Mark PROVEN" button is disabled if no evidence exists
- Export buttons generate output immediately

---

## 7. VALIDATION RULES

### 7.1 Entry Validation

| Rule | Condition | Enforcement |
|------|-----------|-------------|
| **Ordinary words need dictionary** | `type === 'ORDINARY_WORD'` → must have `dictionary.meaning` | UI blocks Save until filled |
| **Cannot PROVEN without evidence** | `proof.status === 'PROVEN'` → `proof.evidence.length > 0` | Button disabled, error shown |
| **Internal operators skip dictionary** | `type === 'INTERNAL_OPERATOR'` → dictionary layer optional | No validation error |
| **Evidence type matches source** | If `type === 'DICTIONARY_SOURCE'`, source must be 'SSKJ' or 'Fran' | Dropdown validation |
| **All evidence needs timestamp** | Every Evidence object must have `timestamp` | Generated on add |

### 7.2 Save Validation

When user clicks "Save":
1. Run `validateEntry(entry)` from validators.ts
2. If errors exist: show error list, do not save
3. If valid: update `updatedAt` timestamp, increment `version`
4. Show success message

### 7.3 Proof Validation

When user clicks "Mark PROVEN":
1. Check `canMarkProven(entry)`
2. If false: show reason ("PROOF_REQUIRES_EVIDENCE"), do not allow
3. If true: set `proof.status = 'PROVEN'`, set `validatedAt` timestamp
4. Show success message

### 7.4 Fake Proof Block

```typescript
// In EntryDetail.tsx on Save:
const block = blockFakeProof(entry);
if (!block.allowed) {
  showError(`Cannot mark PROVEN: ${block.reason}`);
  return;
}
```

---

## 8. PROOF LOGIC

### 8.1 Phase 1 Proof Rule (Single Rule)

**Entry cannot be marked PROVEN without evidence.**

This is enforced in two places:

1. **UI Layer:** The "Mark PROVEN" button is **disabled** until evidence exists.
2. **Validation Layer:** `blockFakeProof()` returns `{ allowed: false }` if status is PROVEN but evidence is empty.

### 8.2 Evidence Entry Flow

1. User clicks "+ Add Evidence"
2. Modal or form appears with fields:
   - Type: [dropdown: DICTIONARY_SOURCE | MANUAL_EXCERPT | FILE_REFERENCE | NOTE | SYSTEM_DEFINITION]
   - Text: [textarea]
   - Source: [text input, optional]
3. User fills and clicks "Add Evidence"
4. Evidence item is appended to `proof.evidence` array
5. Evidence automatically gets a timestamp
6. If evidence exists, "Mark PROVEN" button becomes enabled

### 8.3 Proof Status Progression

```
UNPROVEN
  ↓
PENDING_EVIDENCE (user has added some evidence but not marked PROVEN yet)
  ↓
PROVEN (user clicks "Mark PROVEN" and validation passes)
```

In Phase 1: users manually toggle between UNPROVEN and PROVEN. No intermediate states needed.

### 8.4 Why This Matters

- **Prevents fake claims:** No entry can be marked proven without showing why
- **Simple and auditable:** Anyone can see what evidence supports the claim
- **Extensible:** Phase 2 can add automatic dictionary lookups, file hashing, etc.

---

## 9. EXPORT FORMATS

### 9.1 Export as Markdown

**Filename:** `{term}-{id}.md`  
**Example:** `biti-001.md`

```markdown
# biti

**ID:** biti-001  
**Type:** ORDINARY_WORD  
**Version:** 1  
**Last Updated:** 2026-05-08T00:00:00Z

## Dictionary Layer

**Status:** DICTIONARY_CONFIRMED  
**Meaning:** to be; to exist; to have a certain quality  
**Source:** SSKJ  
**Source Ref:** Fran/SSKJ biti

### Manual Excerpt
biti — biti je osnovna biti vida biti je osnovna biti veda biti je osnovna biti vida biti je osnovna biti veda biti je osnovna biti veda

### Notes
Primary Slovenian infinitive. Core to JEWIK/APD system.

---

## JEWIK Cut

**Operator:** ∴  
**JEWIK Meaning:** biti as the absolute beginning; the paradox that from nothingness (⊘) being arises (∆)  
**Antinomies:** ne-biti, sprememba  
**Relation:** foundation operator for all subsequent terms

### Notes
biti is not a static state but a continuous paradoxical movement.

---

## Proof

**Status:** PROVEN

### Evidence

1. biti — to be; to exist (Source: SSKJ)
2. biti as ∴ from ⊘ (Source: JEWIK/APD canon)

**Validated At:** 2026-05-08T00:00:00Z  
**Validated By:** system

---

*Generated by JEWIK Truthbase Workbench*
```

### 9.2 Export as JSON

**Filename:** `{term}-{id}.json`  
**Example:** `biti-001.json`

```json
{
  "id": "biti-001",
  "term": "biti",
  "type": "ORDINARY_WORD",
  "dictionary": {
    "status": "DICTIONARY_CONFIRMED",
    "meaning": "to be; to exist; to have a certain quality",
    "source": "SSKJ",
    "sourceRef": "Fran/SSKJ biti",
    "excerptText": "biti — biti je osnovna biti vida...",
    "notes": "Primary Slovenian infinitive. Core to JEWIK/APD system.",
    "lastUpdated": "2026-05-08T00:00:00Z"
  },
  "jewikCut": {
    "operator": "∴",
    "meaning": "biti as the absolute beginning...",
    "antinomies": ["ne-biti", "sprememba"],
    "relation": "foundation operator for all subsequent terms",
    "notes": "biti is not a static state..."
  },
  "proof": {
    "status": "PROVEN",
    "evidence": [
      {
        "type": "DICTIONARY_SOURCE",
        "text": "biti — to be; to exist",
        "source": "SSKJ",
        "timestamp": "2026-05-08T00:00:00Z"
      },
      {
        "type": "SYSTEM_DEFINITION",
        "text": "biti as paradoxical movement (∆) arising from nothing (⊘)",
        "source": "JEWIK/APD canon",
        "timestamp": "2026-05-08T00:00:00Z"
      }
    ],
    "validatedAt": "2026-05-08T00:00:00Z",
    "validatedBy": "system",
    "notes": "Sample entry for Phase 1 verification."
  },
  "createdAt": "2026-05-08T00:00:00Z",
  "updatedAt": "2026-05-08T00:00:00Z",
  "version": 1
}
```

### 9.3 Copy as Card Text

**Format:** Plain text, formatted for index cards or notes.

```
biti [biti-001]

Dictionary: to be; to exist; to have a certain quality (SSKJ)

JEWIK: biti as ∴ from ⊘ (paradoxical movement from nothing)

Proof: PROVEN
  - biti — to be (SSKJ)
  - biti as ∴ from ⊘ (JEWIK canon)

Antinomies: ne-biti, sprememba
```

---

## 10. CODEX BUILD PLAN

### Phase 1 Build Sequence (for Codex)

**STEP 0: INVENTAR Verification**

Codex runs this checklist FIRST:

```
[ ] Repo exists at C:\Users\Luka\Documents\Library\06_UI_APLIKACIJE\JEWIK_TRUTHBASE_STUDIO
[ ] package.json exists? YES/NO → what package manager?
[ ] tsconfig.json exists? YES/NO
[ ] src/ directory exists? YES/NO
[ ] Is React already set up? Check package.json for 'react' dependency.
[ ] Is TypeScript configured? Check tsconfig.json for compiler options.
[ ] Is Tauri installed? Check for Cargo.toml and tauri config.
[ ] Is SQLite present? Check package.json or Cargo.toml.
[ ] How many files currently in repo? Count.
[ ] Which files can be safely modified without breaking existing code?

OUTPUT: INVENTAR report
```

If issues found, Codex declares **HOLD** and reports to Claude before proceeding.

---

**STEP 1: Initialize TypeScript + React (if needed)**

```bash
# If no package.json:
npm init -y

# If no React:
npm install react react-dom
npm install --save-dev @types/react @types/react-dom

# If no TypeScript:
npm install --save-dev typescript

# Create tsconfig.json if missing
npx tsc --init
```

**Files affected:** package.json, tsconfig.json  
**Count:** 2 file changes

---

**STEP 2: Create jewik-core library structure**

```bash
mkdir -p jewik-core/src
mkdir -p jewik-desktop/src/components
mkdir -p storage
mkdir -p exports
```

**Files affected:** None (directories only)

---

**STEP 3: Create jewik-core/src/types.ts**

Copy TypeScript types from Section 5.1 above.

**File:** `jewik-core/src/types.ts`  
**Change count:** 1

---

**STEP 4: Create jewik-core/src/operators.ts**

Copy operator definitions from Section 5.2 above.

**File:** `jewik-core/src/operators.ts`  
**Change count:** 1

---

**STEP 5: Create jewik-core/src/validators.ts**

Copy validation logic from Section 5.3 above.

**File:** `jewik-core/src/validators.ts`  
**Change count:** 1

---

**STEP 6: Create jewik-core/src/sampleEntry.ts**

Copy sample entry from Section 5.4 above.

**File:** `jewik-core/src/sampleEntry.ts`  
**Change count:** 1

---

**STEP 7: Create jewik-core/src/index.ts**

Copy index/export from Section 5.5 above.

**File:** `jewik-core/src/index.ts`  
**Change count:** 1

---

**STEP 8: Create jewik-desktop/src/App.tsx**

Create main React component showing EntryList and switching to EntryDetail.

**File:** `jewik-desktop/src/App.tsx`  
**Change count:** 1

**Key code:**
```typescript
import { sampleEntry } from '../../jewik-core/src/sampleEntry';
import EntryDetail from './components/EntryDetail';
import { useState } from 'react';

export default function App() {
  const [selectedEntry, setSelectedEntry] = useState(sampleEntry);

  return (
    <div>
      <h1>JEWIK TRUTHBASE WORKBENCH — Phase 1</h1>
      <button onClick={() => alert('New entry not yet implemented')}>
        + New Entry
      </button>
      <h2>Entries List</h2>
      <div onClick={() => setSelectedEntry(sampleEntry)}>
        {sampleEntry.id} | {sampleEntry.type} | {sampleEntry.dictionary.status}
      </div>
      <EntryDetail entry={selectedEntry} />
    </div>
  );
}
```

---

**STEP 9: Create jewik-desktop/src/components/EntryDetail.tsx**

Create component showing all layers (Dictionary, JEWIK Cut, Proof, Export).

**File:** `jewik-desktop/src/components/EntryDetail.tsx`  
**Change count:** 1

**Key features:**
- Display all four layers
- "+ Add Evidence" button
- "Mark PROVEN" button (disabled if no evidence)
- "Export" buttons
- Validation on Save (show errors if validation fails)

---

**STEP 10: Create sample exports**

Generate sample-entry.md and sample-entry.json from sampleEntry.

**Files:**
- `exports/sample-entry.md`
- `exports/sample-entry.json`

**Change count:** 2

---

**STEP 11: Create main.tsx (if standalone React)**

If building standalone React (not Tauri yet):

```typescript
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
```

**File:** `jewik-desktop/src/main.tsx`  
**Change count:** 1

Create `index.html` pointing to main.tsx.

**File:** `jewik-desktop/index.html`  
**Change count:** 1

---

**TOTAL FILE CHANGES: 15**

**If this exceeds repo constraints:**

Declare **HOLD** and split into phases:

- **Phase 1A:** Create jewik-core library + one sample component (7 files)
- **Phase 1B:** Add React desktop UI (4 files)
- **Phase 1C:** Add Tauri wrapper (3–5 files)
- **Phase 1D:** Add SQLite + export refinement (2 files)

---

**Build verification (after all files created):**

```bash
# Check TypeScript compilation
npx tsc --noEmit

# Check imports
npm list

# Verify sampleEntry loads without errors
node -e "import { sampleEntry } from './jewik-core/src/sampleEntry.ts'; console.log(sampleEntry.id);"
```

If all succeed: Phase 1A complete.

---

## 11. RISKS

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| **Scope creep** (adding database, auth, cloud) | HIGH | CRITICAL | Codex adheres to "max 3–5 files unless HOLD" rule; HOLD declared before expansion |
| **Monorepo complexity** | MEDIUM | MEDIUM | Use simple folder structure; avoid workspaces in Phase 1; handle imports carefully |
| **Tauri setup failure** | MEDIUM | MEDIUM | If Tauri exceeds file budget, skip Tauri; build React-only MVP first (Phase 1A) |
| **Dictionary integration too broad** | MEDIUM | MEDIUM | Phase 1 uses manual dictionary input only; no live API lookups; Fran/SSKJ lookups deferred to Phase 2 |
| **Validation logic incomplete** | LOW | MEDIUM | Test validators.ts with sampleEntry before integrating into UI |
| **Export format bugs** | LOW | MEDIUM | Test Markdown and JSON exports against sampleEntry before release |
| **TypeScript path resolution** | MEDIUM | LOW | Set baseUrl and paths in tsconfig.json; test imports from App.tsx to jewik-core |
| **React state management too complex** | LOW | LOW | Phase 1 uses local state only; no Redux/Context; one entry at a time |

**Mitigation strategy:** If any risk emerges, Codex declares **HOLD** and reports to Claude before proceeding.

---

## 12. PHASE 1 SUCCESS CRITERIA

| Criterion | Definition | How to Verify |
|-----------|-----------|---------------|
| **App opens** | User can run the React app and see the main screen | Run `npm start` or dev server; UI loads without errors |
| **Entry displays** | Sample entry (biti) is visible with all four layers shown | Open EntryDetail; see dictionary, JEWIK cut, proof, export sections |
| **Dictionary layer editable** | User can edit dictionary meaning, source, excerpt fields | Click edit fields in EntryDetail; changes update the UI state |
| **Proof requires evidence** | "Mark PROVEN" button is disabled until evidence is added | Try clicking "Mark PROVEN" with zero evidence; button remains disabled |
| **Evidence can be added** | User can click "+ Add Evidence" and add evidence items | Add two evidence items; they appear in the list |
| **Cannot fake proof** | If user tries to mark PROVEN without evidence, app blocks it | Try Save with `status = 'PROVEN'` and empty evidence array; validator rejects it |
| **Validation shows errors** | If user tries to Save without dictionary meaning (ordinary word), app shows error | Try Save without dictionary.meaning; error message appears |
| **Export as Markdown works** | Clicking "Export as Markdown" generates correct .md format | Click export button; file matches Section 9.1 format |
| **Export as JSON works** | Clicking "Export as JSON" generates correct .json format | Click export button; JSON is valid and matches Section 9.2 |
| **Card text export works** | "Copy as Card Text" generates plain text format | Click button; text matches Section 9.3 format |
| **Library is reusable** | jewik-core can be imported in other projects | Import jewik-core in a test file; no errors |
| **Types are typed** | All functions have proper TypeScript types | Run `tsc --noEmit`; zero type errors |
| **Sample entry proves the loop** | sampleEntry contains all layers and can be exported | `validateEntry(sampleEntry)` returns `{ isValid: true }` |

**Definition of Done:** All 13 criteria pass. Code runs without errors. No scope expansion.

---

## APPENDIX: File Checklist for Codex

Before marking Phase 1 complete, verify these files exist and contain expected content:

```
✓ jewik-core/src/types.ts (contains JEWIKEntry, DictionaryLayer, Proof, Evidence interfaces)
✓ jewik-core/src/operators.ts (contains INTERNAL_OPERATORS object and helper functions)
✓ jewik-core/src/validators.ts (contains validateEntry, canMarkProven, blockFakeProof functions)
✓ jewik-core/src/sampleEntry.ts (contains sampleEntry export with biti example)
✓ jewik-core/src/index.ts (exports all of the above)
✓ jewik-desktop/src/App.tsx (displays entry list and switches to EntryDetail)
✓ jewik-desktop/src/components/EntryDetail.tsx (shows all four layers, evidence, export buttons)
✓ jewik-desktop/src/main.tsx (React entry point, if standalone)
✓ jewik-desktop/index.html (HTML root, if standalone)
✓ exports/sample-entry.md (Markdown export of biti entry)
✓ exports/sample-entry.json (JSON export of biti entry)
✓ package.json (updated with React, TypeScript, any needed deps)
✓ tsconfig.json (configured for TypeScript compilation)
✓ PHASE_1_SPECIFICATION.md (this file, in root)
```

---

**END OF SPECIFICATION**

---

## Quick Reference: One-Page Build Summary for Codex

**Goal:** One React app + one TypeScript library that proves the loop:  
`Create entry → Classify → Dictionary layer → JEWIK cut → Proof with evidence → Validate → Export`

**Success = App opens, shows biti entry, user can edit all layers, cannot fake proof, exports work.**

**Boundary:** Phase 1 only. One entry. Max 15 file changes (or HOLD). No cloud, auth, Tauri (unless fits in budget).

**Key Rule:** `Entry cannot be PROVEN without evidence.` (enforced in validators.ts and UI)

**Three layers before app:**
1. TypeScript types (types.ts)
2. Validation logic (validators.ts)
3. React UI components (App.tsx, EntryDetail.tsx)

**Three exports after app:**
1. Markdown (.md)
2. JSON (.json)
3. Card text (plain text)

**Next phase after Phase 1:** Database storage, multiple entries, dictionary API integration, Tauri desktop window.
