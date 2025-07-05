import unittest
from divine_agents import Agent, NujnaSenca, DrugaPravaOs, Niclo
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

    def test_nujna_senca(self):
        agent = Agent("Shadow")
        senca = NujnaSenca("Temna faza", 0.9)
        new_state = senca.prehod_v_senco(agent)
        self.assertEqual(new_state, "Jaz")

    def test_axis_direction(self):
        agent = Agent("Axis")
        axis = DrugaPravaOs("Os", 0.7)
        direction = axis.doloci_smer(agent)
        self.assertEqual(direction, "proaktivna")

    def test_niclo(self):
        niclo = Niclo()
        state = niclo.stabilizacija()
        self.assertEqual(state, "stabilno")


if __name__ == '__main__':
    unittest.main()
