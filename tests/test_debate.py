import unittest
from divine_agents.agent import Agent
from divine_agents.debate import debate


class TestDebate(unittest.TestCase):
    def test_debate_causes_transition(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        initial_states = (a1.state, a2.state)
        lines = debate(a1, a2, turns=2)
        self.assertNotEqual((a1.state, a2.state), initial_states)
        self.assertTrue(any("prehaja" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
