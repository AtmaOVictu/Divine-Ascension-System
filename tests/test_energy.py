import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents import Agent, EnergyNetwork


class TestEnergyNetwork(unittest.TestCase):
    def test_transfer_increases_target_energy(self):
        a1 = Agent("A1", energy=100)
        a2 = Agent("A2", energy=0)
        net = EnergyNetwork([a1, a2])
        net.transfer(a1, a2, 0.2)
        self.assertGreater(a2.energy, 0)
        self.assertLess(a1.energy, 100)

    def test_step_cycles_energy(self):
        a1 = Agent("A1", energy=10)
        a2 = Agent("A2", energy=10)
        net = EnergyNetwork([a1, a2])
        net.step()
        # After step energy should be conserved approximately
        total_energy = a1.energy + a2.energy
        self.assertAlmostEqual(total_energy, 20, delta=0.0001)


if __name__ == '__main__':
    unittest.main()
