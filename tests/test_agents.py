import unittest
from divine_agents.agent import Agent
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

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_moral_decision(self):
        agent = Agent("A", emotional_state="fearful", loyalty=0.8)
        decision = agent.make_moral_decision("danger")
        self.assertIn("help others", decision)

    def test_collaborative_task(self):
        a1 = Agent("A1", emotional_state="happy", loyalty=0.8)
        a2 = Agent("A2", emotional_state="happy", loyalty=0.8)
        a1.team = [a1, a2]
        a2.team = [a1, a2]
        result = a1.collaborative_task()
        self.assertIn("successfully", result)


if __name__ == '__main__':
    unittest.main()
