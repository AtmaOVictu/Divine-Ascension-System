import unittest

from divine_agents.agent import (
    Agent,
    MultiLayerTransitionSystem,
    ExperienceBasedLearning,
)
from divine_agents.dialogue import PhilosophicalDialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_threshold(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_multi_layer_transition(self):
        agent = Agent("C", loyalty=0.9)
        mlt = MultiLayerTransitionSystem(agent)
        agent.update_emotion(0.9)
        new_state = mlt.multi_layer_transition()
        self.assertEqual(new_state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)


class TestDialogue(unittest.TestCase):
    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        dlg = PhilosophicalDialogue(a1, a2)
        lines = dlg.start()
        self.assertTrue(any("Enotnost" in line for line in lines))


class TestLearning(unittest.TestCase):
    def test_learning_decision(self):
        agent = Agent("Learn")
        learn = ExperienceBasedLearning(agent)
        learn.update_experience("danger", -1)
        agent.update_emotion(0.8)
        agent.transition()
        decision = learn.decide("danger")
        self.assertEqual(decision, "Self-preservation")
        learn.update_experience("danger", 2)
        decision = learn.decide("danger")
        self.assertEqual(decision, "Act selflessly")


if __name__ == "__main__":
    unittest.main()
