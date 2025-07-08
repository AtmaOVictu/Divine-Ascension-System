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
        agent.update_emotion(0.2)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, ["Kaj je resnica?"])
        self.assertEqual(len(lines), 4)

    def test_emotional_transition(self):
        a1 = Agent("X")
        a2 = Agent("Y", state="Jaz")
        questions = ["Kaj je resnica?"] * 4
        philosophical_dialogue(a1, a2, questions)
        self.assertEqual(a1.state, "Enotnost")
        self.assertEqual(a2.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()
