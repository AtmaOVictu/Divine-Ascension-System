import unittest
from divine_agents import Agent, Emotion, State, philosophical_dialogue, parallel_dialogues


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, State.JAZ)

    def test_responses(self):
        agent = Agent("A", state=State.ENOTNOST)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state=State.JAZ)
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_parallel_dialogues(self):
        pairs = [(Agent("X1"), Agent("X2", state=State.JAZ))]
        results = parallel_dialogues(pairs)
        self.assertEqual(len(results), 1)


if __name__ == "__main__":
    unittest.main()
