import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent, RespectAgent, DisrespectAgent, FearAgent, OneValueAgent
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
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_emotion_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Jaz")

    def test_specialised_responses(self):
        r = RespectAgent("R")
        d = DisrespectAgent("D")
        f = FearAgent("F")
        o = OneValueAgent("O", value=0.4)
        self.assertIn("Spoštovanje", r.respond("?"))
        self.assertIn("kršijo", d.respond("?"))
        self.assertIn("Strah", f.respond("?"))
        self.assertIn("Težko", o.respond("?"))


if __name__ == '__main__':
    unittest.main()
