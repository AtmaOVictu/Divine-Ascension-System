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

    def test_dialogue_with_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, emotion1=0.9, emotion2=0.7)
        # Agent2 should transition to Enotnost when transitions are enabled
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_dialogue_without_transitions(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, transitions=False)
        # No state changes should be announced in the dialogue
        self.assertFalse(any("prehaja v stanje" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
