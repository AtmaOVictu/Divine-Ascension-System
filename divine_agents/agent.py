"""Module providing the Agent class for ontological transitions."""

from .security import (
    validate_agent_data,
    check_stage_transition,
    sanitize_output,
    log_error,
    STATES,
)


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = STATES

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Initialize the agent and validate provided data."""
        validate_agent_data(name, state)
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

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        try:
            if self.tension > 0.7 or self.emotion > 0.5:
                if self.state == "Ego":
                    check_stage_transition(self.state, "Jaz")
                    self.state = "Jaz"
                elif self.state == "Jaz":
                    check_stage_transition(self.state, "Enotnost")
                    self.state = "Enotnost"
            self.history.append(self.state)
            return self.state
        except Exception as exc:
            log_error(f"Transition error for {self.name}: {exc}")
            raise

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            text = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            text = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            text = "Vse resnice so eno, medsebojno povezane."
        return sanitize_output(text)
