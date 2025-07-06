class OntoSynonymAnalyzer:
    """Analyze synonym use and detect mismatches."""

    def __init__(self):
        # Map word to its expected synonym meaning
        self.synonyms = {
            "omogočiti": "aktivirati",
            "dovoliti": "dati dovoljenje",
            "sprejeti": "prihvatiti",
            "povedati": "izreči",
        }

    def check_synonym_error(self, word1: str, word2: str) -> bool:
        """Return True if word1 and word2 are not proper synonyms."""
        return word1 in self.synonyms and self.synonyms[word1] != word2

    def message(self, word1: str, word2: str) -> str:
        """Return an explanatory message for synonym usage."""
        if self.check_synonym_error(word1, word2):
            return f"Napaka: Besedi '{word1}' in '{word2}' nista pravi sinonimi v tem kontekstu."
        return "Sinonim je uporabljen pravilno."
