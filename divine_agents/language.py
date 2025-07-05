from dataclasses import dataclass

@dataclass
class LanguageModel:
    """Represents a language system with a unique identifier."""

    name: str
    identifier: str

    def confirm_transition(self) -> str:
        """Return confirmation message when transitioning to this language."""
        return f"\u221A Prehod v {self.name} ({self.identifier}) potrjen."
