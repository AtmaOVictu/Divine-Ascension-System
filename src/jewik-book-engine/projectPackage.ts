import {
  normalizeProjectWorkspaceSnapshot,
  type ProjectWorkspaceSnapshot,
} from "./storage";
import type { ChapterDraft, SourceExcerpt } from "./types";

export const PROJECT_PACKAGE_TYPE = "jewik.project-package";
export const PROJECT_PACKAGE_VERSION = 1;

export type ProjectPackageProjectRef = {
  id: string;
  name: string;
};

export type ProjectPackageV1 = {
  packageVersion: 1;
  packageType: typeof PROJECT_PACKAGE_TYPE;
  exportedAt: string;
  project: ProjectPackageProjectRef;
  workspace: ProjectWorkspaceSnapshot;
};

export type ProjectPackageParseResult =
  | {
      ok: true;
      value: ProjectPackageV1;
    }
  | {
      ok: false;
      code:
        | "INVALID_JSON"
        | "INVALID_PACKAGE_TYPE"
        | "UNSUPPORTED_PACKAGE_VERSION"
        | "INVALID_PROJECT"
        | "INVALID_WORKSPACE"
        | "INVALID_EXPORTED_AT"
        | "INVALID_PACKAGE";
      message: string;
    };

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null;
}

function isNonEmptyString(value: unknown): value is string {
  return typeof value === "string" && value.trim().length > 0;
}

function isStringArray(value: unknown): value is string[] {
  return Array.isArray(value) && value.every((item) => typeof item === "string");
}

function isIsoDateTimeString(value: unknown): value is string {
  return typeof value === "string" && value.length > 0 && Number.isFinite(Date.parse(value));
}

function isDraftState(value: unknown): value is ProjectWorkspaceSnapshot["draftState"] {
  return value === "shranjeno" || value === "nespremenjeno" || value === "osnutek";
}

function isChapterDraft(value: unknown): value is ChapterDraft {
  if (!isRecord(value)) {
    return false;
  }

  return (
    typeof value.id === "string" &&
    typeof value.bookId === "string" &&
    typeof value.title === "string" &&
    typeof value.status === "string" &&
    typeof value.text === "string" &&
    isStringArray(value.linkedExcerptIds) &&
    isStringArray(value.linkedConcepts) &&
    isStringArray(value.variants) &&
    typeof value.currentVariant === "string" &&
    typeof value.updatedAt === "string"
  );
}

function isSourceExcerpt(value: unknown): value is SourceExcerpt {
  if (!isRecord(value)) {
    return false;
  }

  return (
    typeof value.id === "string" &&
    typeof value.sourceId === "string" &&
    typeof value.sourceTitle === "string" &&
    typeof value.locator === "string" &&
    typeof value.text === "string" &&
    typeof value.status === "string" &&
    typeof value.note === "string" &&
    isStringArray(value.conceptHints)
  );
}

function isProjectWorkspaceSnapshot(value: unknown): value is ProjectWorkspaceSnapshot {
  if (!isRecord(value)) {
    return false;
  }

  return (
    typeof value.activeConcept === "string" &&
    typeof value.bookMessage === "string" &&
    typeof value.conceptInput === "string" &&
    isDraftState(value.draftState) &&
    typeof value.lastSavedSnapshot === "string" &&
    Array.isArray(value.excerpts) &&
    value.excerpts.every(isSourceExcerpt) &&
    isChapterDraft(value.chapterDraft)
  );
}

function cloneWorkspace(workspace: ProjectWorkspaceSnapshot): ProjectWorkspaceSnapshot {
  return normalizeProjectWorkspaceSnapshot(workspace);
}

function cloneProject(project: ProjectPackageProjectRef): ProjectPackageProjectRef {
  return {
    id: project.id,
    name: project.name,
  };
}

function validateProjectPackage(value: unknown): ProjectPackageParseResult {
  if (!isRecord(value)) {
    return {
      ok: false,
      code: "INVALID_PACKAGE",
      message: "ProjectPackage must be an object.",
    };
  }

  if (value.packageType !== PROJECT_PACKAGE_TYPE) {
    return {
      ok: false,
      code: "INVALID_PACKAGE_TYPE",
      message: "ProjectPackage type is invalid.",
    };
  }

  if (value.packageVersion !== PROJECT_PACKAGE_VERSION) {
    return {
      ok: false,
      code: "UNSUPPORTED_PACKAGE_VERSION",
      message: "ProjectPackage version is unsupported.",
    };
  }

  if (!isIsoDateTimeString(value.exportedAt)) {
    return {
      ok: false,
      code: "INVALID_EXPORTED_AT",
      message: "ProjectPackage exportedAt must be a valid ISO datetime string.",
    };
  }

  if (
    !isRecord(value.project) ||
    !isNonEmptyString(value.project.id) ||
    !isNonEmptyString(value.project.name)
  ) {
    return {
      ok: false,
      code: "INVALID_PROJECT",
      message: "ProjectPackage project reference is invalid.",
    };
  }

  if (!isProjectWorkspaceSnapshot(value.workspace)) {
    return {
      ok: false,
      code: "INVALID_WORKSPACE",
      message: "ProjectPackage workspace snapshot is invalid.",
    };
  }

  return {
    ok: true,
    value: {
      packageVersion: PROJECT_PACKAGE_VERSION,
      packageType: PROJECT_PACKAGE_TYPE,
      exportedAt: value.exportedAt,
      project: cloneProject(value.project),
      workspace: cloneWorkspace(value.workspace),
    },
  };
}

export function createProjectPackage(
  project: ProjectPackageProjectRef,
  workspace: ProjectWorkspaceSnapshot,
  exportedAt = new Date().toISOString(),
): ProjectPackageV1 | null {
  if (!isNonEmptyString(project.id) || !isNonEmptyString(project.name)) {
    return null;
  }

  if (!isIsoDateTimeString(exportedAt) || !isProjectWorkspaceSnapshot(workspace)) {
    return null;
  }

  return {
    packageVersion: PROJECT_PACKAGE_VERSION,
    packageType: PROJECT_PACKAGE_TYPE,
    exportedAt,
    project: cloneProject({
      id: project.id,
      name: project.name.trim(),
    }),
    workspace: cloneWorkspace(workspace),
  };
}

export function serializeProjectPackage(projectPackage: ProjectPackageV1): string {
  return JSON.stringify(projectPackage, null, 2);
}

export function parseProjectPackage(jsonText: string): ProjectPackageParseResult {
  try {
    return validateProjectPackage(JSON.parse(jsonText) as unknown);
  } catch {
    return {
      ok: false,
      code: "INVALID_JSON",
      message: "ProjectPackage JSON could not be parsed.",
    };
  }
}

export function isProjectPackage(value: unknown): value is ProjectPackageV1 {
  return validateProjectPackage(value).ok;
}

export function readWorkspaceFromProjectPackage(
  projectPackage: unknown,
): ProjectWorkspaceSnapshot | null {
  const result = validateProjectPackage(projectPackage);
  return result.ok ? cloneWorkspace(result.value.workspace) : null;
}
