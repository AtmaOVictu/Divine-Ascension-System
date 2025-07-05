from typing import List, Tuple

try:
    import matplotlib.pyplot as plt
except ImportError:  # pragma: no cover - optional dependency
    plt = None


class TransitionVisualizer:
    """Visualize agent transitions."""

    def __init__(self):
        self.transitions: List[Tuple[str, float]] = []

    def add_transition(self, phase: str, value: float) -> None:
        self.transitions.append((phase, value))

    def plot(self):
        if plt is None:
            raise RuntimeError("matplotlib is required for plotting")
        phases, values = zip(*self.transitions)
        plt.plot(phases, values, marker="o")
        plt.title("Prehodi skozi faze")
        plt.xlabel("Faze")
        plt.ylabel("Vrednost prehoda")
        return plt
