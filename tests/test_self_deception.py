import unittest
from divine_agents.self_deception_agent import SelfDeceptionAgent
from divine_agents.agent import Agent
from divine_agents.dialogue import deception_dialogue


class TestSelfDeceptionAgent(unittest.TestCase):
    def test_no_transition_below_high_threshold(self):
        agent = SelfDeceptionAgent("S")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_forced_transition(self):
        agent = SelfDeceptionAgent("S")
        agent.update_tension(1.1)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_rationalization_reduces_tension(self):
        agent = SelfDeceptionAgent("S")
        agent.update_tension(0.8)
        agent.transition()
        self.assertLess(agent.tension, 0.8)

    def test_deception_dialogue(self):
        a1 = SelfDeceptionAgent("S")
        a2 = Agent("A2", state="Jaz")
        lines = deception_dialogue(a1, a2)
        self.assertTrue(any("poskusa ostati" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
