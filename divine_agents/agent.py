class Agent:
    """Ontological agent capable of transitioning states and expressing emotion."""

    STATES = ("Ego", "Jaz", "Enotnost")
    PRINCIPLES = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set emotion intensity and adjust tension accordingly."""
        self.emotion = max(0.0, min(1.0, value))
        self.tension = min(1.0, self.tension + self.emotion)

    def adjust_emotion(self, delta: float) -> None:
        """Modify emotion and tension incrementally."""
        self.emotion = max(0.0, min(1.0, self.emotion + delta))
        self.tension = max(0.0, min(1.0, self.tension + delta))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))

    def influence(self, other: "Agent") -> None:
        """Slightly adopt another agent's emotional state."""
        self.adjust_emotion(0.1 * other.emotion)
        self.tension = min(1.0, self.tension + 0.1 * other.tension)

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
        """Return a philosophical answer influenced by the current emotion."""
        base = self.PRINCIPLES.get(self.state, "")
        if self.emotion > 0.7:
            tone = "Z veliko čustvenostjo povem: "
        elif self.emotion > 0.3:
            tone = "Čustveno opažam: "
        else:
            tone = "Mirno odgovarjam: "
        return tone + base
