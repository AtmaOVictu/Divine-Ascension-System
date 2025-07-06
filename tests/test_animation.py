import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.animation import TimeCycleApp

class TestTimeCycleApp(unittest.TestCase):
    def test_cycle_color_switch(self):
        color = "blue"
        color = TimeCycleApp.cycle_color(60, color)
        self.assertEqual(color, "red")
        color = TimeCycleApp.cycle_color(120, color)
        self.assertEqual(color, "blue")

if __name__ == '__main__':
    unittest.main()
