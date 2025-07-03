class Translator:
    """Simple translation utility for phrases used by agents."""
    def __init__(self):
        self.translations = {
            "Resnica je absolutna in neodvisna od drugih.": {
                "sl": "Resnica je absolutna in neodvisna od drugih.",
                "en": "Truth is absolute and independent of others."
            },
            "Resnica je relativna, oblikovana z našimi odnosi.": {
                "sl": "Resnica je relativna, oblikovana z našimi odnosi.",
                "en": "Truth is relative, shaped by our relationships."
            },
            "Vse resnice so eno, medsebojno povezane.": {
                "sl": "Vse resnice so eno, medsebojno povezane.",
                "en": "All truths are one, interconnected."
            },
        }

    def translate(self, phrase: str, language: str = "en") -> str:
        """Translate a phrase into the selected language."""
        return self.translations.get(phrase, {}).get(language, phrase)
