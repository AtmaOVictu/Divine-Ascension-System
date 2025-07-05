import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.processor import OntoProcesor


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


class TestOntoProcesor(unittest.TestCase):
    def test_reduce_tension(self):
        agent = Agent("A")
        agent.meta_ego.napetost = 0.8
        agent.onto_procesor.izracunaj_napetost()
        self.assertLess(agent.meta_ego.napetost, 0.8)

    def test_symbol_transition(self):
        agent = Agent("B")
        agent.prehod("B")  # sets high tension and optimizes to Jaz
        self.assertEqual(agent.state, "Jaz")
        agent.prehod("D")  # additional transition due to tension
        self.assertEqual(agent.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()
