"""Dynamic agent system with emotion-driven state transitions."""
from typing import List, Dict


class DynamicAgent:
    """Agent capable of transitioning through ontological states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, key: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.key = key
        self.history: List[str] = [state]
        self.activation_map: Dict[str, str] = {
            "truth": "Ego",
            "negation": "Jaz",
            "wisdom": "Enotnost",
        }

    def update_tension(self, value: float) -> None:
        """Increase tension and check for activation."""
        self.tension += value
        self._check_activation()

    def update_emotion(self, value: float) -> None:
        """Increase emotion and check for activation."""
        self.emotion += value
        self._check_activation()

    def set_key(self, key: str) -> None:
        """Set activation key which may trigger an immediate state change."""
        self.key = key
        new_state = self.activation_map.get(key)
        if new_state:
            self.state = new_state
            self.history.append(self.state)

    def _check_activation(self) -> None:
        """Trigger transition when thresholds are met."""
        if self.tension > 0.7 or self.emotion > 0.5:
            self.transition()

    def transition(self) -> None:
        """Move to the next ontological state."""
        if self.state == "Ego":
            self.state = "Jaz"
        elif self.state == "Jaz":
            self.state = "Enotnost"
        self.history.append(self.state)

    def respond(self, question: str) -> str:
        """Provide a philosophical answer influenced by emotion."""
        base: str
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z nasimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        if self.emotion > 0.7:
            mood = " v mocnem custvenem odzivu"
        elif self.emotion > 0.4:
            mood = " custveno"
        else:
            mood = " mirno"
        return f"{base}{mood}"


class MultiAgentSystem:
    """Container for multiple agents engaged in dialogue."""

    def __init__(self) -> None:
        self.agents: List[DynamicAgent] = []

    def add_agent(self, agent: DynamicAgent) -> None:
        self.agents.append(agent)

    def interact(self) -> List[str]:
        lines: List[str] = []
        for agent in self.agents:
            agent.set_key("truth")
            lines.append(f"{agent.name} ({agent.state}): {agent.respond('Kaj je resnica?')}")
            agent.update_emotion(0.6)
            lines.append(f"{agent.name} prehaja v stanje: {agent.state}")
        return lines
