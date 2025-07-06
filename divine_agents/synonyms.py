"""Synonym analysis utilities for ontological contexts."""

from typing import Dict


class OntoSynonymAnalyzer:
    """Analyzer to check if word pairs are valid synonyms in a given context."""

    def __init__(self, synonyms: Dict[str, str] | None = None) -> None:
        self.synonyms: Dict[str, str] = synonyms or {
            "omogočiti": "aktivirati",
            "dovoliti": "dati dovoljenje",
            "sprejeti": "prihvatiti",
            "povedati": "izreči",
        }

    def check_synonym_error(self, word1: str, word2: str) -> bool:
        """Return True if a synonym mismatch is detected."""
        return word1 in self.synonyms and self.synonyms[word1] != word2

    def explain(self, word1: str, word2: str) -> str:
        """Return explanation for potential synonym misuse."""
        if self.check_synonym_error(word1, word2):
            correct = self.synonyms[word1]
            return (
                f"Napaka: Besedi '{word1}' in '{word2}' nista pravilna sinonima. "
                f"'{word1}' pomeni '{correct}'."
            )
        return "Sinonim je uporabljen pravilno."
