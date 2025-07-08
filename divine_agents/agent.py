class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    CONTRARY_BELIEFS = [
        ("Truth is absolute", "Truth is relative"),
        ("Truth is relative", "Truth is unified"),
    ]

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.beliefs = {}
        self.contradictions = []
        self.interactions = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # Belief handling -----------------------------------------------------

    def add_belief(self, statement: str, value: bool = True) -> None:
        """Store a belief statement."""
        self.beliefs[statement] = value

    def detect_contradictions(self):
        """Check stored beliefs for logical contradictions."""
        detected = []
        for a, b in self.CONTRARY_BELIEFS:
            if self.beliefs.get(a) and self.beliefs.get(b):
                detected.append((a, b))
        self.contradictions.extend(detected)
        return detected

    def resolve_contradictions(self):
        """Resolve contradictions by adjusting emotion and tension."""
        contradictions = self.detect_contradictions()
        if contradictions:
            self.tension += 0.3 * len(contradictions)
            self.emotion += 0.2 * len(contradictions)
        return contradictions

    def reflect(self) -> str:
        """Review interactions and update worldview."""
        self.interactions.append(f"Reflection: {len(self.contradictions)} contradictions")
        self.resolve_contradictions()
        return self.transition()

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
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
