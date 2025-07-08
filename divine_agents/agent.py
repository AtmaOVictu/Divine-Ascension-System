class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent can optionally make commitments which influence how its
    emotional updates affect tension and therefore state transitions.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label: str | None = None
        self.history = [state]
        self.commitment: str | None = None

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            Numeric representation of the emotional intensity.
        label:
            Optional name of the emotion (e.g. ``"anger"``) which is used when
            evaluating the agent's commitment.
        """
        self.emotion = value
        if label is not None:
            self.emotion_label = label
        self.tension += value
        self.evaluate_commitment()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.evaluate_commitment()

    def make_commitment(self, commitment: str) -> None:
        """Declare a commitment influencing future behaviour."""
        self.commitment = commitment
        self.history.append(f"commit:{commitment}")

    def evaluate_commitment(self) -> None:
        """Modify tension based on current commitment and emotion label."""
        if self.commitment == "self-preservation" and self.emotion_label == "anger":
            # escalate tension when anger threatens self-preservation
            self.tension = max(self.tension, 0.8)
        elif self.commitment == "self-awareness" and self.emotion_label == "reflection":
            # encourage reflective transition
            self.tension = max(self.tension, 0.6)

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
        prefix = ""
        if self.emotion_label:
            prefix = f"({self.emotion_label}) "
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
