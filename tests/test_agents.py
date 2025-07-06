import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, emotional_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotional_state_transition(self):
        agent = Agent("A")
        agent.set_emotion_state("anger", 0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_emotional_prefix(self):
        agent = Agent("A")
        agent.set_emotion_state("fear", 0.2)
        self.assertTrue(agent.respond("?").startswith("Zaskrbljeno"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_emotional_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = emotional_dialogue(a1, a2)
        self.assertTrue(any("čuti" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
