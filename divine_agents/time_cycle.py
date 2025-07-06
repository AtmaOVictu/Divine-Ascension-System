"""Tkinter-based animations for simulating infinite time cycles."""
from __future__ import annotations

import tkinter as tk
from dataclasses import dataclass


@dataclass
class Circle:
    """Represent a circle on a Tkinter canvas."""
    item: int
    speed: float


class TimeCycleApp:
    """Animate a simple inner circle moving endlessly."""

    def __init__(self, root: tk.Tk, steps: int = 360) -> None:
        self.root = root
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.outer_circle = self.canvas.create_oval(100, 100, 700, 700, outline="black", width=5)
        self.middle_circle = self.canvas.create_oval(200, 200, 600, 600, outline="black", width=5)
        self.inner_circle = self.canvas.create_oval(300, 300, 500, 500, outline="blue", width=5)

        self.current_step = 0
        self.steps = steps
        self.color = "blue"

    def animate_step(self) -> None:
        """Move the inner circle one step and update its color."""
        self.canvas.move(self.inner_circle, 1, 0)
        self.current_step += 1

        if self.current_step % 60 == 0:
            self.color = "red" if self.color == "blue" else "blue"
            self.canvas.itemconfig(self.inner_circle, outline=self.color)

        if self.current_step >= self.steps:
            self.current_step = 0
            self.canvas.coords(self.inner_circle, 300, 300, 500, 500)

    def start(self, delay_ms: int = 10) -> None:
        """Begin the infinite animation loop."""
        self.animate_step()
        self.root.update_idletasks()
        self.root.after(delay_ms, self.start, delay_ms)


class TimeCycleAppExtended(TimeCycleApp):
    """Animate multiple circles with different speeds."""

    def __init__(self, root: tk.Tk, steps: int = 360) -> None:
        super().__init__(root, steps=steps)
        # override circles with additional ones
        self.canvas.delete(self.inner_circle)
        self.canvas.delete(self.middle_circle)
        self.canvas.delete(self.outer_circle)
        self.circles = [
            Circle(self.canvas.create_oval(100, 100, 700, 700, outline="black", width=5), 0.1),
            Circle(self.canvas.create_oval(200, 200, 600, 600, outline="black", width=5), 0.5),
            Circle(self.canvas.create_oval(300, 300, 500, 500, outline="blue", width=5), 1.0),
        ]
        self.color = "blue"

    def animate_step(self) -> None:
        """Move all circles based on their speed."""
        for circle in self.circles:
            self.canvas.move(circle.item, circle.speed, 0)
        self.current_step += 1

        if self.current_step % 60 == 0:
            self.color = "red" if self.color == "blue" else "blue"
            self.canvas.itemconfig(self.circles[-1].item, outline=self.color)

        if self.current_step >= self.steps:
            self.current_step = 0
            # reset positions
            positions = [
                (100, 100, 700, 700),
                (200, 200, 600, 600),
                (300, 300, 500, 500),
            ]
            for circle, coords in zip(self.circles, positions):
                self.canvas.coords(circle.item, *coords)

