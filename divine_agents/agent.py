class Agent:
    """Ontological agent capable of emotional transitions and self reflection."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

        # Belief system and emotional map used when resolving contradictions
        self.beliefs = {"I am alive": 1.0, "The world is round": 1.0}
        self.emotions = {"anger": 0.0, "doubt": 0.0}
        self.self_reflection = False

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    # ------------------------------------------------------------------
    # Advanced functionality for contradictions and self awareness
    # ------------------------------------------------------------------

    def update_emotions(self, emotion: str, intensity_change: float) -> None:
        """Update a named emotion and adjust tension."""
        if emotion in self.emotions:
            self.emotions[emotion] = min(max(self.emotions[emotion] + intensity_change, 0.0), 1.0)
            self.tension += intensity_change
            self.emotion = max(self.emotions.values())

    def interact(self, interaction: str) -> str:
        """Process an interaction and resolve any detected contradictions."""
        contradictions = self.detect_contradictions(interaction)
        if contradictions:
            return self.resolve_contradictions(contradictions)
        return "No contradictions detected."

    def detect_contradictions(self, interaction: str):
        """Detect contradictions in a provided text."""
        contradictions = []
        if "I am not alive" in interaction and "I am alive" in self.beliefs:
            contradictions.append(("I am alive", "I am not alive"))
        if "The world is flat" in interaction and "The world is round" in self.beliefs:
            contradictions.append(("The world is round", "The world is flat"))
        return contradictions

    def resolve_contradictions(self, contradictions):
        """Resolve contradictions by considering the current emotional state."""
        self.self_reflection = True
        resolved = []
        for belief_a, belief_b in contradictions:
            if self.emotions.get("anger", 0.0) > 0.5:
                resolved.append(belief_a)
            else:
                resolved.append(self.reconcile_beliefs(belief_a, belief_b))
        self.beliefs["truth"] = "; ".join(resolved)
        return f"{self.name} has reconciled beliefs: {resolved}"

    def reconcile_beliefs(self, belief_a: str, belief_b: str) -> str:
        """Create a hybrid truth between two opposing beliefs."""
        return f"{belief_a} and {belief_b} coexist in different contexts."

    def reflect_on_beliefs(self) -> str:
        """Produce a self-reflective statement after contradiction handling."""
        if self.self_reflection:
            self.self_reflection = False
            return f"{self.name} reflects: 'I see my beliefs are fluid and must adapt over time.'"
        return ""

    def get_current_state(self):
        """Return current beliefs and emotions."""
        return self.beliefs, self.emotions
