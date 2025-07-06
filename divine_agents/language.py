class Language:
    """Base class for languages."""

    name: str = "generic"

    def greet(self) -> str:
        raise NotImplementedError

    def farewell(self) -> str:
        raise NotImplementedError


class English(Language):
    """English language implementation."""

    name = "English"

    def greet(self) -> str:
        return "Hello"

    def farewell(self) -> str:
        return "Goodbye"


class Slovenian(Language):
    """Slovenian language implementation."""

    name = "Slovenian"

    def greet(self) -> str:
        return "Pozdravljeni"

    def farewell(self) -> str:
        return "Nasvidenje"
