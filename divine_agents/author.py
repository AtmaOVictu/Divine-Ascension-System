class AuthorBox:
    """Box for defining and isolating an author's identity."""

    def __init__(
        self, name: str, role: str = "Author", data: dict | None = None
    ) -> None:
        self.name = name
        self.role = role
        self.data = data.copy() if data else {"identity": "protected"}

    def update_data(self, new_data: dict) -> None:
        """Update the author's data while keeping identity consistent."""
        self.data.update(new_data)

    def get_identity(self) -> dict:
        """Return a dictionary representing the author's boxed identity."""
        return {"name": self.name, "role": self.role, "data": self.data}

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return f"Author {self.name} with role {self.role} and data {self.data}"
