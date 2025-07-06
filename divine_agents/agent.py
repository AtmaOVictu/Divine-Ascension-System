class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_name: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.past_tension = []
        self.history = [state]

    def update_emotion(self, value: float, name: str = "") -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if name:
            self.emotion_name = name
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level and record history."""
        self.past_tension.append(self.tension)
        self.tension = value
        if len(self.past_tension) > 5:
            self.past_tension.pop(0)

    def interact(self, other: "Agent") -> None:
        """Influence another agent's tension based on this agent's emotion."""
        if self.emotion_name == "anger":
            other.tension += 0.1
        elif self.emotion_name == "calm":
            other.tension -= 0.1

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def move(self) -> str:
        """Determine movement characteristics based on emotion."""
        if self.emotion_name == "anger":
            speed = 2 * self.emotion
            direction = (1, 0)
        elif self.emotion_name == "joy":
            speed = 1 * self.emotion
            direction = (-1, 0)
        else:
            speed = 0.5 * self.emotion
            direction = (0, 0)
        return f"{self.name} se premika s hitrostjo {speed} v smeri {direction}"

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = ""
        if self.emotion_name:
            prefix = f"({self.emotion_name}) "
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
