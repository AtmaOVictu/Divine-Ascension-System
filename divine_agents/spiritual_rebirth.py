"""Dynamic agent system with emotional and philosophical state transitions."""

from typing import List


class SpiritualAgent:
    """Agent that transitions between ontological states based on emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    color_map = {
        "fear": "purple",
        "joy": "yellow",
        "anger": "red",
        "calm": "blue",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_level: float = 0.0, emotion: str = "calm") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion = emotion
        self.knowledge_pool: List[str] = []
        self.history: List[str] = [state]

    def update_emotion(self, emotion: str, level: float) -> None:
        """Update emotion and adjust tension."""
        self.emotion = emotion
        self.emotion_level = level
        self.tension += level

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition to the next ontological state if thresholds are met."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
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

    def gather_knowledge(self, knowledge: str) -> None:
        """Add knowledge influenced by the current emotion."""
        tagged = f"{self.emotion.upper()} knowledge: {knowledge}"
        self.knowledge_pool.append(tagged)


def philosophical_debate(agent1: SpiritualAgent, agent2: SpiritualAgent) -> List[str]:
    """Simulate a short dialogue and trigger state transitions."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # agents react emotionally to the debate
    agent1.update_emotion("fear", 0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion("joy", 0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
