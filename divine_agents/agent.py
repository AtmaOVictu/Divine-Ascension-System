class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("fear", "joy", "anger")
    EMOTION_TRANSLATIONS = {"fear": "strah", "joy": "veselje", "anger": "jeza"}

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        self.tension = 0.0
        self.emotion_level = 0.0
        # Track individual emotion intensities
        self.emotions = {e: 0.0 for e in self.EMOTIONS}
        self.history = [state]

    def update_emotion(self, kind: str, intensity: float) -> None:
        """Update an emotional state and adjust tension accordingly."""
        if kind not in self.EMOTIONS:
            raise ValueError(f"Unknown emotion: {kind}")
        self.emotions[kind] = intensity
        self.emotion_level = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def dominant_emotion(self) -> str:
        """Return the emotion with the highest intensity."""
        return max(self.emotions, key=self.emotions.get)

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and emotion."""
        emotion_key = self.dominant_emotion()
        emotion = self.EMOTION_TRANSLATIONS.get(emotion_key, emotion_key)

        if self.state == "Ego":
            return (
                f"Kljub {emotion}u verjamem, da je resnica absolutna in neodvisna od drugih."
            )
        if self.state == "Jaz":
            return (
                f"Ker čutim {emotion}, verjamem, da je resnica relativna in oblikovana z našimi odnosi."
            )
        return (
            f"Z občutkom {emotion} spoznavam, da so vse resnice eno in medsebojno povezane."
        )
