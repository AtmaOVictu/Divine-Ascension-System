"""Simple Tkinter interface to interact with ontological agents in real time."""

from __future__ import annotations

import tkinter as tk
from typing import Dict

from .agent import Agent


class AgentFrame(tk.Frame):
    """Widget representing an agent with controls for emotions and actions."""

    def __init__(self, master: tk.Misc, agent: Agent) -> None:
        super().__init__(master)
        self.agent = agent
        self._build_widgets()
        self.update_view()

    def _build_widgets(self) -> None:
        self.state_var = tk.StringVar()
        self.tension_var = tk.StringVar()

        tk.Label(self, text=self.agent.name, font=("Arial", 12, "bold")).pack()
        tk.Label(self, textvariable=self.state_var).pack()
        tk.Label(self, textvariable=self.tension_var).pack()

        self.scales: Dict[str, tk.Scale] = {}
        for emotion in self.agent.emotions:
            var = tk.DoubleVar(value=self.agent.emotions[emotion])
            scale = tk.Scale(
                self,
                from_=0,
                to=1,
                resolution=0.01,
                orient="horizontal",
                label=emotion.capitalize(),
                variable=var,
                command=lambda v, e=emotion: self._set_emotion(e, float(v)),
            )
            scale.pack(fill="x")
            self.scales[emotion] = scale

        tk.Button(self, text="Transition", command=self._transition).pack(pady=4)

    def _set_emotion(self, emotion: str, value: float) -> None:
        self.agent.update_emotion(emotion, value)
        self.update_view()

    def _transition(self) -> None:
        self.agent.transition()
        self.update_view()

    def update_view(self) -> None:
        self.state_var.set(f"State: {self.agent.state}")
        self.tension_var.set(f"Tension: {self.agent.tension:.2f}")


class App(tk.Tk):
    """Main window for interacting with multiple agents."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Agent Evolution Simulation")
        self.agent1 = Agent("Agent 1")
        self.agent2 = Agent("Agent 2", state="Jaz")
        AgentFrame(self, self.agent1).pack(side="left", padx=10, pady=10)
        AgentFrame(self, self.agent2).pack(side="right", padx=10, pady=10)


if __name__ == "__main__":
    App().mainloop()
