class Command:
    """Simple command pattern implementation."""

    def __init__(self, name: str, action):
        self.name = name
        self.action = action

    def execute(self):
        return self.action()


class HealthMonitor:
    """Track global system health."""

    def __init__(self):
        self.system_health = 100

    def check_system(self) -> str:
        if self.system_health <= 20:
            return "Opozorilo: Nizka stopnja zdravja sistema!"
        if self.system_health <= 50:
            return "Opozorilo: Zdravje sistema je pod 50%."
        return "Sistem deluje normalno."

    def adjust_health(self, change: int) -> None:
        self.system_health = max(0, min(100, self.system_health + change))


class DynamicAdjustment:
    """Adjust agent tension when threshold is exceeded."""

    def __init__(self, threshold: float = 0.7):
        self.threshold = threshold

    def adjust_tension(self, agent, value: float):
        if value > self.threshold:
            agent.update_tension(value)
            return f"Napetost agenta {agent.name} je bila prilagojena na {value}."
        return ""
