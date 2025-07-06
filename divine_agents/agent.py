class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.problem: str | None = None
        self.dialogue_history: list[tuple[str, str]] = []

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

    # -------------------------- Extended Functionality --------------------------
    def perceive_problem(self, problem: str) -> None:
        """Store a problem the agent wants to solve."""
        self.problem = problem
        self.history.append(f"Problem: {problem}")

    def solve_problem(self) -> str:
        """Attempt to solve a problem, updating emotion and transitioning."""
        if self.problem:
            # Increase emotion which indirectly raises tension
            self.update_emotion(0.6)
            state = self.transition()
            self.history.append(f"Solving: {self.problem}")
            if state == "Enotnost":
                self.problem = None
            return state
        return self.state

    def speak(self, question: str) -> str:
        """Answer a question and remember the exchange."""
        answer = self.respond(question)
        self.dialogue_history.append((question, answer))
        return answer
