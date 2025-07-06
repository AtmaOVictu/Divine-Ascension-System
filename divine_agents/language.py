class Language:
    """Basic representation of a natural language."""

    def __init__(self, name: str, vocabulary: dict | None = None):
        self.name = name
        self.vocabulary = vocabulary or {}

    def translate(self, term: str) -> str:
        """Return a translated term if available."""
        return self.vocabulary.get(term, term)


class English(Language):
    """English language module."""

    def __init__(self):
        super().__init__("English", {
            "hello": "Hello",
            "truth": "truth",
        })


class Slovenian(Language):
    """Slovenian language module."""

    def __init__(self):
        super().__init__("Slovenian", {
            "hello": "Pozdravljeni",
            "truth": "resnica",
        })


def create_language(name: str) -> Language:
    """Factory method used to create language modules by name."""
    normalized = name.lower()
    if normalized in {"english", "en"}:
        return English()
    if normalized in {"slovenian", "sl", "slovene"}:
        return Slovenian()
    return Language(name)
