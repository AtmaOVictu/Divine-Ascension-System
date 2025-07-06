class Agent:
    """Ontological agent that transitions between philosophical states.

    The agent tracks emotion and tension levels which trigger state changes
    according to the following rules:
    - If ``tension`` > 0.7 **or** ``emotion`` > 0.5 the agent advances
      from ``Ego`` -> ``Jaz`` -> ``Enotnost``.
    The history of visited states is stored in ``history``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        # Keep a log of all visited states for later inspection
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion level and increase tension accordingly."""
        self.emotion = value
        # Emotions contribute to the overall tension of the agent
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

    def emotion_label(self) -> str:
        """Return a textual label describing the current emotional intensity."""
        if self.emotion > 0.7:
            return "jezen"
        if self.emotion > 0.3:
            return "miren"
        return "ravnodušen"

    def respond(self, question: str) -> str:
        """Return a philosophical answer including the emotional tone."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        tone = self.emotion_label().capitalize()
        return f"{tone}: {base}"
