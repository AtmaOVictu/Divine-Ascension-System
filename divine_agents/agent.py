class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Initial ontological state (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension:
        Numeric representation of inner tension.
    emotion:
        Numeric intensity of current emotion.
    emotion_label:
        Optional textual label describing the emotion (e.g. ``"fear"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label or "neutral"
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, label: str, intensity: float) -> None:
        """Set both emotion label and intensity."""
        self.emotion_label = label
        self.update_emotion(intensity)

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

    def communicate(self, other: "Agent") -> list[str]:
        """Engage in a short dialogue with another agent."""
        lines = [
            f"{self.name} ({self.state}, {self.emotion_label}): {self.respond('Kaj je resnica?')}",
            f"{other.name} ({other.state}, {other.emotion_label}): {other.respond('Kaj je resnica?')}",
        ]
        # increase emotional intensity due to debate
        self.update_emotion(min(self.emotion + 0.6, 1.0))
        other.update_emotion(min(other.emotion + 0.6, 1.0))
        if self.transition() != self.history[-2]:
            lines.append(f"{self.name} prehaja v stanje: {self.state}")
        if other.transition() != other.history[-2]:
            lines.append(f"{other.name} prehaja v stanje: {other.state}")
        lines.extend([
            f"{self.name}: {self.respond('Kaj je resnica?')}",
            f"{other.name}: {other.respond('Kaj je resnica?')}",
        ])
        return lines


class MultiLayerTransitionSystem:
    """Handle multi-dimensional transitions for an agent."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def multi_layer_transition(self) -> str:
        """Perform a transition considering emotion label and tension."""
        emotion = self.agent.emotion_label
        tension = self.agent.tension

        if self.agent.state == "Ego" and (tension > 0.7 or emotion == "fear"):
            self.agent.state = "Jaz"
        elif self.agent.state == "Jaz" and (tension > 0.7 or emotion == "anger"):
            self.agent.state = "Enotnost"
        self.agent.history.append(self.agent.state)
        return self.agent.state


