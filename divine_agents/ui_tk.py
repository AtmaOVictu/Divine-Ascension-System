import tkinter as tk
from .agent import Agent


class AgentUI:
    """Simple Tkinter UI to interact with a single Agent."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.agent = Agent("UI-Agent")
        self.root.title("Agentni Prehodi")

        tk.Label(root, text="Napetost").pack()
        self.tension = tk.Scale(root, from_=0, to=100, orient="horizontal")
        self.tension.pack()

        tk.Label(root, text="Intenziteta čustev").pack()
        self.emotion = tk.Scale(root, from_=0, to=100, orient="horizontal")
        self.emotion.pack()

        tk.Label(root, text="Vrsta čustva").pack()
        self.emotion_type = tk.Entry(root)
        self.emotion_type.insert(0, "neutral")
        self.emotion_type.pack()

        tk.Button(root, text="Posodobi", command=self.update_agent).pack()
        self.state_label = tk.Label(root, text=f"Trenutno stanje: {self.agent.state}")
        self.state_label.pack()
        self.response_label = tk.Label(root, text="")
        self.response_label.pack()

    def update_agent(self) -> None:
        self.agent.update_tension(self.tension.get() / 100)
        self.agent.update_emotion(
            self.emotion.get() / 100, self.emotion_type.get() or "neutral"
        )
        self.agent.transition()
        self.state_label.config(text=f"Trenutno stanje: {self.agent.state}")
        self.response_label.config(text=self.agent.respond("Kaj je resnica?"))


def run():
    root = tk.Tk()
    AgentUI(root)
    root.mainloop()


if __name__ == "__main__":
    run()
