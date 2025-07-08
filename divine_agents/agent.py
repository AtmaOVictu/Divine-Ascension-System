class Agent:
    """Ontological agent capable of transitioning emotional states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    STATE_VALUES = {
        "Ego": complex(1, 1),       # 1 + i
        "Jaz": complex(0, 1),       # 0 + i
        "Enotnost": complex(2, 0),  # 2
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.state_value = self.STATE_VALUES[state]
        self.history = [state]

    def _update_state_value(self) -> None:
        """Update the complex representation of the agent's state."""
        base = self.STATE_VALUES[self.state]
        self.state_value = complex(base.real + self.tension, base.imag)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = max(0.0, min(1.0, value))
        self.tension += self.emotion
        self._update_state_value()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))
        self._update_state_value()

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self.history.append(self.state)
            self._update_state_value()
        else:
            self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state."""
        prefix = "" if self.emotion < 0.3 else "Čustveno "
        if self.state == "Ego":
            text = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            text = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            text = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix}{text}"
