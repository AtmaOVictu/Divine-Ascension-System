import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.command_center import CommandCenter


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

    def test_emotional_response(self):
        agent = Agent("B1")
        agent.update_emotion(0.6, emotion_type="fear")
        response = agent.respond("Kaj je resnica?")
        self.assertIn("strah", response)

    def test_command_center(self):
        a1 = Agent("C1", tension=0.8)
        a2 = Agent("C2", state="Jaz", tension=0.9)
        center = CommandCenter([a1, a2])
        reports = center.execute_commands()
        self.assertIn("C1 prehaja iz Ego v Jaz", reports)
        self.assertIn("C2 prehaja iz Jaz v Enotnost", reports)


if __name__ == '__main__':
    unittest.main()
