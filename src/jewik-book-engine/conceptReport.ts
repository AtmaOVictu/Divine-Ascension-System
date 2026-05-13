import { seedConceptNodes } from "./seedData";
import type {
  AntinomyLink,
  CanonCandidate,
  ChapterCandidate,
  ConceptReport,
  ConnotationLink,
  SourceExcerpt,
} from "./types";

const relatedConceptMap: Record<string, string[]> = {
  ne: ["nič", "meja", "ločitev", "odsotnost", "da", "O", "razpoka"],
  o: ["nič", "krog", "celota", "odprtost"],
  biti: ["prisotnost", "sled", "telo"],
  razpoka: ["prelom", "rez", "verzija", "meja"],
  ego: ["jaz", "alarm", "namen"],
  telo: ["čutenje", "dih", "vertikala"],
};

const antinomyMap: Record<string, Array<{ opposite: string; note: string }>> = {
  ne: [
    { opposite: "da", note: "Ne in da tvorita osnovno odločilno antinomijo." },
    { opposite: "prisotnost", note: "Ne se v seedu pogosto kaže kot rob odsotnosti proti prisotnosti." },
  ],
  o: [{ opposite: "rez", note: "Krog in rez nosita nasprotni gibanji zaprtja in odprtja." }],
  biti: [{ opposite: "ne-biti", note: "Prisotnost se meri šele proti možnosti izgina." }],
  razpoka: [{ opposite: "sklenjenost", note: "Razpoka deluje proti prehitri zaprtosti sistema." }],
  ego: [{ opposite: "odprtost", note: "Ego zameji, odprtost pa razpre signal." }],
  telo: [{ opposite: "abstrakcija", note: "Telo vrača pomen v čutenje namesto čiste abstrakcije." }],
};

