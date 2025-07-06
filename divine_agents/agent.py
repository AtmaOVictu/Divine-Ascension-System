class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    PRINCIPLES = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion=None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion or {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.history = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update a specific emotion and adjust tension accordingly."""
        if emotion_type not in self.emotion:
            raise ValueError(f"Unknown emotion '{emotion_type}'")
        self.emotion[emotion_type] = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def overall_emotion(self) -> float:
        """Return the highest intensity among all emotions."""
        return max(self.emotion.values())

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.overall_emotion() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotional state."""
        base = self.PRINCIPLES[self.state]
        emotion_comment = ""
        if self.emotion.get("anger", 0) > 0.5:
            emotion_comment = " Čutim jezo."
        elif self.emotion.get("fear", 0) > 0.5:
            emotion_comment = " Čutim strah."
        elif self.emotion.get("joy", 0) > 0.5:
            emotion_comment = " Čutim veselje."
        return f"{base}{emotion_comment}"
