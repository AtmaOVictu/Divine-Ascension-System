from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List


@dataclass
class AuditRecord:
    """Represents a transition record for SymbolicBox."""
    timestamp: datetime
    old_state: str
    new_state: str
    emotion: float
    tension: float


class SymbolicBox:
    """A symbolic container for state transitions with an audit trail."""

    def __init__(self, stage: str, data: Dict[str, Any] | None = None,
                 emotion: float = 0.0, tension: float = 0.0) -> None:
        self.stage = stage
        self.data = data or {}
        self.emotion = emotion
        self.tension = tension
        self.protection_flag = False
        self.audit_trail: List[AuditRecord] = []

    def update_data(self, new_data: Dict[str, Any]) -> None:
        """Update the internal data if not protected."""
        if self.protection_flag:
            raise PermissionError("Cannot modify data, the box is protected.")
        self.data.update(new_data)

    def set_protection(self, flag: bool) -> None:
        """Enable or disable protection."""
        self.protection_flag = flag

    def transition(self, next_stage: str, new_data: Dict[str, Any] | None = None,
                   emotion: float | None = None, tension: float | None = None) -> str:
        """Transition to the next stage and record an audit entry."""
        if self.protection_flag:
            raise PermissionError("Cannot transition, the box is protected.")
        old_state = self.stage
        if new_data:
            self.update_data(new_data)
        if emotion is not None:
            self.emotion = emotion
        if tension is not None:
            self.tension = tension
        self.stage = next_stage
        self.audit_trail.append(
            AuditRecord(
                timestamp=datetime.utcnow(),
                old_state=old_state,
                new_state=next_stage,
                emotion=self.emotion,
                tension=self.tension,
            )
        )
        return self.stage

    def get_audit_trail(self) -> List[AuditRecord]:
        """Return the audit trail for inspection."""
        return self.audit_trail
