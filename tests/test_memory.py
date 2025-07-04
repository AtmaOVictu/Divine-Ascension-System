import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.memory import MemorySystem


class TestMemorySystem(unittest.TestCase):
    def test_update_and_history(self):
        mem = MemorySystem()
        mem.update("Ego")
        mem.update("Jaz", transition_type="tension")
        self.assertEqual(mem.current_state, "Jaz")
        self.assertEqual(mem.get_all_history(), ["Ego"])
        self.assertEqual(mem.get_all_transitions(), ["tension"])

    def test_revert(self):
        mem = MemorySystem()
        mem.update("Ego")
        mem.update("Jaz")
        state = mem.revert()
        self.assertEqual(state, "Ego")
        self.assertEqual(mem.current_state, "Ego")


if __name__ == "__main__":
    unittest.main()

