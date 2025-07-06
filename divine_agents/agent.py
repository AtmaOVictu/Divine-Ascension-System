"""Agent module implementing ontological state transitions and responses."""

from .numerology import numerological_value


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

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
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion and state."""
        prefix = "" if self.emotion <= 0.5 else "Čustveno: "
        if self.state == "Ego":
            text = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            text = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            text = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix}{text}"

    # ------------------------------------------------------------------
    # Decision making utilities
    # ------------------------------------------------------------------
    def numerology(self) -> tuple[float, float, float]:
        """Return numerological values for emotion, tension and history."""
        e_num = numerological_value(self.emotion, scale=1)
        t_num = numerological_value(self.tension, scale=1)
        h_num = numerological_value(len(self.history), scale=10)
        return e_num, t_num, h_num

    def make_decision(self) -> str:
        """Make a simple decision based on numerological interpretation."""
        e_num, t_num, h_num = self.numerology()
        if t_num > 7:
            return f"{self.name} becomes defensive."
        if e_num > 6:
            return f"{self.name} is emotional and reactive."
        if h_num < 5:
            return f"{self.name} is cautious due to lack of experience."
        return f"{self.name} is balanced and ready for strategic decisions."
