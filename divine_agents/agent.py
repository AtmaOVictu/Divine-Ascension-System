class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent maintains an ontological ``state`` (``Ego`` -> ``Jaz`` ->
    ``Enotnost``) and transitions when ``tension`` or ``emotion`` cross the
    defined thresholds. Additional helper methods provide regeneration,
    regulation and modulation capabilities used in the tests and dialogue
    simulation.
    """

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

    # --- new helper methods for regeneration/regulation/modulation ---
    def regenerate(self) -> None:
        """Reset emotion and tension to a balanced state."""
        self.emotion = 0.5
        self.tension = 0.0

    def regulate(self) -> None:
        """Ensure emotion stays within a moderate range and adjust tension."""
        if self.emotion > 0.8:
            self.emotion = 0.8
        elif self.emotion < 0.2:
            self.emotion = 0.2
        self.tension = max(self.tension, self.emotion)

    def modulate(self) -> None:
        """Fine tune the agent's state based on current tension."""
        if self.tension > 0.9:
            self.regenerate()
        else:
            self.regulate()

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        # ensure the internal state is modulated before transitioning
        self.modulate()
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }
        answer = base.get(self.state, "")
        if self.emotion > 0.7:
            answer += " (govorim s strastjo)"
        elif self.emotion < 0.3:
            answer += " (miren ton)"
        return answer
