class Agent:
    """Represents an ontological agent capable of transitioning states.

    An agent maintains internal metrics such as ``tension`` and ``emotion``
    which can be influenced by contextual factors like loyalty or previous
    decisions.  State transitions occur when personalised thresholds are
    exceeded.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        loyalty: float = 0.5,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.loyalty = loyalty
        self.history = [state]
        self.decision_history = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_loyalty(self, value: float) -> None:
        """Update loyalty level within the ``0-1`` range."""
        self.loyalty = max(0.0, min(1.0, value))

    def add_decision(self, decision: str) -> None:
        """Record a decision or interaction."""
        self.decision_history.append(decision)

    def apply_context(self, context: str) -> None:
        """Modify tension and emotion based on contextual information."""
        if context == "moral_dilemma":
            self.tension += 0.2
        elif context == "betrayal":
            self.tension += 0.3
            self.emotion += 0.2
        elif context == "support":
            self.tension = max(0.0, self.tension - 0.1)
            self.emotion = max(0.0, self.emotion - 0.1)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        tension_threshold = 0.7 - self.loyalty * 0.1
        emotion_threshold = 0.5 - self.loyalty * 0.05
        if self.tension > tension_threshold or self.emotion > emotion_threshold:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state.

        Strong emotions amplify the response tone.
        """
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            return base.upper()
        if self.emotion > 0.3:
            return f"{base} (čutim napetost)"
        return base
