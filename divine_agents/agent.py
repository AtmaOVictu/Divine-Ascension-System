class Agent:
    """Ontological agent capable of transitioning states and adapting attributes."""

    STATES = ("Ego", "Jaz", "Enotnost")

    STATE_ATTRIBUTES = {
        "Ego": {
            "norm": "Samooskrba",
            "shape": "kocka",
            "moral_value": "Self-preservation",
        },
        "Jaz": {
            "norm": "Sodelovanje",
            "shape": "krogla",
            "moral_value": "Cooperation",
        },
        "Enotnost": {
            "norm": "Enotnost",
            "shape": "sfera",
            "moral_value": "Unity",
        },
    }

    def __init__(
        self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0
    ) -> None:
        """Initialize agent with ontological state and emotional parameters."""
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.norm = ""
        self.shape = ""
        self.moral_value = ""
        self.history = [state]

        self.apply_state_attributes()

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def change_norm(self) -> None:
        """Adjust normative guideline based on current state."""
        self.norm = self.STATE_ATTRIBUTES[self.state]["norm"]

    def change_shape(self) -> None:
        """Change physical or symbolic shape according to state."""
        self.shape = self.STATE_ATTRIBUTES[self.state]["shape"]

    def update_moral_value(self) -> None:
        """Update moral value tied to the state."""
        self.moral_value = self.STATE_ATTRIBUTES[self.state]["moral_value"]

    def apply_state_attributes(self) -> None:
        """Set normative, shape, and moral value based on current state."""
        self.change_norm()
        self.change_shape()
        self.update_moral_value()

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
            self.apply_state_attributes()
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return f"{base} Čutim močna čustva."
        return base
