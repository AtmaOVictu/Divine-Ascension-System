"""Interactive Tkinter interface for ontological agents."""

from __future__ import annotations

import tkinter as tk
from typing import List

from .agent import Agent
from .dialogue import philosophical_dialogue


class AgentFrame(tk.Frame):
    """Frame widget displaying and controlling a single agent."""

    def __init__(self, master: tk.Misc, agent: Agent, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.agent = agent

        self.state_var = tk.StringVar(value=self.agent.state)
        self.tension_var = tk.DoubleVar(value=self.agent.tension)
        self.emotion_var = tk.DoubleVar(value=self.agent.emotion)

        tk.Label(self, text=agent.name).pack()
        tk.Label(self, textvariable=self.state_var).pack()

        self.tension_scale = tk.Scale(
            self,
            from_=0.0,
            to=1.0,
            resolution=0.01,
            orient=tk.HORIZONTAL,
            label="Tension",
            variable=self.tension_var,
        )
        self.tension_scale.pack()

        self.emotion_scale = tk.Scale(
            self,
            from_=0.0,
            to=1.0,
            resolution=0.01,
            orient=tk.HORIZONTAL,
            label="Emotion",
            variable=self.emotion_var,
        )
        self.emotion_scale.pack()

        tk.Button(self, text="Apply", command=self.apply).pack()

    def apply(self) -> None:
        """Apply slider values and update the agent's state."""
        self.agent.update_tension(self.tension_var.get())
        self.agent.update_emotion(self.emotion_var.get())
        self.agent.transition()
        self.state_var.set(self.agent.state)


def run_interface() -> None:
    """Launch a simple interface with two agents."""
    root = tk.Tk()
    root.title("Agent Evolution Simulator")

    agent1 = Agent("Agent 1")
    agent2 = Agent("Agent 2", state="Jaz")

    frames: List[AgentFrame] = []
    for ag in (agent1, agent2):
        frame = AgentFrame(root, ag, borderwidth=2, relief=tk.GROOVE)
        frame.pack(side=tk.LEFT, padx=10, pady=10)
        frames.append(frame)

    output = tk.Text(root, height=10, width=60)
    output.pack(fill=tk.BOTH, expand=True)

    def step_dialogue() -> None:
        """Perform a dialogue step and display the lines."""
        lines = philosophical_dialogue(agent1, agent2)
        output.insert(tk.END, "\n".join(lines) + "\n")
        for frame in frames:
            frame.state_var.set(frame.agent.state)
            frame.tension_var.set(frame.agent.tension)
            frame.emotion_var.set(frame.agent.emotion)

    tk.Button(root, text="Dialogue Step", command=step_dialogue).pack()

    root.mainloop()


__all__ = ["run_interface", "AgentFrame"]
