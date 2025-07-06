import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.analysis import AgentTenzije, AgentSpoznanja, AgentD


class TestAnalysisAgents(unittest.TestCase):
    def test_tenzije_interpretation(self):
        a = AgentTenzije()
        result = a.interpretiraj("ritem srca")
        self.assertEqual(result, "vrsta tenzije – ciklicna napetost")
        self.assertIn("ritem srca", a.vrste)

    def test_spoznanja_tracking(self):
        a = AgentSpoznanja()
        first = a.preveri("jaz sem glas")
        second = a.preveri("jaz sem glas")
        self.assertIn("novo spoznanje", first)
        self.assertIn("ponovitev spoznanja", second)
        self.assertEqual(len(a.ponovitve), 1)

    def test_agent_d_classification(self):
        a = AgentD()
        res = a.prepoznaj("udarec razlike")
        self.assertIn("oblika đ", res)
        self.assertIn("udarec razlike", a.preboji)


class TestDialogueStateChanges(unittest.TestCase):
    def test_states_after_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        philosophical_dialogue(a1, a2)
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")


if __name__ == "__main__":
    unittest.main()
