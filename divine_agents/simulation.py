from typing import List

from .agent import Agent
from .dialogue import philosophical_dialogue


class Simulation:
    """Run multiple rounds of philosophical dialogues between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent, rounds: int = 2):
        self.agent1 = agent1
        self.agent2 = agent2
        self.rounds = rounds

    def run(self) -> List[str]:
        """Execute the simulation and return the transcript."""
        transcript: List[str] = []
        for _ in range(self.rounds):
            transcript.extend(philosophical_dialogue(self.agent1, self.agent2))
        return transcript


def run_simulation() -> None:
    """Simple entry point to demonstrate the simulation."""
    agent1 = Agent("Agent 1")
    agent2 = Agent("Agent 2", state="Jaz")
    sim = Simulation(agent1, agent2)
    for line in sim.run():
        print(line)


if __name__ == "__main__":
    run_simulation()
