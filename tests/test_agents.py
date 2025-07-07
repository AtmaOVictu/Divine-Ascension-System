import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.krak import Krak


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

class TestKrak(unittest.TestCase):
    def test_krak_emotion_adapts_task(self):
        krak = Krak("K1")
        krak.update_emotion(0.8)
        self.assertEqual(krak.task, "high_emotion_task")

    def test_krak_transition_updates_task(self):
        krak = Krak("K2")
        krak.update_tension(0.9)
        krak.transition()
        self.assertEqual(krak.state, "Jaz")
        self.assertEqual(krak.task, "task_updated")


if __name__ == '__main__':
    unittest.main()
