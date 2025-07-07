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
        # default emotions should transition a2 to Enotnost
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_dialogue_custom_emotions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, emotion1=0.4, emotion2=0.4)
        # emotions below threshold should keep original states
        self.assertIn("A1 prehaja v stanje: Ego", lines[2])
        self.assertIn("A2 prehaja v stanje: Jaz", lines[3])


if __name__ == '__main__':
    unittest.main()
