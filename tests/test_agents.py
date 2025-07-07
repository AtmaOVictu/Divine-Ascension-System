import unittest
from divine_agents import Agent, OntoComputerUseAgent, philosophical_dialogue


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

    def test_emotion_based_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6, "strah")
        new_state = agent.transition()
        self.assertEqual(new_state, "Jaz")

    def test_computer_use_agent(self):
        cua = OntoComputerUseAgent("C")
        result = cua.execute_action("click", {"x": 1, "y": 2})
        self.assertIn("∴", result)
        self.assertIn("⊘", result)


if __name__ == '__main__':
    unittest.main()

