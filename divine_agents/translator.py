class Translator:
    """Simplistic translator agent with history."""

    def __init__(self, name: str, language: str = "Sloven\u0161\u010dina") -> None:
        self.name = name
        self.language = language
        self.history = []  # store tuples of (src_lang, target_lang, text, translation)

    def translate(self, text: str, target_language: str) -> str:
        """Translate text to target_language and store the record."""
        translation = self._mock_translate(text, target_language)
        self.history.append((self.language, target_language, text, translation))
        self.language = target_language
        return translation

    @staticmethod
    def _mock_translate(text: str, target_language: str) -> str:
        """Return a mocked translation string."""
        if target_language == "Angle\u0161\u010dina":
            return f"Translated to English: {text}"
        if target_language == "Nem\u0161\u010dina":
            return f"\u00dcbersetzt ins Deutsche: {text}"
        return f"Prevajanje ni podprto za jezik: {target_language}"

    def reflect_translations(self) -> str:
        """Return a summary of all translations performed."""
        lines = []
        for src, trg, original, result in self.history:
            lines.append(f"{src}->{trg}: {original} => {result}")
        return "\n".join(lines)


class EternalAnalysis:
    """Container for storing analyses of translations."""

    def __init__(self) -> None:
        self.records = []

    def analyze(self, record: tuple) -> str:
        """Store a simple analysis of the given translation record."""
        analysis = f"Analiza prevoda: {record[2]} --> {record[3]}"
        self.records.append(analysis)
        return analysis

    def summary(self) -> str:
        """Return all stored analyses."""
        return "\n".join(self.records)
