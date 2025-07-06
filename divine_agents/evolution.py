"""Evolutionary algorithms used to evolve agent behaviour."""

from __future__ import annotations

import math
import random


def crossover(parent1: list, parent2: list) -> list:
    """Combine two parents using a simple crossover operation."""
    if not parent1 or not parent2:
        return []
    point = random.randint(0, len(parent1) - 1)
    return parent1[:point] + parent2[point:]


def random_solution(length: int = 5) -> list:
    """Generate a random solution vector."""
    return [random.random() for _ in range(length)]


def fitness_function(solution: list) -> float:
    """Evaluate solution fitness."""
    return sum(solution)


def simulated_annealing(iterations: int = 1000) -> tuple[list, float]:
    """Perform a simple simulated annealing search."""
    current = random_solution()
    current_fit = fitness_function(current)
    temperature = 1000.0
    cooling_rate = 0.95
    for _ in range(iterations):
        new = random_solution()
        new_fit = fitness_function(new)
        if new_fit > current_fit or random.random() < math.exp((new_fit - current_fit) / temperature):
            current, current_fit = new, new_fit
        temperature *= cooling_rate
    return current, current_fit


def genetic_algorithm(population_size: int = 10, generations: int = 10) -> list:
    """Run a minimal genetic algorithm returning the best solution."""
    population = [random_solution() for _ in range(population_size)]
    for _ in range(generations):
        population = sorted(population, key=fitness_function, reverse=True)
        next_generation = population[:2]
        while len(next_generation) < population_size:
            p1, p2 = random.sample(population[:5], 2)
            child = crossover(p1, p2)
            next_generation.append(child)
        population = next_generation
    return max(population, key=fitness_function)


def hybrid_algorithm() -> list:
    """Combine genetic algorithm with simulated annealing for refinement."""
    best = genetic_algorithm()
    final, _ = simulated_annealing()
    return final
