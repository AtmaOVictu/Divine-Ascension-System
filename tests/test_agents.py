import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.granular import GranularniPrehodi
from divine_agents.nanoapp import Nanoaplikacija
from divine_agents.interaction import Interakcije
from divine_agents.learning import UcenjeIzIzkusenj


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


class TestModularComponents(unittest.TestCase):
    def test_granularni_prehodi(self):
        agent = Agent("G")
        gp = GranularniPrehodi(agent)
        state = gp.prehod("anger", 0.9, agent.history)
        self.assertEqual(state, "Jaz")

    def test_nanoaplikacija(self):
        agent = Agent("N", tension=1.0)
        nano = Nanoaplikacija(agent)
        tension = nano.optimiziraj_napetost()
        self.assertLessEqual(tension, 0.7)

    def test_interakcije(self):
        a1 = Agent("A1", emotion="calm")
        a2 = Agent("A2", emotion="anger")
        inter = Interakcije(a1, a2)
        inter.medsebojna_interakcija()
        self.assertGreater(a1.tension, 0)

    def test_ucenje(self):
        agent = Agent("U")
        learn = UcenjeIzIzkusenj(agent)
        decision = learn.uci_se("danger")
        self.assertEqual(decision, "Self-preservation")


if __name__ == '__main__':
    unittest.main()
