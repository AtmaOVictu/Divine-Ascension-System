import unittest
from divine_agents.advanced_agents import (
    AgentWithNumber3,
    AgentWithNumber7,
    PhilosopherAgent,
    HeroAgent,
    agent_dialogue,
)


class TestAdvancedAgents(unittest.TestCase):
    def test_numbered_agent_transition(self):
        agent = AgentWithNumber3("A")
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Jaz")

    def test_dialogue_interaction(self):
        a1 = PhilosopherAgent("P")
        a2 = HeroAgent("H")
        lines = agent_dialogue(a1, a2)
        # Expect agents to have transitioned due to emotion updates
        self.assertIn("Jaz", a1.state)
        self.assertIn(a2.state, {"Jaz", "Enotnost"})
        self.assertTrue(any("justice" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
