import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.extensions import (
    LearningAgent,
    InteractionAgent,
    FreeWillAgent,
)


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

    def test_learning_agent(self):
        agent = LearningAgent("L1")
        agent.update_tension(0.9)
        agent.transition()
        agent.learn_from_past()
        self.assertIn("Transitioned", agent.learning_history[0])

    def test_interaction(self):
        a1 = InteractionAgent("I1")
        a2 = InteractionAgent("I2", state="Jaz")
        result = a1.interact(a2)
        self.assertIn(result, {"cooperate", "compete"})

    def test_free_will_agent(self):
        agent = FreeWillAgent("F1")
        decision = agent.make_decision()
        self.assertIn(decision, {"bold", "cautious"})


if __name__ == '__main__':
    unittest.main()
