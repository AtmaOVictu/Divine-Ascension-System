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

    def test_dynamic_tension(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        a1.add_teammate(a2)
        a2.update_emotion(0.9)
        a1.update_tension_dynamic()
        self.assertGreater(a1.tension, 0)

    def test_moral_decision(self):
        agent = Agent("A", tension=0.8, emotional_state="fearful")
        decision = agent.make_moral_decision("test")
        self.assertIn("selfishly", decision)


if __name__ == '__main__':
    unittest.main()
