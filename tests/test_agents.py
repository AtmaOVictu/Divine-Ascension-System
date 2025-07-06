import unittest
import random
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
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_mutation_and_reincarnation(self):
        random.seed(0)
        agent = Agent("M")
        original = agent.dna.copy()
        mutated = agent.mutate(rate=0.1)
        self.assertEqual(len(mutated), len(original))
        self.assertTrue(any(m != o for m, o in zip(mutated, original)))

        child = agent.reincarnate("Child")
        self.assertIsInstance(child, Agent)
        self.assertTrue(any(c != a for c, a in zip(child.dna, agent.dna)))
        self.assertEqual(child.name, "Child")


if __name__ == '__main__':
    unittest.main()
