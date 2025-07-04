import unittest
from divine_agents.agent import Agent
from divine_agents.shumnik import Shumnik, tension_effect, reflection_effect


class TestShumnik(unittest.TestCase):
    def test_tension_shumnik_triggers_transition(self):
        agent = Agent("A")
        s = Shumnik("T", "tension", tension_effect)
        agent.interact_with_shumnik(s)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_reflection_shumnik_advances_jaz_to_enotnost(self):
        agent = Agent("B", state="Jaz")
        s = Shumnik("R", "reflection", reflection_effect)
        agent.interact_with_shumnik(s)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")


if __name__ == "__main__":
    unittest.main()
