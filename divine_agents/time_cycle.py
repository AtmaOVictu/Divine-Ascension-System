import tkinter as tk

from .cycle_model import CycleModel


class TimeCycleApp:
    """Tkinter application that visualizes an infinite time cycle."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Simulacija Ure")
        self.root.geometry("800x600")

        self.model = CycleModel()
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.outer_circle = self.canvas.create_oval(100, 100, 700, 700,
                                                    outline="black", width=5)
        self.middle_circle = self.canvas.create_oval(200, 200, 600, 600,
                                                     outline="black", width=5)
        self.inner_circle = self.canvas.create_oval(300, 300, 500, 500,
                                                    outline=self.model.color,
                                                    width=5)
        self.running = False

    def _step(self):
        angle, color, changed = self.model.step()
        self.canvas.move(self.inner_circle, 1, 0)
        if changed:
            self.canvas.itemconfig(self.inner_circle, outline=color)
        if self.running:
            self.root.after(10, self._step)

    def start(self):
        if not self.running:
            self.running = True
            self._step()

    def stop(self):
        self.running = False
