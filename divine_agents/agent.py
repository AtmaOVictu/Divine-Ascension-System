"""Ontological agent model."""

from dataclasses import dataclass, field


def numerology_value(word: str) -> int:
    """Calculate the numerological value of a word using a=1, b=2 ..."""
    return sum(ord(c.lower()) - 96 for c in word if c.isalpha())


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: list[str] = field(default_factory=list)

    SYMBOLS = {
        "Ego": "⊘",
        "Jaz": "∫(dru/x)",
        "Enotnost": "RES001",
    }

    def __post_init__(self) -> None:
        self.history.append(self.state)
        self.num_value = numerology_value(self.state)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        self.num_value = numerology_value(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            principle = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            principle = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            principle = "Vse resnice so eno, medsebojno povezane."
        return principle

    def symbol(self) -> str:
        """Return symbolic representation of the current state."""
        return self.SYMBOLS.get(self.state, self.state)

    def philosophical_line(self, question: str) -> str:
        """Generate a dialogue line incorporating state and emotion."""
        base = self.respond(question)
        return f"{self.name} ({self.symbol()}): {base} (čustvo={self.emotion:.2f})"
