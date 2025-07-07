class XPSystem:
    """Simple XP tracking system with progress visualization."""

    def __init__(self, max_xp: int = 100) -> None:
        self.xp = 0
        self.max_xp = max_xp

    def add_xp(self, amount: int) -> None:
        """Increase XP by amount, not exceeding max_xp."""
        self.xp = min(self.xp + amount, self.max_xp)

    @property
    def percentage(self) -> float:
        return (self.xp / self.max_xp) * 100

    def progress_bar(self, length: int = 10) -> str:
        """Return a textual progress bar representing XP."""
        filled = int(self.percentage // (100 / length))
        bar = "█" * filled + " " * (length - filled)
        return f"[{bar}] {self.percentage:.1f}%"
