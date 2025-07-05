class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost", "Tezava", "Humor")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0,
                 emotion_level: float = 0.0, emotion_label: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, label: str, value: float) -> None:
        """Update emotion type and intensity then adjust tension."""
        self.emotion_label = label
        self.emotion_level = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition based on tension and emotion."""
        if self.emotion_label in {"frustration", "confusion"} and self.emotion_level > 0.5:
            self.state = "Tezava"
        elif self.emotion_label == "humor" and self.emotion_level > 0.5 and self.tension <= 0.7:
            self.state = "Humor"
        elif self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
            "Tezava": "Soočamo se s težavo, ki zahteva refleksijo.",
            "Humor": "Včasih je smeh najboljše zdravilo."}[
                self.state
            ]
        if self.emotion_label:
            return f"({self.emotion_label}) {base}"
        return base

    def get_state(self) -> str:
        """Return current state."""
        return self.state

    def get_history(self) -> list[str]:
        """Return history of states."""
        return self.history
