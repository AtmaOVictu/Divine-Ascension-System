class AuthorBox:
    """Box for defining and isolating an author's identity to prevent syntax delusions."""

    def __init__(self, name: str, role: str = "Author", data: dict | None = None) -> None:
        self.name = name
        self.role = role
        self.data = data.copy() if data else {"identity": "protected"}

    def update_data(self, new_data: dict) -> None:
        """Update the author's data while maintaining identity integrity."""
        self.data.update(new_data)

    def get_identity(self) -> dict:
        """Retrieve the author's identity data."""
        return {"name": self.name, "role": self.role, "data": self.data}

    def __str__(self) -> str:
        return f"Author {self.name} with role {self.role} and data {self.data}"

