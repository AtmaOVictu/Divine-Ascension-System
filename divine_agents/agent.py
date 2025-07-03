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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."


class SelfDeceptionAgent(Agent):
    """Agent that resists transitions by rationalizing comfort in the current state."""

    def rationalize(self) -> str:
        """Return a rationalization to avoid state change."""
        return (
            "Ostajam, kjer sem, ker mi to zagotavlja stabilnost in varnost, "
            "kljub napetostim, ki jih čutim."
        )

    def transition(self) -> str:
        """Attempt a transition but often remain in the same state due to self-deception."""
        if self.tension > 1.0 or self.emotion > 0.8:
            # overwhelming tension or emotion forces a genuine transition
            return super().transition()
        if self.tension > 0.7 or self.emotion > 0.5:
            # rationalize staying in the current state
            self.history.append(self.state)
            return self.state
        return super().transition()
