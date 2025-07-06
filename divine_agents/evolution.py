from __future__ import annotations

import math
import random
from typing import Callable, Iterable, Tuple


def crossover(parent1: Iterable, parent2: Iterable) -> list:
    """Combine two parents at a random crossover point."""
    parent1 = list(parent1)
    parent2 = list(parent2)
    point = random.randint(0, len(parent1) - 1)
    return parent1[:point] + parent2[point:]


def simulated_annealing(random_solution: Callable[[], Iterable],
                        fitness_function: Callable[[Iterable], float],
                        iterations: int = 1000,
                        temperature: float = 1000.0,
                        cooling_rate: float = 0.95) -> Tuple[Iterable, float]:
    current = random_solution()
    current_fitness = fitness_function(current)
    for _ in range(iterations):
        candidate = random_solution()
        candidate_fitness = fitness_function(candidate)
        if candidate_fitness > current_fitness or random.random() < math.exp((candidate_fitness - current_fitness) / temperature):
            current, current_fitness = candidate, candidate_fitness
        temperature *= cooling_rate
    return current, current_fitness


def hybrid_optimize(genetic_algorithm: Callable[[], Iterable],
                    anneal_random: Callable[[], Iterable],
                    fitness: Callable[[Iterable], float]) -> Tuple[Iterable, float]:
    best = genetic_algorithm()
    return simulated_annealing(anneal_random, fitness)
