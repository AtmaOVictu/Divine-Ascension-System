class Translator:
    """Simple translator between Slovenian and English."""

    def __init__(self):
        self.translations = {
            "Kaj je resnica?": {"sl": "Kaj je resnica?", "en": "What is truth?"},
            "Resnica je absolutna in neodvisna od drugih.": {
                "sl": "Resnica je absolutna in neodvisna od drugih.",
                "en": "Truth is absolute and independent of others.",
            },
            "Resnica je relativna, oblikovana z našimi odnosi.": {
                "sl": "Resnica je relativna, oblikovana z našimi odnosi.",
                "en": "Truth is relative, shaped by our relationships.",
            },
            "Vse resnice so eno, medsebojno povezane.": {
                "sl": "Vse resnice so eno, medsebojno povezane.",
                "en": "All truths are one, interconnected.",
            },
        }

    def translate(self, text: str, language: str) -> str:
        """Return translation if available."""
        return self.translations.get(text, {}).get(language, text)
