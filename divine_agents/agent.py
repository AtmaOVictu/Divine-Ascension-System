from typing import List, Dict


class AgentHistory:
    """Utility class for tracking state transitions of an agent."""

    def __init__(self, initial_state: str) -> None:
        self.transitions: List[Dict[str, str]] = []
        self.current_state = initial_state

    def record_transition(self, state_from: str, state_to: str) -> None:
        self.transitions.append({"from": state_from, "to": state_to})
        self.current_state = state_to

    def states(self) -> List[str]:
        states = [self.transitions[0]["from"]] if self.transitions else [self.current_state]
        states.extend(t["to"] for t in self.transitions)
        return states


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = AgentHistory(state)

    def update_emotion(self, value: float, emotion_type: str = "neutral") -> None:
        """Update emotion intensity, set emotion type, and adjust tension."""
        self.emotion = value
        self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        previous_state = self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.record_transition(previous_state, self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        mood = ""
        if self.emotion_type == "fear":
            mood = " Čutim strah."
        elif self.emotion_type == "joy":
            mood = " Občutim veselje."
        elif self.emotion_type == "anger":
            mood = " Občutim jezo."

        return f"{base}{mood}"
