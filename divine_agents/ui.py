import tkinter as tk
from .agent import Agent


class SoulCompassApp:
    """Simple Tkinter UI to visualise agent transitions."""

    COLOR_MAP = {
        "Ego": "red",
        "Jaz": "yellow",
        "Enotnost": "green",
    }

    def __init__(self, root: tk.Tk, agent: Agent | None = None) -> None:
        self.root = root
        self.agent = agent or Agent("Agent 1")

        self.root.title("Soul Compass")
        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack()

        self.display = self.canvas.create_oval(50, 50, 250, 250, fill="red")
        self.text = tk.Label(self.root, text=f"Stanje: {self.agent.state}")
        self.text.pack(pady=10)

        self.tension_btn = tk.Button(self.root, text="Povečaj napetost", command=self.increase_tension)
        self.tension_btn.pack(pady=5)
        self.emotion_btn = tk.Button(self.root, text="Povečaj čustva", command=self.increase_emotion)
        self.emotion_btn.pack(pady=5)

        self.update_visual()

    def increase_tension(self) -> None:
        self.agent.update_tension(self.agent.tension + 0.2)
        self.update_state()

    def increase_emotion(self) -> None:
        self.agent.update_emotion(self.agent.emotion + 0.3)
        self.update_state()

    def update_state(self) -> None:
        self.agent.transition()
        self.update_visual()

    def update_visual(self) -> None:
        color = self.COLOR_MAP.get(self.agent.state, "gray")
        self.canvas.itemconfig(self.display, fill=color)
        self.text.config(text=f"Stanje: {self.agent.state}")


def run_app() -> None:
    """Helper to run the Tkinter app."""
    root = tk.Tk()
    app = SoulCompassApp(root)
    root.mainloop()


__all__ = ["SoulCompassApp", "run_app"]
