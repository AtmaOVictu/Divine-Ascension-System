import time
import tkinter as tk


class LoadingScreen:
    """Display a progress indicator that updates based on absolute time."""

    def __init__(self, root: tk.Tk, duration: float = 5.0) -> None:
        self.root = root
        self.root.title("Loading Screen")
        self.duration = duration
        self.start_time = time.time()
        self.progress_label = tk.Label(root, text="Progress: 0%", font=("Helvetica", 16))
        self.progress_label.pack(pady=20)
        self.update_progress()

    def calculate_progress(self) -> int:
        """Calculate progress percentage based on elapsed time."""
        elapsed = time.time() - self.start_time
        progress = min(int((elapsed / self.duration) * 100), 100)
        return progress

    def update_progress(self) -> None:
        progress = self.calculate_progress()
        self.progress_label.config(text=f"Progress: {progress}%")
        if progress < 100:
            self.root.after(100, self.update_progress)
        else:
            self.root.after(500, self.root.destroy)


if __name__ == "__main__":
    root = tk.Tk()
    LoadingScreen(root)
    root.mainloop()
