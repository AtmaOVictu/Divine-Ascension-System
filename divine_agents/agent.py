import random


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # New methods implementing 'happy coincidences'
    def interact_with(self, other_agent: "Agent") -> str:
        """Interact with another agent and process a happy coincidence."""
        feedback = self.create_happy_coincidence()
        self.receive_feedback(feedback)
        return feedback

    def create_happy_coincidence(self) -> str:
        """Generate a random feedback event representing a coincidence."""
        return random.choice([
            "positive",
            "neutral",
            "conflict",
            "surprise",
            "happy",
        ])

    def receive_feedback(self, feedback: str) -> None:
        """Update emotion based on feedback and attempt state transition."""
        adjustments = {
            "positive": 0.6,
            "neutral": 0.2,
            "conflict": 0.8,
            "surprise": 0.5,
            "happy": 0.9,
        }
        self.update_emotion(adjustments.get(feedback, 0.0))
        self.transition()

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
