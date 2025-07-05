import unittest
from divine_agents.agent import Agent, OracleAgent
from divine_agents.dialogue import philosophical_dialogue, oracle_dialogue


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


class TestOracleAgent(unittest.TestCase):
    def test_records_transitions(self):
        oracle = OracleAgent("O")
        oracle.update_tension(0.8)
        oracle.transition()
        self.assertEqual(len(oracle.transitions), 1)

    def test_oracle_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        oracle = OracleAgent("Oracle")
        lines = oracle_dialogue(a1, a2, oracle)
        self.assertTrue(any("Oracle predlaga" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
