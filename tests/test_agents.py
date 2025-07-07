import unittest
from divine_agents.agent import Agent
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

    def test_shadow_influence(self):
        agent = Agent("S", shadows={"fear": 0.6})
        agent.update_emotion(0.0)
        agent.transition()
        self.assertGreaterEqual(agent.emotion, 0.6)

    def test_emotional_connection(self):
        a1 = Agent("A1", emotion=0.8)
        a2 = Agent("A2", emotion=0.0)
        a1.connect(a2)
        a1.transition()
        self.assertNotEqual(a2.emotion, 0.0)


if __name__ == '__main__':
    unittest.main()
