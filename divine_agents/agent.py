class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    TENSION_THRESHOLD = 0.7
    EMOTION_THRESHOLD = 0.5

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        # Track individual emotions influencing the agent
        self.emotions = {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.history = [state]

    @property
    def emotion(self) -> float:
        """Return the highest emotional intensity."""
        return max(self.emotions.values())

    def update_emotion(self, name: str, value: float) -> None:
        """Update a specific emotion and increase tension accordingly."""
        self.emotions[name] = value
        self.tension = min(1.0, self.tension + value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > self.TENSION_THRESHOLD or self.emotion > self.EMOTION_THRESHOLD:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and emotions."""
        emotion_note = ""
        if self.emotions.get("anger", 0) > 0.5:
            emotion_note = " Jezim se."
        elif self.emotions.get("fear", 0) > 0.5:
            emotion_note = " Čutim strah."
        elif self.emotions.get("joy", 0) > 0.5:
            emotion_note = " Preveva me radost."

        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih." + emotion_note
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi." + emotion_note
        return "Vse resnice so eno, medsebojno povezane." + emotion_note
