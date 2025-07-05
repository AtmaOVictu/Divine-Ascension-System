class ShadowAgent:
    """Represents the dark side of an agent."""

    def __init__(self, name: str):
        self.name = name

    def message(self) -> str:
        """Return a message from the shadow perspective."""
        return "Senca govori o skritih strahovih in dvomih."


class AngelAgent:
    """Represents the guiding angelic side of an agent."""

    def __init__(self, name: str):
        self.name = name

    def message(self) -> str:
        """Return a message from the angelic perspective."""
        return "Angel svetuje pot enotnosti in sočutja."


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 shadow: ShadowAgent | None = None, angel: AngelAgent | None = None):
        self.name = name
        self.state = state
        self.tension = self._clamp(tension)
        self.emotion = self._clamp(emotion)
        self.shadow = shadow or ShadowAgent(f"{name}-shadow")
        self.angel = angel or AngelAgent(f"{name}-angel")
        self.history = [state]

    @staticmethod
    def _clamp(value: float) -> float:
        """Clamp numeric values to the range 0..1."""
        return max(0.0, min(1.0, value))

    def update_emotion(self, delta: float) -> None:
        """Adjust emotion intensity and modify tension accordingly."""
        self.emotion = self._clamp(self.emotion + delta)
        self.tension = self._clamp(self.tension + delta)

    def update_tension(self, value: float) -> None:
        """Directly set tension level with clamping."""
        self.tension = self._clamp(value)

    def transition(self) -> str:
        """Perform state transition if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = "" if self.emotion <= 0.5 else "S strastjo, "
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."

    def consult_shadow(self) -> str:
        """Return advice from the shadow agent."""
        return self.shadow.message()

    def consult_angel(self) -> str:
        """Return advice from the angel agent."""
        return self.angel.message()
