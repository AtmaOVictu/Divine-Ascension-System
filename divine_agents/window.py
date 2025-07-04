import sys
from typing import Optional

try:
    import tkinter as tk
except Exception:  # pragma: no cover - Tkinter may not be available
    tk = None


class TransitionWindow:
    """Create a transition window for user interaction.

    Parameters
    ----------
    headless : bool, optional
        When True, no graphical elements are created. Useful for testing or
        environments without a display.
    root : Optional[tk.Tk], optional
        Existing Tk root. Only used when headless is False.
    """

    def __init__(self, headless: bool = False, root: Optional["tk.Tk"] = None):
        self.headless = headless or tk is None
        self.transition_active = False
        self.new_window_created = False
        if not self.headless:
            self.root = root or tk.Tk()
            self.root.title("Prehod skozi sistem")
            self.root.geometry("400x200")

            self.label = tk.Label(
                self.root,
                text="Prehod skozi faze sistema",
                font=("Helvetica", 16),
            )
            self.label.pack(pady=30)

            self.transition_button = tk.Button(
                self.root, text="Za\u010dni Prehod", command=self.activate_transition
            )
            self.transition_button.pack()
        else:
            self.label_text = "Prehod skozi faze sistema"

    def activate_transition(self) -> None:
        """Activate the transition and create a new window."""
        self.transition_active = True
        if self.headless:
            self.label_text = "Faza prehoda aktivirana. Sistem se osve\u017euje..."
            self.create_new_window()
        else:
            self.label.config(text="Faza prehoda aktivirana. Sistem se osve\u017euje...")
            # schedule creation after delay to mimic UI behaviour
            self.root.after(1000, self.create_new_window)

    def create_new_window(self) -> None:
        """Create a new window for the user or author."""
        self.new_window_created = True
        if not self.headless:
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

    def run(self) -> None:
        """Start the Tk main loop if not in headless mode."""
        if not self.headless:
            self.root.mainloop()


__all__ = ["TransitionWindow"]
