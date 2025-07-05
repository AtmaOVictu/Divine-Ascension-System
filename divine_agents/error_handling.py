class SimpleErrorLogger:
    """A simple error logger that stores error messages."""
    def __init__(self):
        self.errors = []

    def log_error(self, error_message: str) -> None:
        """Record an error message."""
        self.errors.append(error_message)
        print(f"Napaka: {error_message}")

    def show_errors(self) -> None:
        """Display all logged errors."""
        if not self.errors:
            print("Ni napak.")
        else:
            print("Napake:")
            for error in self.errors:
                print(f"- {error}")


from datetime import datetime

class DateErrorLogger(SimpleErrorLogger):
    """Error logger that attaches a timestamp to each error."""
    def log_error(self, error_message: str) -> None:
        error_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"{error_time} - {error_message}"
        self.errors.append(message)
        print(f"Napaka zabeležena: {message}")

