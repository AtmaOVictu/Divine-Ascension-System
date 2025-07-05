import unittest

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestEmotionalDialogue(unittest.TestCase):
    def test_emotion_triggers_transition(self):
        agent = Agent("X")
        agent.set_emotion("fear", 0.6)
        agent.transition()
        self.assertEqual(agent.state, "Jaz")

    def test_emotional_response_phrase(self):
        agent = Agent("Y", emotion_name="joy")
        agent.update_emotion(0.2)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("veselje", reply)

    def test_philosophical_dialogue_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("čuti" in line for line in lines))
        self.assertIn("Jaz", a1.state)
        self.assertIn(a2.state, Agent.STATES)


if __name__ == "__main__":
    unittest.main()
