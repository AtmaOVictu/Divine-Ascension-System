import unittest
from divine_agents.agent import Agent
from divine_agents.orchestration import AgentDirigent, Zbor, DivinitetniAgent


class TestOrchestration(unittest.TestCase):
    def test_dirigent_orchestrates_transitions(self):
        a1 = Agent("A1", tension=0.8)
        a2 = Agent("A2", state="Jaz", tension=0.8)
        dirigent = AgentDirigent("D")
        dirigent.add_agent(a1)
        dirigent.add_agent(a2)
        dirigent.orchestrate()
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")

    def test_zbor_unifies_agents(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        zbor = Zbor()
        zbor.add_agent(a1)
        zbor.add_agent(a2)
        zbor.collective_consciousness()
        self.assertTrue(all(agent.state == "Enotnost" for agent in zbor.agents))

    def test_divinitetni_agent_elevates(self):
        guide = DivinitetniAgent("G")
        a = Agent("A")
        guide.elevate(a)
        self.assertEqual(a.state, "Vi\u0161ja Zavest")


if __name__ == '__main__':
    unittest.main()
