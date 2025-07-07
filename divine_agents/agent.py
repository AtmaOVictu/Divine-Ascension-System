from .symbolic_box import SymbolicBox


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 box: SymbolicBox | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.box = box if box else SymbolicBox(stage=state, data={"agent": name, "state": state})
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.box.update_data({"emotion": self.emotion, "tension": self.tension})

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.box.update_data({"tension": self.tension})

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.box.transition(self.state, {"tension": self.tension, "emotion": self.emotion})
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        mood = "umirjeno" if self.emotion <= 0.5 else "z veliko čustva"
        return f"{base} ({mood})"
