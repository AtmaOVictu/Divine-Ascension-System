import unittest
from divine_agents.agent import Agent, AgentWithHistory, EmotionalAgent
from divine_agents.dialogue import philosophical_dialogue, dynamic_dialogue


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

    def test_history_based_transition(self):
        agent = AgentWithHistory("H")
        for _ in range(3):
            agent.update_tension(0.8)
            agent.transition()
        self.assertIn(agent.state, ("Jaz", "Enotnost"))

    def test_dynamic_dialogue(self):
        a1 = AgentWithHistory("D1")
        a2 = AgentWithHistory("D2", state="Jaz")
        lines = dynamic_dialogue(a1, a2)
        self.assertTrue(any(word in lines[-1] for word in ["Jaz", "Enotnost"]))

    def test_emotional_interaction(self):
        a1 = EmotionalAgent("E1")
        a2 = EmotionalAgent("E2", state="Jaz")
        a1.update_tension(0.6)
        a2.update_tension(0.6)
        a1.interact(a2)
        self.assertGreater(a1.emotion, 0)


if __name__ == '__main__':
    unittest.main()
