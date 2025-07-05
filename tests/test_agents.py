import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.orchestrator import AgentDirigent, Zbor, DivinitetniAgent


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


class TestDirigentAndZbor(unittest.TestCase):
    def test_dirigent_orchestrates(self):
        a1 = Agent("A1", tension=0.8)
        dirg = AgentDirigent("D")
        dirg.add_agent(a1)
        dirg.orchestrate()
        self.assertEqual(a1.state, "Jaz")

    def test_zbor_collective(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        zb = Zbor()
        zb.add_agent(a1)
        zb.add_agent(a2)
        zb.collective_consciousness()
        self.assertEqual(a1.state, "Enotnost")
        self.assertEqual(a2.state, "Enotnost")


class TestDivinitetniAgent(unittest.TestCase):
    def test_elevate(self):
        mentor = DivinitetniAgent("Mentor")
        student = Agent("Student")
        mentor.elevate(student)
        self.assertEqual(student.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()
