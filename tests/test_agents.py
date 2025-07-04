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
        agent = Agent("A", state="Enotnost", emotion=0.8)
        reply = agent.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("Strastno"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Ensure state transition occurred
        self.assertTrue(any("prehaja v stanje" in line for line in lines))
        # Ensure numerology value included
        self.assertTrue(any("vrednost" in line for line in lines))

    def test_state_value(self):
        agent = Agent("A")
        self.assertEqual(agent.state_value, Agent.numerology("Ego"))


if __name__ == '__main__':
    unittest.main()
