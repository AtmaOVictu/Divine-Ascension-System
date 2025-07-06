class Agent:
    """Ontological agent capable of state transitions and emotional responses."""

    STATES = ("Ego", "Jaz", "Enotnost")
    MOODS = ("neutral", "fear", "joy", "anger")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion: float = 0.0, mood: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.mood = mood
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_mood(self, mood: str) -> None:
        """Set mood and adjust tension based on emotional flavour."""
        if mood not in self.MOODS:
            raise ValueError(f"Unknown mood: {mood}")
        self.mood = mood
        if mood in ("fear", "anger"):
            self.tension += 0.3
        elif mood == "joy":
            self.tension = max(self.tension - 0.2, 0.0)

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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        mood_note = {
            "fear": " Čutim strah ob teh mislih.",
            "joy": " Preveva me veselje.",
            "anger": " Občutim jezo.",
        }.get(self.mood, "")

        return f"{base}{mood_note}"
