import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.simulation import dynamic_debate


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
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_dynamic_debate_transition(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        lines = dynamic_debate(a1, a2, rounds=5)
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)
        self.assertTrue(any("prehaja v stanje" in l for l in lines))

    def test_emotional_response_prefix(self):
        a = Agent("X", tension=0.0, emotion=0.8)
        reply = a.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("S silovitim"))


if __name__ == '__main__':
    unittest.main()
