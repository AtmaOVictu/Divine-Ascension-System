import unittest
from divine_agents import Agent, InteractionAgent, SimulationPhase, AdvancedAgent
from divine_agents.dialogue import philosophical_dialogue


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

    def test_emotion_update(self):
        agent = Agent("B")
        agent.update_love(0.7)
        self.assertGreater(agent.emotion, 0)

    def test_interaction_and_moral_dilemma(self):
        a1 = InteractionAgent("I1")
        a2 = InteractionAgent("I2")
        outcome = a1.interact(a2)
        self.assertIn(outcome, {"cooperate", "compete", "attack", "defend"})

        phase = SimulationPhase("test", moral_dilemma=True)
        decision = phase.run(a1)
        self.assertIn("choose", decision)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_advanced_agent_transition(self):
        agent = AdvancedAgent("AA")
        agent.update_love(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")


if __name__ == '__main__':
    unittest.main()
