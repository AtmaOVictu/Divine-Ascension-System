import unittest
from divine_agents.time_cycle import TimeCycleSimulator


class TestTimeCycleSimulator(unittest.TestCase):
    def test_color_toggle(self):
        sim = TimeCycleSimulator()
        initial_color = sim.color
        for _ in range(60):
            sim.step()
        self.assertNotEqual(sim.color, initial_color)

    def test_full_cycle(self):
        sim = TimeCycleSimulator()
        for _ in range(360):
            state = sim.step()
        self.assertEqual(state.angle, 0)
        self.assertEqual(sim.position, 0)


if __name__ == "__main__":
    unittest.main()
