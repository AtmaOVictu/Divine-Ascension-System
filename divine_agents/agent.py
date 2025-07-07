class Agent:
    """Represents an ontological agent capable of transitioning states.

    Transitions rely on emotion and tension thresholds. By default the
    thresholds span decimal values between ``0`` and ``1``. However a
    transition only occurs once the minimum developer specified levels are
    reached (tension ``> 0.7`` or emotion ``> 0.5``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, thresholds: list | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        # thresholds covering decimal points from 0.1 to 1.0 if none provided
        self.thresholds = thresholds or [i / 10 for i in range(1, 11)]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition when threshold conditions are met."""
        for threshold in sorted(self.thresholds):
            tension_ok = self.tension >= threshold and threshold >= 0.7
            emotion_ok = self.emotion >= threshold and threshold >= 0.5
            if tension_ok or emotion_ok:
                if self.state == "Ego":
                    self.state = "Jaz"
                elif self.state == "Jaz":
                    self.state = "Enotnost"
                break
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
