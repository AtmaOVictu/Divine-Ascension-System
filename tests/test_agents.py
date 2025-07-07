import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, dynamic_dialogue


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

    def test_emotion_driven_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_dynamic_dialogue(self):
        a1 = Agent("C1")
        a2 = Agent("C2", state="Jaz")
        lines = dynamic_dialogue(a1, a2, rounds=3)
        # after several rounds emotions should drive them forward
        self.assertTrue(a1.state in Agent.STATES)
        self.assertTrue(a2.state in Agent.STATES)
        self.assertEqual(len(lines), 6)


if __name__ == '__main__':
    unittest.main()
