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
        lines = philosophical_dialogue(
            a1,
            a2,
            emotion_inc1=0.9,
            emotion_inc2=0.7,
            tension_inc1=0.1,
            tension_inc2=0.1,
            extra_turns=["Custom message"],
        )
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertIn("Custom message", lines)


if __name__ == '__main__':
    unittest.main()
