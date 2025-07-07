import uuid


class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent keeps track of its emotional intensity, tension level and
    history of states. A unique identifier allows the agent to be copied or
    referenced later in simulations.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.id = self.generate_id()

    def generate_id(self) -> str:
        """Return a unique identifier for this agent."""
        return f"{self.name}_{uuid.uuid4().hex}"

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def describe_emotion(self) -> str:
        """Return a textual description of the current emotional intensity."""
        if self.emotion > 0.7:
            return "zelo intenzivno"
        if self.emotion > 0.5:
            return "intenzivno"
        if self.emotion > 0.2:
            return "blago"
        return "mirno"

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
        emotion_note = self.describe_emotion()

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{base} (čustvo: {emotion_note})"

    def replay_history(self) -> str:
        """Return the recorded history of states and events."""
        return "\n".join(self.history)

    def copy_state(self) -> "Agent":
        """Create a shallow copy of the agent preserving current values."""
        return Agent(self.name, self.state, self.tension, self.emotion)

    def mark_with_tattoo(self, tattoo: str) -> None:
        """Record a significant event in the agent's history."""
        self.history.append(f"Tattoo applied: {tattoo}")
