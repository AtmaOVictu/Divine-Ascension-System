import random
import math


def biological_transition(t: float, k_bio: float, c_bio: float) -> float:
    """Logistic function controlling biological tension."""
    return 1 / (1 + math.exp(-k_bio * (t - c_bio)))


def social_transition(t: float, k_soc: float, c_soc: float) -> float:
    """Logistic function controlling social interaction."""
    return 1 / (1 + math.exp(-k_soc * (t - c_soc)))


class DynamicAgent:
    """Agent that evolves through biological and social phases."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, id: int, state: str = "Ego", initial_tension: float = 0.0,
                 k_bio: float = 1.0, c_bio: float = 0.5,
                 k_soc: float = 1.5, c_soc: float = 0.6) -> None:
        self.id = id
        self.state = state
        self.state_bio = initial_tension
        self.state_soc = 0.0
        self.k_bio = k_bio
        self.c_bio = c_bio
        self.k_soc = k_soc
        self.c_soc = c_soc
        self.emotion = 0.0
        self.shadow = 0.0
        self.history = [state]

    def update_emotion(self, emotion_value: float, shadow_value: float) -> None:
        """Update emotion and shadow, increasing biological tension."""
        self.emotion = emotion_value
        self.shadow = shadow_value
        self.state_bio += self.emotion + self.shadow

    def evolve(self) -> None:
        """Advance biological and social states and handle transitions."""
        self.state_bio = biological_transition(self.state_bio, self.k_bio, self.c_bio)
        self.state_soc = social_transition(self.state_soc, self.k_soc, self.c_soc)
        self._transition_state()

    def _transition_state(self) -> None:
        """Transition ontological state when thresholds are met."""
        if self.state in ("Ego", "Jaz"):
            if self.state_bio > 0.7 or self.emotion > 0.5:
                if self.state == "Ego":
                    self.state = "Jaz"
                else:
                    self.state = "Enotnost"
                self.history.append(self.state)

    def get_state(self):
        """Return current internal states and ontological phase."""
        return self.state_bio, self.state_soc, self.emotion, self.shadow, self.state

    def respond(self, question: str) -> str:
        """Respond based on ontological state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."


class MultiAgentSystem:
    """Manage a collection of DynamicAgents."""

    def __init__(self, num_agents: int = 5) -> None:
        self.agents = [
            DynamicAgent(
                id=i,
                k_bio=random.uniform(0.5, 1.5),
                c_bio=random.uniform(0.3, 0.7),
                k_soc=random.uniform(1.0, 2.0),
                c_soc=random.uniform(0.5, 0.8),
            )
            for i in range(num_agents)
        ]

    def update_agents_emotion(self, emotions, shadows) -> None:
        for agent, emo, sha in zip(self.agents, emotions, shadows):
            agent.update_emotion(emo, sha)

    def evolve_agents(self) -> None:
        for agent in self.agents:
            agent.evolve()

    def get_agents_state(self):
        return [agent.get_state() for agent in self.agents]
