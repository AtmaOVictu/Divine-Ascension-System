import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.ontoscience_box import (
    OntoscienceBox,
    initialize_agents,
    recursive_evolution,
    transition_function,
)


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertEqual(a1.state, "Jaz")
        self.assertEqual(a2.state, "Enotnost")

    def test_box_functions(self):
        matrix = initialize_agents(3)
        self.assertEqual(len(matrix), 3)
        evolved = recursive_evolution(matrix, iterations=1)
        self.assertEqual(len(evolved), 3)

        state = [1.0, 0.0, 0.0]
        trans = [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]
        new_state = transition_function(state, trans)
        self.assertEqual(len(new_state), 3)

    def test_ontoscience_box(self):
        box = OntoscienceBox(2, iterations=1)
        original = box.get_agent_states()
        evolved = box.evolve_agents()
        self.assertEqual(len(evolved), len(original))


if __name__ == '__main__':
    unittest.main()
