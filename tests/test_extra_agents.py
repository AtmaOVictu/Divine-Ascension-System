import unittest
from divine_agents.extra_agents import (
    ReasonAgent,
    InterpolationAgent,
    IntercontinentalizationAgent,
)
from divine_agents.agent import Agent


class TestExtraAgents(unittest.TestCase):
    def test_reason_agent_logic(self):
        r = ReasonAgent('R')
        r.update_logic(0.6)
        self.assertIn('valid', r.reason('smisel'))

    def test_interpolation_transition(self):
        a1 = Agent('A1')
        a2 = Agent('A2', state='Jaz')
        interp = InterpolationAgent('I', interpolation_level=0.8)
        self.assertIn('Interpolating', interp.interpolate(a1, a2))
        interp.update_emotion(0.8)
        self.assertEqual(interp.transition(), 'Jaz')

    def test_intercontinental_connect(self):
        a1 = Agent('A1')
        a2 = Agent('A2')
        intercon = IntercontinentalizationAgent('IC', reach=0.9)
        self.assertIn('Connecting', intercon.connect_worlds(a1, a2))
        intercon.update_emotion(0.8)
        self.assertEqual(intercon.transition(), 'Jaz')


if __name__ == '__main__':
    unittest.main()

