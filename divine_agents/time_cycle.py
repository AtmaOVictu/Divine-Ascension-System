"""Simulation utilities for displaying a circular loading animation."""

from dataclasses import dataclass


@dataclass
class TimeCycleState:
    """Simple data structure representing the state of the time cycle."""
    position: int
    angle: int
    color: str


class TimeCycleSimulator:
    """Logic-only simulator for an endless time cycle animation."""

    def __init__(self, width: int = 360):
        self.width = width
        self.position = 0
        self.angle = 0
        self.color = "blue"

    def step(self) -> TimeCycleState:
        """Advance the simulation by one step and return the new state."""
        self.position = (self.position + 1) % self.width
        self.angle = (self.angle + 1) % 360
        if self.angle % 60 == 0:
            self.color = "red" if self.color == "blue" else "blue"
        return TimeCycleState(self.position, self.angle, self.color)


try:
    import tkinter as tk
except Exception:  # pragma: no cover - if tkinter is unavailable
    tk = None


class TimeCycleApp:
    """Tkinter GUI that visualizes the :class:`TimeCycleSimulator`."""

    def __init__(self, root: "tk.Tk", simulator: TimeCycleSimulator | None = None):
        if tk is None:
            raise RuntimeError("Tkinter is required for TimeCycleApp")
        self.root = root
        self.simulator = simulator or TimeCycleSimulator()
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.inner_circle = self.canvas.create_oval(300, 300, 500, 500, outline=self.simulator.color, width=5)
        self.animate()

    def animate(self) -> None:
        state = self.simulator.step()
        self.canvas.move(self.inner_circle, 1, 0)
        self.canvas.itemconfig(self.inner_circle, outline=state.color)
        self.root.after(10, self.animate)
