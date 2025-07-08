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

    def reflect(self) -> str:
        """Generate a reflection string capturing the agent's current state."""
        reflection = (
            f"{self.name} ({self.state}) reflects with emotion {self.emotion:.2f}"
        )
        return reflection

    def learn_from_others(self, reflections: list[str]) -> None:
        """Adjust tension based on reflections from other agents."""
        for entry in reflections:
            if self.name not in entry and "Ego" in entry:
                self.tension += 0.1

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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def dialogue_response(self) -> str:
        """Return a response influenced by emotional state."""
        base = self.respond("Kaj je resnica?")
        if self.emotion > 0.5:
            if self.state == "Ego":
                return f"Močno verjamem: {base}"
            if self.state == "Jaz":
                return f"Globoko čutim, da {base}"
            return f"Z mirnostjo spoznavam, da {base}"
        return base
