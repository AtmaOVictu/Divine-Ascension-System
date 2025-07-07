from .symbolic_box import ExtraSymbolicBox


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent maintains an extra symbolic box that mirrors its current state
    and acts as a fallback container for transition data. This additional box
    ensures that transitions can be validated and, if necessary, reverted.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        # Maintain an extra symbolic box mirroring the agent's state.
        self.extra_box = ExtraSymbolicBox(stage=state, data={"name": name})

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.extra_box.update_data({"emotion": self.emotion, "tension": self.tension})

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.extra_box.update_data({"tension": self.tension})

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        old_state = self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        # mirror the transition in the extra box for validation/fallback
        self.extra_box.transition(self.state, {"prev_state": old_state})
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
            return f"{base} (čustveni naboj: {self.emotion:.1f})"
        return base
