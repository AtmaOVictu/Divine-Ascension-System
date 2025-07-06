"""Simple Tkinter-based UI for visualizing Agent state transitions."""

from tkinter import Tk, Canvas, Button, Label

from .agent import Agent


COLOR_MAP = {
    "Ego": "red",
    "Jaz": "yellow",
    "Enotnost": "green",
}


class SoulCompassApp:
    """Graphical interface for interacting with a single Agent."""

    def __init__(self, root: Tk, agent: Agent | None = None) -> None:
        self.root = root
        self.root.title("Soul Compass")
        self.root.geometry("800x600")

        self.agent = agent or Agent("Agent 1")

        # Canvas for visualization
        self.canvas = Canvas(self.root, width=800, height=400)
        self.canvas.pack()
        self.agent_display = self.canvas.create_oval(50, 50, 150, 150, fill=COLOR_MAP[self.agent.state])

        # Label for textual state
        self.text_display = Label(self.root, text=f"Stanje: {self.agent.state}", font=("Helvetica", 14))
        self.text_display.pack(pady=20)

        # Controls
        self.tension_button = Button(self.root, text="Povečaj napetost", command=self.increase_tension)
        self.tension_button.pack(pady=10)
        self.emotion_button = Button(self.root, text="Povečaj čustva", command=self.increase_emotion)
        self.emotion_button.pack(pady=10)

    # Logic -----------------------------------------------------------------
    def increase_tension(self) -> None:
        """Increase agent tension and update UI."""
        self.agent.update_tension(self.agent.tension + 0.2)
        self.update_agent_state()

    def increase_emotion(self) -> None:
        """Increase agent emotion and update UI."""
        self.agent.update_emotion(self.agent.emotion + 0.3)
        self.update_agent_state()

    def update_agent_state(self) -> None:
        """Transition agent if thresholds are met and refresh visualization."""
        new_state = self.agent.transition()
        self.text_display.config(text=f"Stanje: {new_state}")
        self.canvas.itemconfig(self.agent_display, fill=COLOR_MAP[new_state])


def main() -> None:
    """Run the UI if executed as a script."""
    root = Tk()
    app = SoulCompassApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
