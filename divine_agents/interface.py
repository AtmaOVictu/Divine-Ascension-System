import tkinter as tk
from .agent import Agent
from .dialogue import philosophical_dialogue


class App:
    """Simple Tkinter interface for interacting with two agents."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Agent Evolution Simulation")

        self.agent1 = Agent("Agent 1")
        self.agent2 = Agent("Agent 2", state="Jaz")

        self.state_label1 = tk.Label(root, text=self._agent_text(self.agent1))
        self.state_label1.pack()
        self.state_label2 = tk.Label(root, text=self._agent_text(self.agent2))
        self.state_label2.pack()

        # Sliders for agent1 emotion and tension
        self.emotion1 = tk.Scale(root, from_=0, to=1, resolution=0.01,
                                 orient="horizontal", label="Agent1 Emotion")
        self.emotion1.set(self.agent1.emotion)
        self.emotion1.pack()
        self.tension1 = tk.Scale(root, from_=0, to=1, resolution=0.01,
                                 orient="horizontal", label="Agent1 Tension")
        self.tension1.set(self.agent1.tension)
        self.tension1.pack()

        # Buttons
        tk.Button(root, text="Update Agent1", command=self.update_agent1).pack()
        tk.Button(root, text="Dialogue", command=self.run_dialogue).pack()

        self.dialogue_box = tk.Text(root, height=10, width=60)
        self.dialogue_box.pack()

    def _agent_text(self, agent: Agent) -> str:
        return f"{agent.name}: {agent.state} (t={agent.tension:.2f}, e={agent.emotion:.2f})"

    def update_agent1(self) -> None:
        self.agent1.update_emotion(self.emotion1.get())
        self.agent1.update_tension(self.tension1.get())
        self.agent1.transition()
        self.state_label1.config(text=self._agent_text(self.agent1))

    def run_dialogue(self) -> None:
        lines = philosophical_dialogue(self.agent1, self.agent2)
        self.state_label1.config(text=self._agent_text(self.agent1))
        self.state_label2.config(text=self._agent_text(self.agent2))
        self.dialogue_box.delete("1.0", tk.END)
        self.dialogue_box.insert(tk.END, "\n".join(lines))


def main() -> None:
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
