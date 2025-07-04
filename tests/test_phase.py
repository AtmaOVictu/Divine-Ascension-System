import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.phase import RESPhase, generate_phases
from divine_agents.agent import PhaseModifier


class TestPhaseModification(unittest.TestCase):
    def test_generate_phases_count(self):
        phases = generate_phases()
        self.assertEqual(len(phases), 101)
        self.assertEqual(phases[0].label, "RES000")
        self.assertEqual(phases[-1].label, "RES100")

    def test_phase_transition_with_modifier(self):
        phase = RESPhase("RES001", tension=0.6)
        modifier = PhaseModifier("Mod")
        modifier.modify_phase(phase, new_tension=0.8)
        transitioned = phase.transition()
        self.assertTrue(transitioned)
        self.assertEqual(phase.emotion, "Transformed Emotion")


if __name__ == "__main__":
    unittest.main()
