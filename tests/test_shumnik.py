import unittest
from divine_agents import Agent, shumnik_tension, shumnik_reflection


class TestShumnikIntegration(unittest.TestCase):
    def test_tension_shumnik_triggers_transition(self):
        agent = Agent("A")
        shumnik_tension.activate(agent)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_reflection_shumnik_to_enotnost(self):
        agent = Agent("B", state="Jaz")
        shumnik_reflection.activate(agent)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")


if __name__ == '__main__':
    unittest.main()
