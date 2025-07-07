class SpaceTimeBox:
    """Simulate space-time with a box tracking stage, coordinates and time."""
    def __init__(self, stage: str, data: dict | None = None, coordinates: dict | None = None):
        self.stage = stage
        self.data = data or {}
        self.coordinates = coordinates or {"x": 0, "y": 0, "z": 0}
        self.time = 0
        self.protection_flag = False

    def update_coordinates(self, x: float, y: float, z: float) -> None:
        """Update spatial coordinates."""
        self.coordinates = {"x": x, "y": y, "z": z}

    def update_time(self, delta_time: float) -> None:
        """Advance the time variable."""
        self.time += delta_time

    def transition(self, next_stage: str, new_data: dict | None = None) -> None:
        """Move to the next stage while updating time and coordinates."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot transition.")
        self.stage = next_stage
        self.update_time(1)
        self.update_coordinates(
            self.coordinates["x"] + 1,
            self.coordinates["y"],
            self.coordinates["z"],
        )
        if new_data:
            self.data.update(new_data)

    def get_state(self) -> dict:
        """Return the current state of the space-time box."""
        return {
            "stage": self.stage,
            "coordinates": self.coordinates,
            "time": self.time,
            "data": self.data,
        }

    def __str__(self) -> str:
        return (
            f"Space-Time Box at {self.stage} with coordinates {self.coordinates} "
            f"and time {self.time}."
        )
