import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentSystem(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.set_emotion("jeza", 0.8)
        self.assertEqual(agent.transition(), "Jaz")

    def test_response_emotion_visibility(self):
        agent = Agent("B", state="Enotnost")
        agent.set_emotion("mir", 0.4)
        self.assertIn("mir", agent.respond("Kaj je resnica?"))
        agent.hide_emotion(True)
        self.assertNotIn("mir", agent.respond("Kaj je resnica?"))

    def test_dialogue_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_dialogue_hidden_emotions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, hide_emotions=True)
        # first lines should not reveal emotion labels
        self.assertFalse(any("(jeza)" in line or "(veselje)" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
