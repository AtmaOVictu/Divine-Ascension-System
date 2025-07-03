import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, run_parallel_dialogues


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_trigger(self):
        agent = Agent("B")
        agent.set_emotion("strah", 0.6)
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

    def test_parallel_dialogues(self):
        pairs = [
            (Agent("P1"), Agent("P2", state="Jaz")),
            (Agent("P3"), Agent("P4", state="Jaz")),
        ]
        results = run_parallel_dialogues(pairs)
        self.assertEqual(len(results), 2)
        self.assertTrue(any("Enotnost" in line for convo in results for line in convo))


if __name__ == '__main__':
    unittest.main()
