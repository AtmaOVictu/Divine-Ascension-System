class Agent:
    """Represent an ontological agent with desire-driven state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.problem = None
        self.desire = None
        self.log = []

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

    # New functionality reflecting problem/desire mechanics
    def recognize_problem(self, problem: str) -> None:
        """Store a problem the agent wants to solve."""
        self.problem = problem
        self.desire = problem
        self.log.append(f"Recognized problem: {problem}")

    def yearn_for_solution(self) -> None:
        """Increase emotion and tension when desiring a solution."""
        if self.desire:
            # yearning raises emotion slightly which in turn increases tension
            self.update_emotion(min(1.0, self.emotion + 0.1))
            self.log.append(f"Yearning for solution: {self.desire}")
        else:
            self.log.append("No problem to yearn for.")

    def solve_problem(self) -> None:
        """Attempt to solve the recognized problem via state transitions."""
        if not self.desire:
            self.log.append("Nothing to solve.")
            return
        self.log.append(f"Attempting to solve: {self.desire}")
        prev_state = self.state
        self.transition()
        if self.state == "Enotnost" and prev_state != "Enotnost":
            self.log.append("Problem resolved in Enotnost.")
            self.problem = None
            self.desire = None

    def dialogue(self, other: "Agent") -> list:
        """Dialogue about truth, reflecting states and emotions."""
        conversation = []
        conversation.append(
            f"{self.name} ({self.state}): {self.respond('Kaj je resnica?')}"
        )
        conversation.append(
            f"{other.name} ({other.state}): {other.respond('Kaj je resnica?')}"
        )

        # Both agents yearn for solutions which may increase tension/emotion
        self.yearn_for_solution()
        other.yearn_for_solution()
        self.solve_problem()
        other.solve_problem()

        conversation.append(f"{self.name} stanje: {self.state}")
        conversation.append(f"{other.name} stanje: {other.state}")
        return conversation

    def history_log(self) -> list:
        """Return internal event log for testing or inspection."""
        return self.log
