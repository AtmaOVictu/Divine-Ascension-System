class ModularUnit:
    """Building block that can connect to other units and activate recursively."""

    def __init__(self, unit_name: str, connected_units=None):
        self.unit_name = unit_name
        self.connected_units = connected_units if connected_units else []

    def connect_unit(self, unit: 'ModularUnit') -> None:
        """Connect this unit with another unit if not already connected."""
        if unit not in self.connected_units:
            self.connected_units.append(unit)

    def activate(self) -> list[str]:
        """Activate this unit and its connected units."""
        outputs = [f"{self.unit_name} activated."]
        for unit in self.connected_units:
            outputs.extend(unit.activate())
        return outputs
