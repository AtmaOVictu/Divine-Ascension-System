class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, xp: int = 0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.xp = xp
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def reward(self, result: bool) -> None:
        """Adjust emotion and XP based on the result."""
        if result:
            self.emotion += 0.1
            self.xp += 10
        else:
            self.emotion -= 0.1
            self.xp = max(0, self.xp - 5)
        self.history.append(("reward", self.state, self.tension, self.emotion, self.xp))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def complete_task(self, task: str) -> None:
        """Grant XP for completing tasks."""
        if task == "philosophical_question":
            self.xp += 15
        elif task == "transition":
            self.xp += 20
        self.history.append(("task_completed", task, self.xp))

    def level_up(self) -> None:
        """Advance the agent when enough XP has been gathered."""
        if self.xp >= 100:
            self.xp = 0
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self.history.append(("level_up", self.state))

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

        if self.emotion > 0.6:
            mood = "z navdušenjem"
        elif self.emotion < -0.6:
            mood = "z zaskrbljenostjo"
        else:
            mood = "mirno"
        return f"{base} ({mood})"
