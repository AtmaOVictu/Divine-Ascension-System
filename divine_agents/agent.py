from .aspects import ShadowAgent, AngelAgent


class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        shadow: ShadowAgent | None = None,
        angel: AngelAgent | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = self._clamp(tension)
        self.emotion = self._clamp(emotion)
        self.shadow = shadow or ShadowAgent(f"{name} Shadow")
        self.angel = angel or AngelAgent(f"{name} Angel")
        self.history = [state]

    @staticmethod
    def _clamp(value: float) -> float:
        """Clamp a float value to the ``0.0-1.0`` range."""
        return max(0.0, min(1.0, value))

    def update_emotion(self, value: float) -> None:
        """Update emotion and raise tension in a clamped manner."""
        self.emotion = self._clamp(value)
        self.tension = self._clamp(self.tension + value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level with clamping."""
        self.tension = self._clamp(value)

    def consult_shadow(self) -> str:
        """Consult the shadow aspect which increases tension."""
        advice = self.shadow.advise()
        self.update_tension(self.tension + 0.2)
        return advice

    def consult_angel(self) -> str:
        """Consult the angelic aspect which soothes emotion."""
        advice = self.angel.advise()
        self.update_emotion(self.emotion + 0.2)
        return advice

    def transition(self) -> str:
        """Perform state transition if tension or emotion exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
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

        if self.emotion > 0.7:
            return base + " Obcutim mocna custva."  # emotional emphasis
        return base
