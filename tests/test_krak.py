import unittest
from divine_agents.krak import Krak
from divine_agents.dialogue import emotional_dialogue
from divine_agents.agent import Agent


class TestKrak(unittest.TestCase):
    def test_krak_transition_on_emotion(self):
        k = Krak("K")
        k.update_emotion(0.8)
        state = k.transition()
        self.assertEqual(state, "Jaz")
        self.assertIn(("Jaz", "task_updated"), k.krak_history)

    def test_emotional_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = emotional_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
