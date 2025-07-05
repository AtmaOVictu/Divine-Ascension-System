import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_no_transition_below_threshold(self):
        agent = Agent("A")
        agent.update_emotion(0.4)
        agent.update_tension(0.6)
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_save_and_load_state(self):
        import os
        import tempfile

        agent = Agent("Saver", state="Jaz", tension=0.5, emotion=0.2)
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "agent.json")
            agent.save(path)
            loaded = Agent.load(path)
        self.assertEqual(loaded.state, "Jaz")
        self.assertAlmostEqual(loaded.tension, 0.5)
        self.assertAlmostEqual(loaded.emotion, 0.2)


if __name__ == '__main__':
    unittest.main()
