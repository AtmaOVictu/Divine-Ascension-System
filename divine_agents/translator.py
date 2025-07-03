class Translator:
    """Simple dictionary-based translator for task names."""

    def __init__(self):
        self.translations = {
            "samospoznanje": {"sl": "samospoznanje", "en": "self-awareness"},
            "self-awareness": {"sl": "samospoznanje", "en": "self-awareness"},
            "logični prehod": {"sl": "logični prehod", "en": "logical transition"},
            "logical transition": {"sl": "logični prehod", "en": "logical transition"},
            "emotivni prehod": {"sl": "emotivni prehod", "en": "emotional transition"},
            "emotional transition": {"sl": "emotivni prehod", "en": "emotional transition"},
            "nova naloga": {"sl": "nova naloga", "en": "new task"},
            "new task": {"sl": "nova naloga", "en": "new task"},
            "kritična napaka": {"sl": "kritična napaka", "en": "critical error"},
            "critical error": {"sl": "kritična napaka", "en": "critical error"},
            "sprememba stanja": {"sl": "sprememba stanja", "en": "state change"},
            "state change": {"sl": "sprememba stanja", "en": "state change"},
        }

    def translate(self, task: str, language: str = "en") -> str:
        """Translate a task name into the given language."""
        return self.translations.get(task, {}).get(language, task)
