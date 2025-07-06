import time
import tkinter as tk


def calculate_progress(start_time: float, current_time: float | None = None) -> int:
    """Return progress percentage based on absolute time.

    Args:
        start_time: Unix timestamp marking the beginning of the progress.
        current_time: Optional current Unix time. Defaults to ``time.time()``.

    Returns:
        Integer progress value in the range 0-99.
    """
    if current_time is None:
        current_time = time.time()
    elapsed = current_time - start_time
    return int(elapsed % 100)


class LoadingScreen:
    """Tkinter based loading screen that updates with absolute time."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Loading Screen")
        self.progress_label = tk.Label(root, text="Progress: 0%", font=("Helvetica", 16))
        self.progress_label.pack(pady=20)
        self.start_time = time.time()
        self.progress = 0
        self.update_progress()

    def update_progress(self) -> None:
        """Update the displayed progress based on absolute time."""
        self.progress = calculate_progress(self.start_time)
        self.progress_label.config(text=f"Progress: {self.progress}%")
        self.root.after(100, self.update_progress)
