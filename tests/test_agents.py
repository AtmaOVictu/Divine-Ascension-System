import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.learning import ExperienceBasedLearning


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
        agent = Agent("B", loyalty=0.9, emotional_state="happy")
        state = agent.multi_layer_transition()
        self.assertEqual(state, "Jaz")

    def test_emotional_tension_adjustment(self):
        agent = Agent("C", emotional_state="angry")
        agent.adjust_tension_based_on_emotions()
        self.assertGreater(agent.tension, 0)

    def test_learning_from_experience(self):
        agent = Agent("D")
        agent.add_experience("helped")
        learner = ExperienceBasedLearning(agent)
        decision = learner.learn_from_past_decisions("danger")
        self.assertEqual(decision, "Act selflessly")


if __name__ == '__main__':
    unittest.main()
