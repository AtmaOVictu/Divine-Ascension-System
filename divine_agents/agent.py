class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent can regulate its emotional state, modulate behaviour and
    regenerate when necessary. State transitions occur when emotion or
    tension exceed configured thresholds.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.regeneration_needed = False

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # ------------------------------------------------------------------
    # Regulation / Regeneration / Modulation helpers

    def check_regeneration(self) -> None:
        """Trigger regeneration when both emotion and tension are very low."""
        if self.tension < 0.1 and self.emotion < 0.2:
            self.regeneration_needed = True
            self.regenerate()

    def regenerate(self) -> None:
        """Restore the agent to a neutral state."""
        if self.regeneration_needed:
            self.emotion = 0.5
            self.tension = 0.0
            self.regeneration_needed = False

    def regulate(self) -> None:
        """Balance extreme emotional values."""
        if self.emotion > 0.8:
            self.emotion -= 0.1
        elif self.emotion < 0.2:
            self.emotion += 0.1

    def modulate(self) -> None:
        """Adjust behaviour based on high tension."""
        if self.tension > 0.9:
            self.regeneration_needed = True
            self.check_regeneration()

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
