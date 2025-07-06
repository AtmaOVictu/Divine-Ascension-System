import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.multi_layer import (
    MultiLayerTransitionSystem,
    ExperienceBasedLearning,
    HistoricalRefactor,
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

    def test_emotion_tension_adjustment(self):
        agent = Agent("A")
        agent.update_emotion(0.3, "angry")
        self.assertEqual(agent.tension, 0.3)

    def test_learning_and_refactor(self):
        agent = Agent("A")
        learner = ExperienceBasedLearning(agent)
        agent.add_experience("helped")
        decision = learner.learn_from_past_decisions("danger")
        self.assertEqual(decision, "Act selflessly")

        agent.history.append("hesitation")
        ref = HistoricalRefactor(agent)
        ref.auto_refactor()
        self.assertEqual(agent.state, "Jaz")

    def test_multi_layer_transition(self):
        agent = Agent("A", tension=0.8)
        agent.emotional_state = "fearful"
        system = MultiLayerTransitionSystem(agent)
        state = system.multi_layer_transition()
        self.assertEqual(state, "Ego")


if __name__ == "__main__":
    unittest.main()
