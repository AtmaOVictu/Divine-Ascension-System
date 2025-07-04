import unittest
from divine_agents import Agent, InteractionManager


class TestInteractionManager(unittest.TestCase):
    def test_exchange_triggers_transition(self):
        a1 = Agent('A1')
        a2 = Agent('A2', state='Jaz')
        manager = InteractionManager(a1, a2)
        # High emotions should push a1 to Jaz and a2 to Enotnost
        lines = manager.exchange(0.8, 0.8)
        self.assertIn('Jaz', a1.state)
        self.assertIn('Enotnost', a2.state)
        # Dialogue should reference their new states
        self.assertTrue(any('Jaz' in line or 'Enotnost' in line for line in lines))

    def test_simulate_multiple_steps(self):
        a1 = Agent('A1')
        a2 = Agent('A2')
        manager = InteractionManager(a1, a2)
        steps = [(0.4, 0.4), (0.8, 0.8)]
        dialogue = manager.simulate(steps)
        # After final step both should be at least Jaz
        self.assertIn(a1.state, ['Jaz', 'Enotnost'])
        self.assertIn(a2.state, ['Jaz', 'Enotnost'])
        self.assertEqual(len(dialogue) > 0, True)


if __name__ == '__main__':
    unittest.main()
