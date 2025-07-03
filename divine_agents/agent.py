class Agent:
    """Ontological agent capable of state transitions based on emotions and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotions = {}
        self.history = [state]

    def update_emotion(self, name: str, value: float) -> None:
        """Update a named emotion and adjust tension accordingly."""
        self.emotions[name] = value
        self.emotion = max(self.emotions.values())
        self.tension += value

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
        """Return a philosophical answer depending on the current state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane."
        }[self.state]

        if self.emotions.get("fear", 0) > 0.5:
            return base + " Občutim strah."
        if self.emotions.get("joy", 0) > 0.5:
            return base + " Preveva me veselje."
        if self.emotions.get("anger", 0) > 0.5:
            return base + " Čutim jezo."
        return base