function tokenize(value: string): string[] {
  return value
    .toLocaleLowerCase("sl-SI")
    .replace(/[.,;:!?()[\]{}"'`]/g, " ")
    .split(/\s+/)
    .map((item) => item.trim())
    .filter((item) => item.length > 0);
}

function uniqueStrings(values: string[]): string[] {
  return [...new Set(values)];
}

function excerptMatchesTerm(excerpt: SourceExcerpt, term: string): boolean {
  const normalizedTerm = normalizeConcept(term);
  if (!normalizedTerm) {
    return false;
  }

  const hintHit = excerpt.conceptHints.some((hint) => normalizeConcept(hint) === normalizedTerm);
  if (hintHit) {
    return true;
  }

  return tokenize(excerpt.text).includes(normalizedTerm);
}

function buildDefinition(normalizedConcept: string, aliases: Record<string, string[]>): string {
  const conceptNode = seedConceptNodes.find((node) => node.normalizedTerm === normalizedConcept);
  if (conceptNode) {
    return conceptNode.draftDefinition;
  }

  const aliasText = (aliases[normalizedConcept] ?? []).join(", ");
  return aliasText
    ? `Osnutek definicije za ${normalizedConcept}: delovni pojem z aliasi ${aliasText}.`
    : `Osnutek definicije za ${normalizedConcept}: pojem še nima zbranih aliasov.`;
}

export function normalizeConcept(input: string): string {
  return input.trim().toLocaleLowerCase("sl-SI").replace(/\s+/g, " ");
}

export function findExactMatches(concept: string, excerpts: SourceExcerpt[]): SourceExcerpt[] {
  const normalizedConcept = normalizeConcept(concept);
  if (!normalizedConcept) {
    return [];
  }

  return excerpts.filter((excerpt) => excerptMatchesTerm(excerpt, normalizedConcept));
}

export function findAliasMatches(
  concept: string,
  aliases: Record<string, string[]>,
  excerpts: SourceExcerpt[],
): SourceExcerpt[] {
  const normalizedConcept = normalizeConcept(concept);
  const aliasList = aliases[normalizedConcept] ?? [];
  if (aliasList.length === 0) {
    return [];
  }

  const exactIds = new Set(findExactMatches(normalizedConcept, excerpts).map((excerpt) => excerpt.id));

  return excerpts.filter((excerpt) => {
    if (exactIds.has(excerpt.id)) {
      return false;
    }

    return aliasList.some((alias) => excerptMatchesTerm(excerpt, alias));
  });
}

export function buildConnotationLinks(
  concept: string,
  aliases: Record<string, string[]>,
): ConnotationLink[] {
  const normalizedConcept = normalizeConcept(concept);

  return (aliases[normalizedConcept] ?? []).map((alias) => ({
    id: `connotation-${normalizedConcept}-${normalizeConcept(alias)}`,
    concept: normalizedConcept,
    target: alias,
    note: `${normalizedConcept} se v seedu bere tudi kot ${alias}.`,
  }));
}

export function buildAntinomyLinks(concept: string): AntinomyLink[] {
  const normalizedConcept = normalizeConcept(concept);

  return (antinomyMap[normalizedConcept] ?? []).map((item) => ({
    id: `antinomy-${normalizedConcept}-${normalizeConcept(item.opposite)}`,
    concept: normalizedConcept,
    opposite: item.opposite,
    note: item.note,
  }));
}

export function buildChapterCandidates(
  concept: string,
  matches: SourceExcerpt[],
): ChapterCandidate[] {
  const normalizedConcept = normalizeConcept(concept);
  if (!normalizedConcept || matches.length === 0) {
    return [];
  }

  const relatedConcepts = uniqueStrings(
    matches.flatMap((match) => match.conceptHints.map((hint) => normalizeConcept(hint))),
  )
    .filter((hint) => hint !== normalizedConcept)
    .slice(0, 4);

  return [
    {
      id: `chapter-candidate-${normalizedConcept}`,
      title: normalizedConcept === "ne" ? "Beseda je Ne" : `Poglavje: ${normalizedConcept}`,
      status: matches.length > 1 ? "DRAFT" : "IDEA",
      summary:
        relatedConcepts.length > 0
          ? `Poglavje poveže ${normalizedConcept} z: ${relatedConcepts.join(", ")}.`
          : `Poglavje zadrži ${normalizedConcept} kot samostojen osnutek.`,
      supportingExcerptIds: matches.slice(0, 3).map((match) => match.id),
      relatedConcepts,
    },
  ];
}

export function buildCanonCandidates(
  concept: string,
  matches: SourceExcerpt[],
): CanonCandidate[] {
  const normalizedConcept = normalizeConcept(concept);
  if (!normalizedConcept || matches.length === 0) {
    return [];
  }

  return matches
    .filter((match) => match.status === "RELEVANT" || match.status === "CANON_CANDIDATE")
    .slice(0, 3)
    .map((match) => ({
      id: `canon-candidate-${normalizedConcept}-${match.id}`,
      concept: normalizedConcept,
      excerptId: match.id,
      sourceId: match.sourceId,
      reason: `${match.sourceTitle} že nosi relevanten ali canon kandidat signal.`,
    }));
}

export function buildConceptReport(
  concept: string,
  excerpts: SourceExcerpt[],
  aliases: Record<string, string[]>,
): ConceptReport {
  const normalizedConcept = normalizeConcept(concept);
  const exactMatches = findExactMatches(normalizedConcept, excerpts);
  const aliasMatches = findAliasMatches(normalizedConcept, aliases, excerpts);
  const combinedMatches = [...exactMatches, ...aliasMatches];
  const connotations = buildConnotationLinks(normalizedConcept, aliases);
  const antinomies = buildAntinomyLinks(normalizedConcept);
  const chapterCandidates = buildChapterCandidates(normalizedConcept, combinedMatches);
  const canonCandidates = buildCanonCandidates(normalizedConcept, combinedMatches);
  const relatedConcepts = uniqueStrings([
    ...(relatedConceptMap[normalizedConcept] ?? []),
    ...combinedMatches.flatMap((match) => match.conceptHints),
  ]).filter((item) => normalizeConcept(item) !== normalizedConcept);

  return {
    concept,
    normalizedConcept,
    definition: buildDefinition(normalizedConcept, aliases),
    relatedConcepts: relatedConcepts.slice(0, 7),
    exactMatches,
    aliasMatches,
    connotations,
    antinomies,
    chapterCandidates,
    canonCandidates,
  };
}
