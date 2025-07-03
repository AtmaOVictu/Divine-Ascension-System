import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, philosophical_debate


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
        a1.update_tension(0.8)
        a2.update_tension(0.8)
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any(state in line for state in ("Jaz", "Enotnost") for line in lines))

    def test_emotion_effect_triggers_transition(self):
        agent = Agent("B")
        agent.apply_emotion_effect("anger")
        agent.apply_emotion_effect("anger")
        agent.transition()
        self.assertEqual(agent.state, "Jaz")

    def test_philosophical_debate(self):
        a1 = Agent("X1")
        a2 = Agent("X2", state="Jaz")
        lines = philosophical_debate(a1, a2, rounds=2)
        self.assertTrue(len(lines) >= 4)


if __name__ == '__main__':
    unittest.main()
