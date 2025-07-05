class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        # track micro (NANO) events that can lead to a larger MEGA shift
        self.nano_counter = 0
        self.nano_threshold = 3

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def nano_event(self, emotion_change: float = 0.1, tension_change: float = 0.1) -> None:
        """Register a small (NANO) event that may accumulate into a MEGA shift."""
        self.emotion += emotion_change
        self.tension += tension_change + emotion_change
        self.nano_counter += 1
        if self.nano_counter >= self.nano_threshold:
            self.mega_event()

    def mega_event(self) -> None:
        """Trigger a MEGA change by boosting tension and resetting the counter."""
        self.tension = max(self.tension, 1.0)
        self.emotion = max(self.emotion, 0.8)
        self.nano_counter = 0

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
        """Return a philosophical answer depending on the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            mood = " (zelo čustveno)"
        elif self.emotion > 0.3:
            mood = " (čustveno)"
        else:
            mood = ""
        return base + mood
