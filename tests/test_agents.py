import unittest

from divine_agents import (
    Agent,
    FreeWillAgent,
    InteractionAgent,
    LearningAgent,
    SimulationPhase,
    philosophical_dialogue,
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

    def test_learning_and_interaction(self):
        learner = LearningAgent("L")
        learner.update_tension(0.9)
        learner.transition()
        last = learner.learn_from_past()
        self.assertEqual(last, "Jaz")

        other = InteractionAgent("O", state="Jaz")
        result = other.interact(InteractionAgent("P"))
        self.assertIn(result, {"cooperate", "compete"})

    def test_simulation_phase(self):
        agent = Agent("S")
        agent.update_tension(0.9)
        phase = SimulationPhase("Test", moral_dilemma=True)
        phase.run(agent)
        self.assertTrue(any("Moral dilemma decision" in h for h in agent.history))

    def test_free_will(self):
        agent = FreeWillAgent("F")
        decision = agent.make_decision()
        self.assertIn(decision, {"bold", "cautious"})


if __name__ == '__main__':
    unittest.main()
