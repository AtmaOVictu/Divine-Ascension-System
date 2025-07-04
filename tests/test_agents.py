import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, dynamic_dialogue


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

    def test_set_emotion_and_transition(self):
        agent = Agent("A")
        agent.set_emotion("strah", 0.6)
        self.assertEqual(agent.emotion_label, "strah")
        self.assertGreater(agent.tension, 0.5)
        self.assertEqual(agent.transition(), "Jaz")

    def test_dynamic_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = dynamic_dialogue(a1, a2)
        self.assertTrue(a1.state != "Ego" or a2.state != "Jaz")
        self.assertTrue(any("občutek" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
