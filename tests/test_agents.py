import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_with_emotion(self):
        agent = Agent("FilozofskiAgent")
        agent.update_emotion(0.8, "strah")
        self.assertEqual(agent.transition(), "Jaz")
        self.assertEqual(
            agent.response_with_emotion("To je filozofsko vprasanje."),
            "S strahom: To je filozofsko vprasanje.")

        agent.update_emotion(0.9, "veselje")
        self.assertEqual(agent.transition(), "Enotnost")
        self.assertEqual(
            agent.response_with_emotion("Mogoce bi morali bolj raziskovati."),
            "Z veseljem: Mogoce bi morali bolj raziskovati.")

    def test_transition_to_res001(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion(0.9, "veselje")
        self.assertEqual(agent.transition(), "RES001")

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("S strahom" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
