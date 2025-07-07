from .extra_box import ExtraSymbolicBox


class Agent:
    """Represent an ontological agent capable of transitioning states.

    Each agent maintains an ``ExtraSymbolicBox`` which acts as a safety
    buffer for state changes and stores auxiliary data about the agent.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        # Extra box used for buffering state transitions
        self.extra_box = ExtraSymbolicBox(stage=state, data={"name": name})

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.extra_box.update_data({"emotion": self.emotion})

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.extra_box.update_data({"tension": self.tension})

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self.extra_box.transition(self.state, {"transitioned": True})
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            tone = " (izraza mocna custva)"
        else:
            tone = ""
        return base + tone
