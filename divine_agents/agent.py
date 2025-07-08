from dataclasses import dataclass


@dataclass
class Emotion:
    """Represents the emotional state of an agent."""

    type: str = "neutral"  # e.g. fear, joy, anger
    level: float = 0.0      # intensity from 0 to 1


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion or Emotion()
        self.history = [state]

    def update_emotion(self, emotion_type: str, level: float) -> None:
        """Update emotion and adjust tension accordingly."""
        self.emotion.type = emotion_type
        self.emotion.level = level
        self.tension += level

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion.level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        prefix_map = {
            "fear": "S tresočim glasom, ",
            "joy": "Z veseljem, ",
            "anger": "Z jezo, ",
        }
        prefix = prefix_map.get(self.emotion.type, "")
        return prefix + base
