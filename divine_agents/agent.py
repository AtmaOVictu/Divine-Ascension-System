class Agent:
    """Ontological agent capable of transitioning states based on tension,
    emotion and contextual influences."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.internal_context = None
        self.external_context = None
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def set_contexts(self, internal: str = None, external: str = None) -> None:
        """Assign internal and external contexts to the agent."""
        self.internal_context = internal
        self.external_context = external

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def transition_by_context(self) -> str:
        """Transition according to internal and external contexts."""
        if self.internal_context == "visoka napetost" and self.external_context == "stresno okolje":
            return self.transition()
        if self.internal_context == "mirno" and self.external_context == "podpora":
            # force transition to Enotnost if already in Jaz
            if self.state == "Jaz":
                self.tension = 1.0
                self.emotion = 1.0
            return self.transition()
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return f"\u010cutim intenzivna \u010dustva. {base}"
        return base
