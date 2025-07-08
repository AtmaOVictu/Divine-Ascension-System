import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.knowledge import KnowledgeBase, AutoLearningSystem


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

    def test_emotion_trigger_transition(self):
        agent = Agent("B")
        agent.update_emotion("anger", 0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_learning_system(self):
        agent = Agent("C")
        kb = KnowledgeBase()
        system = AutoLearningSystem(agent, kb)
        response = system.process("nov koncept")
        self.assertIn(agent.state, agent.history)
        self.assertTrue(kb.add_knowledge("drug koncept"))


if __name__ == '__main__':
    unittest.main()
