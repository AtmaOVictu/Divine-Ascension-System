import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from divine_agents.loading_screen import LoadingScreen
import tkinter as tk


@unittest.skipIf(os.environ.get('DISPLAY', '') == '', 'Requires display')
class TestLoadingScreen(unittest.TestCase):
    def test_calculate_progress(self):
        root = tk.Tk()
        root.withdraw()
        screen = LoadingScreen(root, duration=1.0)
        screen.start_time -= 0.5
        progress = screen.calculate_progress()
        self.assertTrue(40 <= progress <= 60)
        root.destroy()


if __name__ == '__main__':
    unittest.main()
