import asyncio
import unittest

from divine_agents.agent import Agent
from divine_agents.async_dialogue import asynchronous_dialogue

class TestAsyncDialogue(unittest.TestCase):
    def test_async_dialogue_transitions(self):
        agent1 = Agent("A1")
        agent2 = Agent("A2")
        lines = asyncio.run(asynchronous_dialogue(agent1, agent2, rounds=2, delay=0))
        assert len(lines) > 0
        # ensure that at least one agent has progressed from Ego state
        assert agent1.state != "Ego" or agent2.state != "Ego"

if __name__ == "__main__":
    unittest.main()
