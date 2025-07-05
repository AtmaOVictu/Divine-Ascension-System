"""Language models and registry for agent responses."""

from typing import Dict


class LanguageModel:
    """Represents a set of responses for a particular language."""

    def __init__(self, language: str, responses: Dict[str, str]):
        self.language = language
        self.responses = responses

    def response(self, state: str) -> str:
        return self.responses.get(state, "")


LANGUAGE_MODELS: Dict[str, LanguageModel] = {}


def register_language(language: str, responses: Dict[str, str]) -> None:
    """Register a new language model."""
    LANGUAGE_MODELS[language] = LanguageModel(language, responses)


# Default languages
register_language(
    "sloven\u0161\u010dina",
    {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z na\u0161imi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    },
)

register_language(
    "english",
    {
        "Ego": "Truth is absolute and independent of others.",
        "Jaz": "Truth is relative, shaped by our relationships.",
        "Enotnost": "All truths are one, interconnected.",
    },
)
