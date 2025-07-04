class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent maintains an ontological ``state`` (``Ego``, ``Jaz`` or ``Enotnost``)
    and transitions between them when its ``tension`` or ``emotion`` exceeds the
    required thresholds. ``emotion`` contributes to ``tension`` and also colours
    the responses returned by :meth:`respond`.
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
        # emotion naturally increases tension
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
        """Return a philosophical answer depending on the current state.

        Emotional intensity colours the reply. When ``emotion`` is high the
        response is prefixed with *"Čustveno"*, otherwise it is more calm.
        """
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        prefix = "Čustveno povem: " if self.emotion > 0.5 else "Mirno razmišljam: "
        return f"{prefix}{base}"
