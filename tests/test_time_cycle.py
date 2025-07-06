import unittest
import tkinter as tk
from tkinter import TclError
from divine_agents.time_cycle import TimeCycleApp


class TestTimeCycleApp(unittest.TestCase):
    def test_color_toggle(self):
        try:
            root = tk.Tk()
            root.withdraw()
        except TclError:
            self.skipTest("Tk unavailable")
            return
        app = TimeCycleApp(root, steps=120)
        for _ in range(60):
            app.animate_step()
        self.assertEqual(app.color, "red")
        for _ in range(60):
            app.animate_step()
        self.assertEqual(app.color, "blue")
        root.destroy()


if __name__ == "__main__":
    unittest.main()
