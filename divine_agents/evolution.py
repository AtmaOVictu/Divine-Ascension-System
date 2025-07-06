import math
import random


def crossover(parent1: str, parent2: str) -> str:
    """Combine two parent states using a simple crossover."""
    point = random.randint(0, len(parent1))
    return parent1[:point] + parent2[point:]


def simulated_annealing(fitness_func, random_solution):
    """Basic simulated annealing implementation."""
    current = random_solution()
    current_fitness = fitness_func(current)
    temperature = 1000
    cooling = 0.95

    for _ in range(100):
        candidate = random_solution()
        candidate_fitness = fitness_func(candidate)
        if candidate_fitness > current_fitness or random.random() < math.exp((candidate_fitness - current_fitness) / temperature):
            current = candidate
            current_fitness = candidate_fitness
        temperature *= cooling
    return current, current_fitness


def hybrid_algorithm(genetic_func, fitness_func, random_solution):
    """Use GA to explore then SA to refine."""
    best = genetic_func()
    final, fit = simulated_annealing(fitness_func, random_solution)
    return final
