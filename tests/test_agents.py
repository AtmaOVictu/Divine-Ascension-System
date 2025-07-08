import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        agent.update_emotion(0.6, "joy")
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_frame_history(self):
        agent = Agent("B")
        agent.update_emotion(0.6, "fear")
        agent.transition()
        agent.update_emotion(0.6, "joy")
        agent.transition()
        self.assertEqual(len(agent.get_history()), len(agent.get_frames()))
        self.assertEqual(agent.get_history()[-1], "Enotnost")

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("absolutna" in line for line in lines))
        self.assertTrue(any("relativna" in line for line in lines))
        self.assertTrue(any("Enotnost" in line or "eno" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
