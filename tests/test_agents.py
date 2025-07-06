import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_tension_based_transition(self) -> None:
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_based_transition(self) -> None:
        agent = Agent("B")
        agent.update_emotion("fear", 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self) -> None:
        agent = Agent("A", state="Enotnost")
        agent.update_emotion("joy", 0.2)
        reply = agent.respond()
        self.assertIn("eno", reply)

    def test_dialogue(self) -> None:
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("Čutim" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
