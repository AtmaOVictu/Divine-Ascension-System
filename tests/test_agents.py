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
        lines = philosophical_dialogue(a1, a2, emotion1="fear", emotion2="joy")
        self.assertTrue(any("Enotnost" in line for line in lines))
        # check that emotion name is reflected in responses
        self.assertTrue(any("Čustvo: fear" in line for line in lines))

    def test_emotion_transition(self):
        agent = Agent("B")
        agent.set_emotion("anger", 0.6)
        agent.transition()
        self.assertEqual(agent.state, "Jaz")


if __name__ == '__main__':
    unittest.main()
