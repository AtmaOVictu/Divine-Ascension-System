import tkinter as tk
from .agent import Agent


class AgentUI:
    """Interactive Tkinter interface for visualizing an Agent."""

    COLOR_MAP = {
        "Ego": "red",
        "Jaz": "yellow",
        "Enotnost": "green",
    }

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.agent = Agent("Agent 1")

        # Canvas showing the agent as a circle
        self.canvas = tk.Canvas(root, width=200, height=200)
        self.canvas.pack(pady=10)
        self.agent_display = self.canvas.create_oval(50, 50, 150, 150, fill=self.COLOR_MAP[self.agent.state])

        # State and metrics labels
        self.state_label = tk.Label(root, text=f"Stanje: {self.agent.state}")
        self.state_label.pack()
        self.tension_label = tk.Label(root, text=f"Napetost: {self.agent.tension:.1f}")
        self.tension_label.pack()
        self.emotion_label = tk.Label(root, text=f"Čustva: {self.agent.emotion:.1f}")
        self.emotion_label.pack()

        # Buttons to manipulate tension and emotion
        tk.Button(root, text="Povečaj napetost", command=self.increase_tension).pack(pady=5)
        tk.Button(root, text="Povečaj čustva", command=self.increase_emotion).pack(pady=5)

        # Entry for phonetic sound triggering state changes
        self.sound_entry = tk.Entry(root)
        self.sound_entry.pack(pady=5)
        tk.Button(root, text="Oddaj zvok", command=self.play_sound).pack(pady=5)

        # Label for philosophical response
        self.response_label = tk.Label(root, text="", wraplength=180)
        self.response_label.pack(pady=10)

    def increase_tension(self) -> None:
        """Increase tension and update the interface."""
        self.agent.update_tension(self.agent.tension + 0.2)
        self._update_state()

    def increase_emotion(self) -> None:
        """Increase emotion and update the interface."""
        self.agent.update_emotion(self.agent.emotion + 0.3)
        self._update_state()

    def play_sound(self) -> None:
        """React to user-entered sound by increasing emotion."""
        sound = self.sound_entry.get().strip()
        if sound:
            self.agent.update_emotion(self.agent.emotion + 0.3)
            self.sound_entry.delete(0, tk.END)
        self._update_state()

    def _update_state(self) -> None:
        """Handle state transition and refresh display."""
        self.agent.transition()
        # Update display elements
        color = self.COLOR_MAP[self.agent.state]
        self.canvas.itemconfig(self.agent_display, fill=color)
        self.state_label.config(text=f"Stanje: {self.agent.state}")
        self.tension_label.config(text=f"Napetost: {self.agent.tension:.1f}")
        self.emotion_label.config(text=f"Čustva: {self.agent.emotion:.1f}")
        self.response_label.config(text=self.agent.respond("Kaj je resnica?"))


def run_app() -> None:
    """Launch the Tkinter UI."""
    root = tk.Tk()
    root.title("Soul Compass")
    AgentUI(root)
    root.mainloop()


if __name__ == "__main__":
    run_app()
