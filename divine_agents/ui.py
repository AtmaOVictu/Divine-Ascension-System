import tkinter as tk
from .agent import Agent

STATE_COLORS = {
    "Ego": "red",
    "Jaz": "yellow",
    "Enotnost": "green",
}


class SoulCompassApp:
    """Interactive UI for visualizing and manipulating an :class:`Agent`."""

    def __init__(self, root: tk.Tk | None = None, agent: Agent | None = None,
                 enable_ui: bool = True) -> None:
        """Create the application.

        Parameters
        ----------
        root:
            Optional Tk root. If ``enable_ui`` is ``True`` and ``root`` is
            ``None``, a new ``tk.Tk`` instance will be created. When running in
            headless mode (``enable_ui=False``) no UI elements are created.
        agent:
            Optional :class:`Agent` instance to control.
        enable_ui:
            If ``False``, the UI elements are not created which allows the class
            to be used in a headless environment such as the test suite.
        """

        self.enable_ui = enable_ui
        self.root = root if root is not None else (tk.Tk() if enable_ui else None)
        self.agent = agent if agent else Agent("Agent 1", state="Ego")

        if self.enable_ui:
            self.root.title("Soul Compass")

            self.canvas = tk.Canvas(self.root, width=800, height=600)
            self.canvas.pack()

            self.agent_display = self.canvas.create_oval(
                50, 50, 150, 150, fill=STATE_COLORS[self.agent.state]
            )
            self.text_display = tk.Label(
                self.root, text=f"Stanje: {self.agent.state}", font=("Helvetica", 14)
            )
            self.text_display.pack(pady=20)

            self.tension_button = tk.Button(
                self.root, text="Pove\u010daj napetost", command=self.increase_tension
            )
            self.tension_button.pack(pady=10)

            self.emotion_button = tk.Button(
                self.root, text="Pove\u010daj \u010dustva", command=self.increase_emotion
            )
            self.emotion_button.pack(pady=10)
        else:
            # Attributes used in update_agent_state so that method can be called
            # safely when UI is disabled.
            self.canvas = None
            self.agent_display = None
            self.text_display = None

    def increase_tension(self, delta: float = 0.2) -> None:
        """Increase agent tension and update state."""
        self.agent.update_tension(self.agent.tension + delta)
        self.update_agent_state()

    def increase_emotion(self, delta: float = 0.3) -> None:
        """Increase agent emotion and update state."""
        self.agent.update_emotion(self.agent.emotion + delta)
        self.update_agent_state()

    def update_agent_state(self) -> None:
        """Transition the agent if thresholds are met and refresh display."""
        state = self.agent.transition()
        if self.enable_ui:
            self.text_display.config(text=f"Stanje: {state}")
            self.canvas.itemconfig(self.agent_display, fill=STATE_COLORS[state])

    def run(self) -> None:
        """Start the Tkinter event loop if UI is enabled."""
        if self.enable_ui:
            self.root.mainloop()
