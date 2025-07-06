class Agent:
    """Ontological agent capable of transitioning states based on emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0,
                 emotion: float = 0.0, emotion_kind: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_kind = emotion_kind
        self.history = [state]

    def update_emotion(self, kind: str, intensity: float) -> None:
        """Update emotion type and intensity, adjusting tension accordingly."""
        self.emotion_kind = kind
        self.emotion = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        emotion_note = {
            "fear": " Čutim strah.",
            "joy": " Preveva me veselje.",
            "anger": " Občutim jezo."
        }.get(self.emotion_kind, "")
        return base + emotion_note
