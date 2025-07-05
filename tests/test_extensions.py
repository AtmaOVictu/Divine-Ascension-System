import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.extensions import (
    LearningAgent,
    InteractionAgent,
    FreeWillAgent,
    SimulationPhase,
)


class TestLearningAgent(unittest.TestCase):
    def test_learn_and_adapt(self):
        agent = LearningAgent("L")
        agent.update_emotion(0.6)
        agent.transition()
        agent.learn_from_past()
        self.assertIn("Transitioned", agent.learning_history[-1])
        agent.adapt_to_environment()


class TestInteractionAgent(unittest.TestCase):
    def test_interaction_outcome(self):
        a1 = InteractionAgent("A1")
        a2 = InteractionAgent("A2", state="Jaz")
        outcome = a1.interact(a2)
        self.assertEqual(outcome, "compete")


class TestFreeWillAgent(unittest.TestCase):
    def test_make_decision(self):
        agent = FreeWillAgent("F")
        with patch("random.random", return_value=0.9):
            decision = agent.make_decision()
        self.assertEqual(decision, "bold")


class TestSimulationPhase(unittest.TestCase):
    def test_moral_dilemma(self):
        agent = LearningAgent("L")
        agent.update_tension(0.9)
        phase = SimulationPhase("test", moral_dilemma=True)
        phase.run(agent)
        self.assertIn("Moral dilemma decision", agent.history[-1])


if __name__ == "__main__":
    unittest.main()
