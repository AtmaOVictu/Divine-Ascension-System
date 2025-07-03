class Translator:
    """Simple dictionary-based translator for tasks and responses."""

    def __init__(self) -> None:
        self.translations = {
            "samospoznanje": {"sl": "samospoznanje", "en": "self-awareness"},
            "logični prehod": {"sl": "logični prehod", "en": "logical transition"},
            "emotivni prehod": {"sl": "emotivni prehod", "en": "emotional transition"},
            "nova naloga": {"sl": "nova naloga", "en": "new task"},
            "kritična napaka": {"sl": "kritična napaka", "en": "critical error"},
            "sprememba stanja": {"sl": "sprememba stanja", "en": "state change"},
        }
        self.responses = {
            "Ego": {
                "sl": "Resnica je absolutna in neodvisna od drugih.",
                "en": "Truth is absolute and independent of others.",
            },
            "Jaz": {
                "sl": "Resnica je relativna, oblikovana z našimi odnosi.",
                "en": "Truth is relative and shaped by our relationships.",
            },
            "Enotnost": {
                "sl": "Vse resnice so eno, medsebojno povezane.",
                "en": "All truths are one and interconnected.",
            },
        }

    def translate(self, text: str, language: str = "en") -> str:
        """Translate known task keywords; return original if unknown."""
        return self.translations.get(text, {}).get(language, text)

    def response(self, state: str, language: str = "sl") -> str:
        """Return a philosophical response translation for a given state."""
        return self.responses.get(state, {}).get(language, "")
