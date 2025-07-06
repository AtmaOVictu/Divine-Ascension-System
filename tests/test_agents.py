import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.automation import AutomatskiPrehodi, SamodejnaOptimizacija
from divine_agents.qlearning import QLearningAgent


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

    def test_automatic_transitions(self):
        agent = Agent("Auto")
        agent.update_tension(0.8)
        auto = AutomatskiPrehodi(agent)
        self.assertEqual(auto.preveri_pogoje_za_prehod(), "Jaz")

    def test_automatic_optimization(self):
        agent = Agent("Opt", tension=0.9)
        agent.history.append("error detected")
        optimizer = SamodejnaOptimizacija(agent)
        optimizer.optimiziraj_kodo()
        self.assertLess(agent.tension, 0.9)

    def test_qlearning_update(self):
        q_agent = QLearningAgent(actions=["a", "b"])
        value = q_agent.update_q_value("s1", "a", 1, "s2")
        self.assertIn("a", q_agent.q_table["s1"])
        self.assertEqual(value, q_agent.q_table["s1"]["a"])


if __name__ == '__main__':
    unittest.main()
