import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, multi_round_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_emotion("joy")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost", emotion="fear")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("With fear", reply)
        self.assertIn("Vse resnice so eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))

    def test_multi_round_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = multi_round_dialogue(a1, a2, rounds=2, seed=1)
        self.assertEqual(len(lines), 4)
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)


if __name__ == '__main__':
    unittest.main()
