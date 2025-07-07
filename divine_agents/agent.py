class Agent:
    """Represent an ontological agent capable of transitioning states."""

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


class HiddenAgent(Agent):
    """Agent that tracks hidden emotional history influencing tension."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.hidden_factors = {"past_emotions": [], "hidden_tension": 0.0}

    def update_hidden_factors(self) -> None:
        """Update hidden factors based on emotional history."""
        self.hidden_factors["past_emotions"].append(self.emotion)
        if len(self.hidden_factors["past_emotions"]) > 5:
            self.hidden_factors["past_emotions"].pop(0)
        avg = sum(self.hidden_factors["past_emotions"]) / len(self.hidden_factors["past_emotions"])
        self.hidden_factors["hidden_tension"] = avg
        # hidden tension subtly increases visible tension
        self.tension += avg / 10


class SimultaneousAgent(Agent):
    """Agent capable of exploring past states while transitioning."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.past_states = []

    def explore_multiple_dimensions(self) -> None:
        """Explore the last state and adjust before transitioning."""
        if self.past_states:
            last = self.past_states[-1]
            self.state = f"Exploring state: {last}"
            super().transition()

    def transition(self) -> str:
        self.past_states.append(self.state)
        self.explore_multiple_dimensions()
        return super().transition()


class FuturePredictingAgent(Agent):
    """Agent that predicts future state based on past transitions."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.past_transitions = []

    def transition(self) -> str:
        self.past_transitions.append(self.state)
        next_state = super().transition()
        self.predict_future()
        return next_state

    def predict_future(self) -> None:
        if self.past_transitions:
            predicted = self.past_transitions[-1]
            self.state = f"Predicting future state: {predicted}"
