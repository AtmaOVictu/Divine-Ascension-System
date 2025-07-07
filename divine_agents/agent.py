class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent tracks emotional intensity, tension and experience points (XP).
    XP can be increased via rewards or task completion and can be used for
    potential upgrades of the agent. State transitions occur when emotion or
    tension thresholds are exceeded.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, xp: int = 0):
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

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def reward(self, result: bool) -> None:
        """Adjust emotion and XP based on success or failure."""
        if result:
            self.emotion += 0.1
            self.xp += 10
        else:
            self.emotion -= 0.1
            self.xp -= 5
        self.history.append(("reward", self.state, self.tension, self.emotion))

    def complete_task(self, task: str) -> None:
        """Grant XP for completing a specific task."""
        if task == "philosophical_question":
            self.xp += 15
        elif task == "transition":
            self.xp += 20
        self.history.append(("task_completed", task, self.xp))

    def level_up(self) -> bool:
        """Upgrade the agent when enough XP is collected."""
        if self.xp >= 100:
            self.xp = 0
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self.history.append(("level_up", self.state))
            return True
        return False

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
