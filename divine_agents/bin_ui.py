"""Simple Tkinter UI for interacting with an agent's trash bin."""

import tkinter as tk
from .agent import AgentWithBin


class TrashBinUI:
    """Tkinter interface for managing a trash bin."""

    def __init__(self, root: tk.Tk, agent: AgentWithBin) -> None:
        self.root = root
        self.agent = agent
        self.root.title(f"Smetišče agenta {self.agent.name}")

        self.status = tk.Label(root, text="Smetišče je prazno.")
        self.status.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()
        tk.Button(root, text="Dodaj", command=self.add_item).pack()

        self.remove_entry = tk.Entry(root)
        self.remove_entry.pack()
        tk.Button(root, text="Odstrani", command=self.remove_item).pack()

    def add_item(self) -> None:
        item = self.entry.get()
        if item:
            self.agent.discard(item)
            self.entry.delete(0, tk.END)
            self.update_status()

    def remove_item(self) -> None:
        item = self.remove_entry.get()
        if item:
            self.agent.restore(item)
            self.remove_entry.delete(0, tk.END)
            self.update_status()

    def update_status(self) -> None:
        content = ", ".join(self.agent.trash_bin.view())
        text = f"Vsebina: {content}" if content else "Smetišče je prazno."
        self.status.config(text=text)
