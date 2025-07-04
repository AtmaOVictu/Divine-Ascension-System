"""Interactive transition window for the Divine Agents system."""

import sys
import tkinter as tk

class TransitionWindow:
    """GUI for triggering agent state transitions."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Prehod skozi sistem")
        self.root.geometry("400x200")

        self.label = tk.Label(
            self.root, text="Prehod skozi faze sistema", font=("Helvetica", 16)
        )
        self.label.pack(pady=30)

        self.transition_button = tk.Button(
            self.root, text="Za\u010dni Prehod", command=self.activate_transition
        )
        self.transition_button.pack()

    def activate_transition(self) -> None:
        """Activate transition and open a new window."""
        self.label.config(text="Faza prehoda aktivirana. Sistem se osve\u017euJe...")
        self.root.after(1000, self.create_new_window)

    def create_new_window(self) -> None:
        """Open a secondary window for the user or author."""
        new_window = tk.Toplevel(self.root)
        new_window.title("Novi prehod")
        new_label = tk.Label(
            new_window,
            text="Novo okno za uporabnika ali avtorja.",
            font=("Helvetica", 14),
        )
        new_label.pack(pady=20)
        new_button = tk.Button(new_window, text="Dokon\u010daj", command=new_window.destroy)
        new_button.pack()


def launch() -> None:
    """Launch the transition GUI if Python version is supported."""
    if sys.version_info >= (3, 6):
        root = tk.Tk()
        app = TransitionWindow(root)
        root.mainloop()
    else:
        print("Python ni ustrezno pripravljen za izvedbo tega programa.")


if __name__ == "__main__":
    launch()
