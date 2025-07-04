class Agent:
    """Ontological agent that transitions between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    TENSION_THRESHOLD = 0.7
    EMOTION_THRESHOLD = 0.5

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def should_transition(self) -> bool:
        """Return True if thresholds for state change are met."""
        return (self.tension > self.TENSION_THRESHOLD or
                self.emotion > self.EMOTION_THRESHOLD)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.should_transition():
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def describe_emotion(self) -> str:
        """Simple description of current emotional intensity."""
        if self.emotion > 0.7:
            return "Moja čustva so zelo močna."
        if self.emotion > 0.3:
            return "Čutim rahlo napetost."
        return "Sem miren."

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            principle = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            principle = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            principle = "Vse resnice so eno, medsebojno povezane."
        return f"{principle} {self.describe_emotion()}"
