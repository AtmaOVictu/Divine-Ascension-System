class Agent:
    """Represents an ontological agent capable of transitioning states and solving problems."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.desire = None
        self.history = [state]
        self.events = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def recognize_problem(self, problem: str) -> None:
        """Set an internal desire/problem the agent wants to solve."""
        self.desire = problem
        self.events.append(f"Recognized problem: {problem}")

    def solve_problem(self) -> str:
        """Attempt to solve the current problem and possibly transition state."""
        if not self.desire:
            return self.state
        # Emotions rise while searching for a solution
        self.update_emotion(0.6)
        new_state = self.transition()
        if new_state == "Enotnost":
            self.events.append(f"Resolved problem: {self.desire}")
            self.desire = None
        else:
            self.events.append(f"Working on problem: {self.desire} -> {new_state}")
        return new_state

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
