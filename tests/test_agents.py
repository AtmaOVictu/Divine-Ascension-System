import unittest
from divine_agents import (
    Agent,
    GranularniPrehodi,
    Nanoaplikacija,
    Interakcije,
    UcenjeIzIzkusenj,
    philosophical_dialogue,
)


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

    def test_granular_prehodi(self):
        agent = Agent("A")
        prehodi = GranularniPrehodi(agent)
        new_state = prehodi.prehod(0.6, 0.8)
        self.assertEqual(new_state, "Jaz")

    def test_nanoaplikacija(self):
        agent = Agent("A", tension=0.9)
        nano = Nanoaplikacija(agent)
        tension = nano.optimiziraj_napetost()
        self.assertLessEqual(tension, 0.7)

    def test_learning(self):
        agent = Agent("A")
        agent.history.append("helped")
        learning = UcenjeIzIzkusenj(agent)
        decision = learning.odlocitev("danger")
        self.assertEqual(decision, "Act selflessly")


if __name__ == '__main__':
    unittest.main()
