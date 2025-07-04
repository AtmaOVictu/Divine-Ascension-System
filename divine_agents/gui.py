import sys
from typing import List

try:
    import tkinter as tk
except Exception:  # Avoid failing import during tests where Tk may not be available
    tk = None

from .agent import Agent


class TransitionWindow:
    """Tkinter window to display agents and trigger state transitions."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents
        self.root = None
        self.labels = []

    def _format_state(self, agent: Agent) -> str:
        return f"{agent.name}: {agent.state}"

    def _on_transition(self, agent: Agent, label):
        agent.transition()
        if hasattr(label, "config"):
            label.config(text=self._format_state(agent))

    def setup(self) -> None:
        if tk is None:
            raise RuntimeError("tkinter is required to run the GUI")
        self.root = tk.Tk()
        self.root.title("Agent Transitions")
        for agent in self.agents:
            frame = tk.Frame(self.root)
            frame.pack(padx=5, pady=5)
            lbl = tk.Label(frame, text=self._format_state(agent))
            lbl.pack(side="left")
            btn = tk.Button(frame, text="Transition", command=lambda a=agent, l=lbl: self._on_transition(a, l))
            btn.pack(side="right")
            self.labels.append(lbl)

    def run(self) -> None:
        self.setup()
        self.root.mainloop()


def launch_gui(agents: List[Agent] | None = None) -> None:
    """Launch the transition GUI if Python version is sufficient."""
    if sys.version_info < (3, 6):
        raise RuntimeError("Python 3.6 or higher is required to run the GUI.")
    if agents is None:
        agents = [Agent("A1"), Agent("A2", state="Jaz")]
    window = TransitionWindow(agents)
    window.run()
