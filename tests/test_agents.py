import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.learning import ExperienceBasedLearning
from divine_agents.refactor import HistoricalRefactor


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

    def test_historical_transition(self):
        agent = Agent("B", experiences=["self-preservation"])
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_learning_decision(self):
        agent = Agent("C")
        learner = ExperienceBasedLearning(agent)
        learner.update_experience("debate", 1)
        decision = learner.decide("debate")
        self.assertEqual(decision, "Act selflessly")

    def test_refactor_message(self):
        agent = Agent("D")
        agent.history.extend(["hesitation", "hesitation"])
        ref = HistoricalRefactor(agent)
        msg = ref.auto_refactor()
        self.assertIn("Jaz", msg)


if __name__ == '__main__':
    unittest.main()
