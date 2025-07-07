import unittest
from divine_agents.agent import Agent
from divine_agents.command_center import CommandCenter
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_trigger(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        center = CommandCenter()
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, center=center)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertEqual(len(center.log), 4)

    def test_command_center(self):
        center = CommandCenter()
        agent = Agent("C")
        center.send_command(agent, "excite")
        self.assertGreater(agent.emotion, 0.0)
        center.send_command(agent, "calm")
        self.assertLessEqual(agent.tension, 0.5)


if __name__ == '__main__':
    unittest.main()
