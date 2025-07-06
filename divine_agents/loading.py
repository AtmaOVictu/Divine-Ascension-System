import time
import tkinter as tk
from typing import Callable, Optional


class LoadingScreen:
    """Tkinter-based loading screen using absolute time for progress."""

    def __init__(self, root: Optional[tk.Tk] = None, time_func: Optional[Callable[[], float]] = None) -> None:
        self.root = root
        self.time_func = time_func or time.time
        self.start_time = self.time_func()

        if self.root:
            self.root.title("Loading Screen")
            self.progress_label = tk.Label(self.root, text="Progress: 0%", font=("Helvetica", 16))
            self.progress_label.pack(pady=20)
            self.update_progress()

    def get_progress(self) -> int:
        """Return current progress percentage based on elapsed time."""
        elapsed = self.time_func() - self.start_time
        # Increase by 1 every 0.5 seconds, cycle at 100
        return int(elapsed * 2) % 100

    def update_progress(self) -> int:
        """Update progress label if running with a GUI."""
        progress = self.get_progress()
        if self.root:
            self.progress_label.config(text=f"Progress: {progress}%")
            self.root.after(100, self.update_progress)
        return progress


if __name__ == "__main__":
    root = tk.Tk()
    screen = LoadingScreen(root)
    root.mainloop()
