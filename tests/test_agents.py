import unittest
from divine_agents.agent import Agent, WideAgent, NarrowAgent
from divine_agents.dialogue import philosophical_dialogue, ontological_debate


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

    def test_wide_agent_transition(self):
        wa = WideAgent("W1")
        wa.update_emotion(0.9)
        self.assertEqual(wa.state, "Jaz")

    def test_narrow_agent_threshold(self):
        na = NarrowAgent("N1", threshold=0.4)
        na.update_value(0.8)
        self.assertEqual(na.state, "Jaz")

    def test_ontological_debate(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = ontological_debate(a1, a2)
        self.assertEqual(len(lines), 6)


if __name__ == '__main__':
    unittest.main()
