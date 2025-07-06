import unittest
import sys
from pathlib import Path

# Ensure package root is on the path for direct test execution
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.systems import (
    MultiLayerTransitionSystem,
    ExperienceBasedLearning,
    HistoricalRefactor,
    EmotionalTensionDynamics,
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

    def test_multi_layer_transition(self):
        agent = Agent("ML", loyalty=0.9, emotional_state="happy")
        mlt = MultiLayerTransitionSystem(agent)
        new_state = mlt.multi_layer_transition()
        self.assertEqual(new_state, "Jaz")

    def test_experience_based_learning(self):
        agent = Agent("EXP")
        agent.record_experience("helped a friend")
        learner = ExperienceBasedLearning(agent)
        decision = learner.learn_from_past_decisions("danger")
        self.assertEqual(decision, "Act selflessly")

    def test_emotional_tension_dynamics(self):
        agent = Agent("EMO", emotional_state="angry")
        dyn = EmotionalTensionDynamics(agent)
        dyn.adjust_tension_based_on_emotions()
        self.assertGreater(agent.tension, 0)

    def test_historical_refactor(self):
        agent = Agent("HIST")
        agent.history.append("hesitation")
        ref = HistoricalRefactor(agent)
        state = ref.auto_refactor()
        self.assertEqual(state, "Jaz")


if __name__ == "__main__":
    unittest.main()
