import unittest
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, dynamic_debate
from divine_agents.special_agents import AgentNEZNANKA, AgentNEZNANKA_ZVOK, AgentPI, AgentROM


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

    def test_dynamic_debate(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        dynamic_debate(a1, a2, rounds=2)
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")

    def test_special_agents(self):
        n = AgentNEZNANKA()
        self.assertEqual(n.zaznaj("napetost brez definicije")[1], "neizreceno")

        zv = AgentNEZNANKA_ZVOK()
        self.assertEqual(zv.zaznaj_in_zveni("prilo\u017enost za akcijo"), "zven")

        pi = AgentPI()
        self.assertEqual(pi.zaznaj("rast v tisi\u0161ini"), "rast v presledku")

        rom = AgentROM()
        self.assertEqual(rom.rast("alarm zaznan kot odgovor"), "rast sistema")


if __name__ == '__main__':
    unittest.main()
