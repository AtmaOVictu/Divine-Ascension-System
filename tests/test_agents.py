import unittest
from divine_agents.agent import Agent, SelfDeceptionAgent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_self_deception_blocks_transition(self):
        agent = SelfDeceptionAgent("B", tension=0.8)
        state = agent.transition()
        self.assertEqual(state, "Ego")
        self.assertTrue(agent.rationalizations)

    def test_self_deception_breaks_at_high_tension(self):
        agent = SelfDeceptionAgent("B", tension=0.95)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_dialogue_with_self_deception(self):
        a1 = SelfDeceptionAgent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("racionalizira" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
