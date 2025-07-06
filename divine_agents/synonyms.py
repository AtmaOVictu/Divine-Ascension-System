class OntoSynonymAnalyzer:
    """Analyze and validate synonym usage in context."""

    def __init__(self):
        # Basic synonyms mapped to their core meaning
        self.synonyms = {
            "omogočiti": "aktivirati",
            "dovoliti": "dati dovoljenje",
            "sprejeti": "prihvatiti",
            "povedati": "izreči",
        }

    def check_synonym_error(self, word1: str, word2: str) -> str:
        """Return an error message if words are misused as synonyms."""
        if word1 in self.synonyms and self.synonyms[word1] != word2:
            return f"Napaka: Besedi '{word1}' in '{word2}' nista pravi sinonimi v tem kontekstu."
        return "Sinonim je uporabljen pravilno."
