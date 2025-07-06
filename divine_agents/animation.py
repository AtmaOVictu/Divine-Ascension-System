import tkinter as tk
import time
from typing import Optional

class TimeCycleApp:
    """Tkinter-based animation simulating an infinite time cycle."""

    def __init__(self, root: tk.Tk, steps: int = 360) -> None:
        self.root = root
        self.root.title("Simulacija Ure")
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.outer_circle = self.canvas.create_oval(100, 100, 700, 700, outline="black", width=5)
        self.middle_circle = self.canvas.create_oval(200, 200, 600, 600, outline="black", width=5)
        self.inner_circle = self.canvas.create_oval(300, 300, 500, 500, outline="blue", width=5)

        self.color = "blue"
        self.steps = steps

    @staticmethod
    def cycle_color(step: int, current_color: str) -> str:
        """Return a new color every 60 degrees to illustrate change."""
        if step % 60 == 0:
            return "red" if current_color == "blue" else "blue"
        return current_color

    def animate_circle(self) -> None:
        """Animate the inner circle in an infinite loop."""
        for i in range(self.steps):
            self.canvas.move(self.inner_circle, 1, 0)
            self.color = self.cycle_color(i, self.color)
            self.canvas.itemconfig(self.inner_circle, outline=self.color)
            self.root.update()
            time.sleep(0.01)
        # restart animation for endless effect
        self.animate_circle()


def main(steps: Optional[int] = 360) -> None:
    root = tk.Tk()
    app = TimeCycleApp(root, steps=steps)
    app.animate_circle()
    root.mainloop()


if __name__ == "__main__":
    main()
