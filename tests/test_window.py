import unittest
from divine_agents import window


class TestPythonDetection(unittest.TestCase):
    def test_python_ready(self):
        self.assertTrue(window.is_python_ready((3, 6)))


if __name__ == "__main__":
    unittest.main()
