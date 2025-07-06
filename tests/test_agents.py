import unittest

from divine_agents import (
    Agent,
    philosophical_dialogue,
    generate_rhythm_sequence,
    state_rhythm,
)


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6, "fear")
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

    def test_rhythm_sequence(self):
        agent = Agent("C")
        agent.update_tension(0.8)
        agent.transition()
        seq = generate_rhythm_sequence(agent)
        self.assertEqual(seq, [state_rhythm("Ego"), state_rhythm("Jaz")])


if __name__ == '__main__':
    unittest.main()
