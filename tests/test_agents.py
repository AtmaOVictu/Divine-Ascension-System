import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, dynamic_dialogue
from divine_agents.codex import Codex


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

    def test_dynamic_dialogue_transition(self):
        a1 = Agent("B1")
        a2 = Agent("B2")
        lines = dynamic_dialogue(a1, a2)
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))

    def test_codex_debate(self):
        codex = Codex()
        a1 = Agent("C1")
        a2 = Agent("C2")
        codex.add_agent(a1)
        codex.add_agent(a2)
        transcript = codex.run_debate(a1, a2)
        self.assertGreater(len(transcript), 0)


if __name__ == '__main__':
    unittest.main()
