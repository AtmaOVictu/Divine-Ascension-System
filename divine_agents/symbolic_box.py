class ExtraSymbolicBox:
    """An extra symbolic box to facilitate necessity and act as a fallback."""

    def __init__(self, stage: str, data: dict | None = None):
        self.stage = stage
        self.data = data or {}
        self.protection_flag = False

    def update_data(self, new_data: dict) -> None:
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot modify data.")
        self.data.update(new_data)

    def set_protection(self, flag: bool) -> None:
        self.protection_flag = flag

    def transition(self, next_stage: str, new_data: dict) -> None:
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot transition.")
        self.stage = next_stage
        self.update_data(new_data)

    def get_data(self) -> dict:
        return self.data

    def __str__(self) -> str:
        return f"Extra box at {self.stage} stage with data: {self.data}"
