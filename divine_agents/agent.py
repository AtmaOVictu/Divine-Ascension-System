from .transitions import biological_transition, social_transition


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

    def evolve(
        self,
        t: float,
        k_bio: float = 1.0,
        c_bio: float = 0.5,
        k_soc: float = 1.5,
        c_soc: float = 0.6,
    ) -> str:
        """Evolve the agent through biological and social transitions."""
        bio = biological_transition(t, k_bio, c_bio)
        soc = social_transition(t, k_soc, c_soc)
        self.update_emotion(bio)
        self.update_tension(self.tension + soc)
        return self.transition()

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
        emotional_suffix = ""
        if self.emotion > 0.7:
            emotional_suffix = " Moja custva so mocna."  # Slovenian accent
        if self.state == "Ego":
            return (
                "Resnica je absolutna in neodvisna od drugih." + emotional_suffix
            )
        if self.state == "Jaz":
            return (
                "Resnica je relativna, oblikovana z nasimi odnosi." + emotional_suffix
            )
        return "Vse resnice so eno, medsebojno povezane." + emotional_suffix
