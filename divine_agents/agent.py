class Agent:
    """Ontological agent influenced by emotions and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_level: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion_type = emotion_type
        self.history = [state]

    def set_emotion(self, emotion_type: str, level: float) -> None:
        """Set the agent's emotion and adjust tension accordingly."""
        self.emotion_type = emotion_type
        self.emotion_level = level
        self.tension += level

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition between ontological states based on emotion and tension."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def _emotion_prefix(self) -> str:
        mapping = {
            "fear": "Čutim strah. ",
            "joy": "Čutim veselje. ",
            "anger": "Čutim jezo. ",
        }
        return mapping.get(self.emotion_type, "")

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state."""
        prefix = self._emotion_prefix()
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return prefix + base
