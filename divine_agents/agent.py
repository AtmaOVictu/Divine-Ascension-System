from typing import Dict, List, Tuple, Optional


class Agent:
    """Represents an ontological agent capable of transitioning states and
    resolving contradictory beliefs."""

    STATES = ("Ego", "Jaz", "Enotnost")

    # Map of positive beliefs to their negated counterparts
    CONTRADICTIONS: Dict[str, str] = {
        "I am alive": "I am not alive",
        "The world is round": "The world is flat",
    }

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history: List[str] = [state]
        self.beliefs: Dict[str, float] = {
            "I am alive": 1.0,
            "The world is round": 1.0,
        }
        self.emotions: Dict[str, float] = {"anger": 0.0, "fear": 0.0, "joy": 0.0}
        self.self_reflection = False

    def update_emotion(self, value: float, emotion_type: str = "anger") -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        if emotion_type in self.emotions:
            self.emotions[emotion_type] = min(max(value, 0.0), 1.0)

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

    # ------------------------------------------------------------------
    # Self-awareness and contradiction management
    # ------------------------------------------------------------------

    def detect_contradictions(self, text: str) -> List[Tuple[str, str]]:
        """Detect contradictions in the provided text based on current beliefs."""
        found: List[Tuple[str, str]] = []
        for belief, negation in self.CONTRADICTIONS.items():
            if belief in self.beliefs and negation in text:
                found.append((belief, negation))
        return found

    def reconcile_beliefs(self, belief_a: str, belief_b: str) -> str:
        """Create a hybrid truth between opposing beliefs."""
        return f"{belief_a} and {belief_b} coexist in different contexts."

    def resolve_contradictions(self, contradictions: List[Tuple[str, str]]) -> List[str]:
        """Resolve all detected contradictions taking emotions into account."""
        self.self_reflection = True
        results = []
        for a, b in contradictions:
            if self.emotions.get("anger", 0.0) > 0.5:
                results.append(a)
            else:
                results.append(self.reconcile_beliefs(a, b))
        for belief in results:
            self.beliefs["truth"] = belief
        return results

    def interact(self, other_agent: Optional["Agent"], text: str) -> List[str]:
        """Interact with a statement and handle any contradictions."""
        contradictions = self.detect_contradictions(text)
        if contradictions:
            return self.resolve_contradictions(contradictions)
        return [self.respond(text)]

    def reflect_on_beliefs(self) -> str:
        """Produce a reflective statement if self-reflection was triggered."""
        if self.self_reflection:
            self.self_reflection = False
            return (
                f"{self.name} reflects: 'I see my beliefs are fluid and must "
                "adapt over time.'"
            )
        return ""

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
