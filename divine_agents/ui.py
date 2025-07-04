import tkinter as tk
from tkinter import ttk

from .agent import Agent


def launch_ui() -> None:
    """Launch a simple UI to manipulate an agent's tension and emotion."""
    agent = Agent("UI-Agent")

    root = tk.Tk()
    root.title("Ontološki Agent")

    tension_var = tk.DoubleVar(value=0.0)
    emotion_var = tk.DoubleVar(value=0.0)
    state_var = tk.StringVar(value=f"Stanje: {agent.state}")

    def update(_=None) -> None:
        agent.update_tension(tension_var.get())
        agent.update_emotion(emotion_var.get())
        agent.transition()
        state_var.set(f"Stanje: {agent.state}")

    ttk.Label(root, text="Napetost").pack(pady=5)
    ttk.Scale(root, from_=0, to=1, variable=tension_var, orient="horizontal", command=update).pack(fill="x", padx=10)

    ttk.Label(root, text="Čustvo").pack(pady=5)
    ttk.Scale(root, from_=0, to=1, variable=emotion_var, orient="horizontal", command=update).pack(fill="x", padx=10)

    ttk.Label(root, textvariable=state_var, font=("Helvetica", 14)).pack(pady=10)

    root.mainloop()


__all__ = ["launch_ui"]
