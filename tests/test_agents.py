import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, dynamic_philosophical_dialogue


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

    def test_emotion_trigger(self):
        agent = Agent("B1")
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Jaz")

    def test_dynamic_dialogue(self):
        a1 = Agent("X1")
        a2 = Agent("X2", state="Jaz")
        lines = dynamic_philosophical_dialogue(a1, a2)
        # Final lines should reflect unified truth from both agents
        self.assertIn("Enotnost", lines[-2])
        self.assertIn("Enotnost", lines[-1])


if __name__ == '__main__':
    unittest.main()
