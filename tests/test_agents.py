import unittest
from divine_agents import Agent, philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_tension_triggers_transition(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_triggers_transition(self):
        agent = Agent("B")
        agent.update_emotion("fear", 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion("joy", 0.2)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("joy", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertEqual(a1.state, "Jaz")
        self.assertTrue(any("absolutna" in l or "relativna" in l for l in lines))


if __name__ == '__main__':
    unittest.main()
