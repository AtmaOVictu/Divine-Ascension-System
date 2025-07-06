class Language:
    """Base class for language translations."""
    def __init__(self, name: str, translations: dict):
        self.name = name
        self.translations = translations

    def translate(self, key: str) -> str:
        """Return translation for the given key."""
        return self.translations.get(key, key)


class English(Language):
    def __init__(self):
        super().__init__("English", {
            "hello": "Hello",
            "truth": "Truth is absolute",
        })


class Slovene(Language):
    def __init__(self):
        super().__init__("Slovene", {
            "hello": "Pozdravljeni",
            "truth": "Resnica je relativna",
        })
