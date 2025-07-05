from .i18n import RESPONSES, LANGUAGES


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name : str
        Name of the agent.
    state : str, optional
        Starting ontological state, one of ``Ego``, ``Jaz`` or ``Enotnost``.
    tension : float, optional
        Initial tension level. Values are clamped to the range ``0.01`` .. ``1``.
    emotion : float, optional
        Initial emotion intensity. Values are clamped to the range ``0.01`` .. ``1``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = self._clamp(tension)
        self.emotion = self._clamp(emotion)
        self.history = [state]

    @staticmethod
    def _clamp(value: float, minimum: float = 0.01, maximum: float = 1.0) -> float:
        """Clamp ``value`` to the inclusive ``minimum``/``maximum`` range."""
        if value < minimum:
            return minimum
        if value > maximum:
            return maximum
        return value

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value : float
            New emotion intensity. Clamped between ``0.01`` and ``1``.
        """
        self.emotion = self._clamp(value)
        self.tension = self._clamp(self.tension + value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level.

        Parameters
        ----------
        value : float
            New tension level. Clamped between ``0.01`` and ``1``.
        """
        self.tension = self._clamp(value)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str, language: str = "sl") -> str:
        """Return a philosophical answer depending on the current state.

        Parameters
        ----------
        question : str
            The incoming question (ignored, kept for compatibility).
        language : str, optional
            Two-letter language code, ``"sl"`` or ``"en"``.
        """
        if language not in LANGUAGES:
            raise ValueError("Unsupported language")
        return RESPONSES[self.state][language]
