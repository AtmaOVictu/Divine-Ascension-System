import sys
import tkinter as tk


def is_python_ready(min_version=(3, 6)) -> bool:
    """Check if the running Python version meets the minimum requirement."""
    return sys.version_info >= min_version


class TransitionWindow:
    """Simple Tkinter window that creates an additional window on demand."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Prehod skozi sistem")
        self.root.geometry("400x200")
        self.label = tk.Label(self.root, text="Prehod skozi faze sistema", font=("Helvetica", 16))
        self.label.pack(pady=30)
        self.transition_button = tk.Button(self.root, text="Za\u010dni Prehod", command=self.activate_transition)
        self.transition_button.pack()

    def activate_transition(self):
        """Activate state transition and create a new window after a delay."""
        self.label.config(text="Faza prehoda aktivirana. Sistem se osve\u017euje...")
        self.root.after(1000, self.create_new_window)

    def create_new_window(self):
        """Open an additional window for the user or author."""
        new_window = tk.Toplevel(self.root)
        new_window.title("Novi prehod")
        new_label = tk.Label(new_window, text="Novo okno za uporabnika ali avtorja.", font=("Helvetica", 14))
        new_label.pack(pady=20)
        new_button = tk.Button(new_window, text="Dokon\u010daj", command=new_window.destroy)
        new_button.pack()

    def run(self):
        """Start the Tkinter main loop."""
        self.root.mainloop()


def open_transition_window() -> None:
    """Open the transition window if Python is ready."""
    if is_python_ready():
        win = TransitionWindow()
        win.run()
    else:
        raise RuntimeError("Python ni ustrezno pripravljen za izvedbo programa.")
