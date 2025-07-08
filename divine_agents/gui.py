import tkinter as tk
from .agent import Agent
from .dialogue import philosophical_dialogue


class AgentGUI:
    """Tkinter interface for interacting with two agents in real time."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Agent Evolution Simulation")

        # create agents
        self.agent1 = Agent("Agent 1")
        self.agent2 = Agent("Agent 2", state="Jaz")

        # display areas
        self.dialog = tk.Text(root, height=10, width=60)
        self.dialog.pack()

        self.a1_label = tk.Label(root)
        self.a1_label.pack()
        self.a2_label = tk.Label(root)
        self.a2_label.pack()

        # sliders for emotion
        self.e1_slider = tk.Scale(root, from_=0, to=1, resolution=0.01,
                                  orient="horizontal", label="Agent1 Emotion",
                                  command=lambda v: self.set_emotion(self.agent1, v))
        self.e1_slider.pack()
        self.e2_slider = tk.Scale(root, from_=0, to=1, resolution=0.01,
                                  orient="horizontal", label="Agent2 Emotion",
                                  command=lambda v: self.set_emotion(self.agent2, v))
        self.e2_slider.pack()

        # buttons
        self.interact_button = tk.Button(root, text="Interact", command=self.interact)
        self.interact_button.pack()

        self.force_button = tk.Button(root, text="Force Evolution", command=self.force_evolution)
        self.force_button.pack()

        self.update_labels()

    def set_emotion(self, agent: Agent, value: float) -> None:
        agent.update_emotion(float(value))
        self.update_labels()

    def force_evolution(self) -> None:
        """Force both agents to evolve to the next state."""
        for ag in (self.agent1, self.agent2):
            if ag.state == "Ego":
                ag.state = "Jaz"
            elif ag.state == "Jaz":
                ag.state = "Enotnost"
        self.update_labels()

    def interact(self) -> None:
        lines = philosophical_dialogue(self.agent1, self.agent2)
        self.dialog.delete("1.0", tk.END)
        self.dialog.insert(tk.END, "\n".join(lines))
        self.update_labels()

    def update_labels(self) -> None:
        self.a1_label.config(text=f"Agent1 - State: {self.agent1.state}, Emotion: {self.agent1.emotion:.2f}, Tension: {self.agent1.tension:.2f}")
        self.a2_label.config(text=f"Agent2 - State: {self.agent2.state}, Emotion: {self.agent2.emotion:.2f}, Tension: {self.agent2.tension:.2f}")


def main() -> None:
    root = tk.Tk()
    gui = AgentGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
