import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.stabilization import NujnaSenca, DrugaPravaOs, NucnoNiclo


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

    def test_nujna_senca(self):
        agent = Agent("A")
        senca = NujnaSenca("Temna faza", 0.9)
        msg = senca.prehod_v_senco(agent)
        self.assertIn("nujno fazo sence", msg)
        self.assertEqual(agent.state, "Jaz")

    def test_druga_prava_os(self):
        agent = Agent("A")
        axis = DrugaPravaOs("Svetla pot", 0.7)
        smer = axis.doloci_smer(agent)
        self.assertEqual(smer, "proaktivna")
        self.assertGreater(agent.emotion, 0.0)

    def test_nucno_niclo(self):
        niclo = NucnoNiclo()
        msg = niclo.stabilizacija()
        self.assertEqual(niclo.stanje, "stabilno")
        self.assertIn("ničelnem stanju", msg)


if __name__ == '__main__':
    unittest.main()
