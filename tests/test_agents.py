import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.interaction import Kapacitor


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


class TestKapacitor(unittest.TestCase):
    def test_activation(self):
        k = Kapacitor()
        k.sprejmi_vhod("aktiviraj")
        stanje, intenziteta = k.preveri_stanje()
        self.assertEqual(stanje, "Aktivacija")
        self.assertGreaterEqual(intenziteta, 0.3)

    def test_transition(self):
        k = Kapacitor()
        k.sprejmi_vhod("prehod")
        stanje, intenziteta = k.preveri_stanje()
        self.assertEqual(stanje, "Prehod")
        self.assertGreaterEqual(intenziteta, 0.5)


if __name__ == '__main__':
    unittest.main()
