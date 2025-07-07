"""Symbolic containers representing stages of an ontological process."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class SymbolicBox:
    """Container holding data at a specific ontological stage."""

    stage: str
    data: Dict[str, Any] = field(default_factory=dict)

    def update(self, **kwargs: Any) -> None:
        """Update data stored in the box."""
        self.data.update(kwargs)

    def __repr__(self) -> str:  # pragma: no cover - representation utility
        return f"SymbolicBox(stage={self.stage!r}, data={self.data!r})"
