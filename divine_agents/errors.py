class SimpleErrorLogger:
    """Basic error logger storing messages in memory."""

    def __init__(self) -> None:
        self.errors = []

    def log_error(self, message: str) -> None:
        self.errors.append(message)
        print(f"Napaka: {message}")

    def show_errors(self) -> None:
        if not self.errors:
            print("Ni napak.")
        else:
            print("Napake:")
            for error in self.errors:
                print(f"- {error}")
