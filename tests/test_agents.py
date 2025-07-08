import unittest
import random

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.learning import KnowledgeBase, AutoLearningSystem


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


class TestLearningSystem(unittest.TestCase):
    def test_knowledge_base(self):
        kb = KnowledgeBase()
        self.assertTrue(kb.add_knowledge("alpha"))
        self.assertFalse(kb.add_knowledge("alpha"))
        self.assertFalse(kb.is_new("alpha"))
        self.assertTrue(kb.is_new("beta"))

    def test_random_exploration(self):
        kb = KnowledgeBase()
        system = AutoLearningSystem(kb)
        system.process_input("concept")
        random.seed(0)
        self.assertEqual(system.random_exploration(), "concept")


if __name__ == '__main__':
    unittest.main()
