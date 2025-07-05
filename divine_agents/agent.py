from .ontology import OntoState, should_transition, truth_statement


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = (OntoState.Ego.name, OntoState.Jaz.name, OntoState.Enotnost.name)

    def __init__(self, name: str, state: str = OntoState.Ego.name, tension: float = 0.0, emotion: float = 0.0):
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
        if should_transition(self.tension, self.emotion):
            if self.state == OntoState.Ego.name:
                self.state = OntoState.Jaz.name
            elif self.state == OntoState.Jaz.name:
                self.state = OntoState.Enotnost.name
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        return truth_statement(OntoState[self.state])
