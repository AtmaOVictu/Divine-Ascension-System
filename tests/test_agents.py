import os
import sys
import unittest
import random

# Ensure package can be imported when running tests directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.advanced_agent import MultiLayeredAgent
from divine_agents.emotional_dynamics import EmotionalTensionDynamics
from divine_agents.evolution import crossover, simulated_annealing


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


class TestAdvancedAgent(unittest.TestCase):
    def test_multi_layer_transition_loyalty(self):
        agent = MultiLayeredAgent("B", state="Jaz", loyalty=0.9, experiences=["selfish"])
        state = agent.multi_layer_transition()
        self.assertEqual(state, "Enotnost")

    def test_emotional_adjustment(self):
        agent = MultiLayeredAgent("C", emotion_label="angry")
        dynamics = EmotionalTensionDynamics(agent)
        dynamics.adjust_tension()
        self.assertGreater(agent.tension, 0.0)


class TestEvolutionaryAlgorithms(unittest.TestCase):
    def test_crossover_length(self):
        child = crossover("ABCDE", "12345")
        self.assertEqual(len(child), 5)

    def test_simulated_annealing_runs(self):
        def random_solution():
            return [random.randint(0, 1) for _ in range(4)]

        def fitness(sol):
            return sum(sol)

        solution, score = simulated_annealing(random_solution, fitness, iterations=10)
        self.assertIsNotNone(solution)
        self.assertIsInstance(score, (int, float))


if __name__ == '__main__':
    unittest.main()
