import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_with_emotion(self):
        agent = Agent(name="FilozofskiAgent", state="Ego")
        agent.update_emotion(0.8, "strah")
        self.assertEqual(agent.transition(), "Jaz")
        self.assertEqual(
            agent.response_with_emotion("To je filozofsko vprašanje."),
            "S strahom: To je filozofsko vprašanje."
        )

        agent.update_emotion(0.9, "veselje")
        self.assertEqual(agent.transition(), "Enotnost")
        self.assertEqual(
            agent.response_with_emotion("Mogoče bi morali bolj raziskovati."),
            "Z veseljem: Mogoče bi morali bolj raziskovati."
        )

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertEqual(len(lines), 2)


if __name__ == '__main__':
    unittest.main()
