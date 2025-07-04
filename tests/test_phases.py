import unittest
from divine_agents.phases import generate_phases


class TestPhases(unittest.TestCase):
    def test_generate_phases_count(self):
        phases = generate_phases()
        self.assertEqual(len(phases), 103)

    def test_phase_labels(self):
        phases = generate_phases()
        expected = ["RES0", "RES00", "RES000", "RES001", "RES002"]
        self.assertEqual([p.label for p in phases[:5]], expected)


if __name__ == "__main__":
    unittest.main()
