class Language:
    """Simple language module for philosophical responses."""

    def __init__(self, name: str, code: str, responses: dict):
        self.name = name
        self.code = code
        self.responses = responses

    def translate(self, key: str) -> str:
        """Return the translation for a given key."""
        return self.responses.get(key, key)


class Slovenian(Language):
    """Privzeti slovenski prevodi."""

    def __init__(self):
        responses = {
            "truth_absolute": "Resnica je absolutna in neodvisna od drugih.",
            "truth_relative": "Resnica je relativna, oblikovana z našimi odnosi.",
            "truth_unified": "Vse resnice so eno, medsebojno povezane.",
        }
        super().__init__("Slovenian", "sl", responses)


class English(Language):
    """English translations of philosophical responses."""

    def __init__(self):
        responses = {
            "truth_absolute": "Truth is absolute and independent of others.",
            "truth_relative": "Truth is relative, shaped by our relationships.",
            "truth_unified": "All truths are one, interconnected.",
        }
        super().__init__("English", "en", responses)
