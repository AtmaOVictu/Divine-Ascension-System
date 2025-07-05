import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        agent = Agent("B")
        agent.update_emotion(0.6, "fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        agent.update_emotion(0.6, "joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("(joy)"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertEqual(len(lines), 6)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_section_transition(self):
        agent = Agent("B", tension=0.1, emotion=0.2)
        state = agent.section_transition()
        self.assertEqual(state, "Ego")
        agent.update_emotion(0.6, "fear")
        state = agent.section_transition()
        self.assertEqual(state, "Jaz")


if __name__ == '__main__':
    unittest.main()
