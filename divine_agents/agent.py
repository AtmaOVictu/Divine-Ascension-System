class Agent:
    """Ontological agent capable of transitioning philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name or "calm"
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Increase emotion intensity and adjust tension accordingly."""
        self.emotion += value
        if self.emotion < 0:
            self.emotion = 0
        self.tension += value

    def set_emotion(self, name: str, intensity: float) -> None:
        """Set emotion label and intensity, adjusting tension."""
        self.emotion_name = name
        self.emotion = intensity
        self.tension += intensity

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
        """Return a philosophical answer influenced by state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        if self.emotion > 0.5:
            prefix_map = {
                "fear": "V strahu razmišlja, ",
                "anger": "V jezi odgovori, ",
                "joy": "Z veseljem pove, ",
            }
            prefix = prefix_map.get(self.emotion_name, "")
            return prefix + base
        return base
