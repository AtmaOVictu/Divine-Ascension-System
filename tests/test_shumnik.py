import unittest

from divine_agents.agent import Agent
from divine_agents.shumnik import Shumnik, tension_effect, reflection_effect


class TestShumnikIntegration(unittest.TestCase):
    def test_shumnik_activation_affects_tension(self):
        agent = Agent("B")
        agent.update_tension(0.6)
        s = Shumnik("ŠumT", "Tension phase", tension_effect)
        agent.interact_with_shumnik(s)
        self.assertGreater(agent.tension, 0.6)

    def test_transition_via_shumnik(self):
        agent = Agent("B", tension=0.6)
        s = Shumnik("ŠumT", "Tension phase", tension_effect)
        agent.interact_with_shumnik(s)
        state = agent.transition()
        self.assertEqual(state, "Jaz")


if __name__ == "__main__":
    unittest.main()
