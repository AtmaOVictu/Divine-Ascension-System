"""Utilities for managing and distributing tasks (Kraks)."""
from __future__ import annotations

import random
import time
from dataclasses import dataclass, field
from typing import List


@dataclass
class Krak:
    """Represents a single task that can be triggered."""

    name: str
    condition: str
    status: str = "pending"
    timestamp: float = field(default_factory=time.time)

    def activate(self) -> str:
        """Activate the krak if it's pending."""
        if self.status == "pending":
            self.status = "in-progress"
            self.timestamp = time.time()
            return f"Krak {self.name} activated"
        return f"Krak {self.name} is already {self.status}"

    def complete(self) -> str:
        """Mark the krak as completed."""
        self.status = "completed"
        self.timestamp = time.time()
        return f"Krak {self.name} completed"


class GitHubHandler:
    """Simulate task tracking on GitHub."""

    def __init__(self, repository_url: str) -> None:
        self.repository_url = repository_url

    def commit_task(self, task: Krak) -> str:
        """Simulate committing a task to GitHub."""
        return f"Task {task.name} committed to {self.repository_url}"

    def update_task_status(self, task: Krak) -> str:
        """Simulate updating task status on GitHub."""
        return f"Status of {task.name} set to {task.status}"


class VercelHandler:
    """Simulate serverless execution via Vercel."""

    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint

    def trigger_task(self, task: Krak) -> str:
        """Trigger task execution. Returns simulated response."""
        payload = {
            "task_name": task.name,
            "status": task.status,
            "timestamp": time.time(),
        }
        # In real usage this would call requests.post(self.endpoint, json=payload)
        # For tests and offline execution we simply return a string
        return f"Triggered {payload['task_name']} at {self.endpoint}"


class KrakManager:
    """Manage and distribute kraks to agents."""

    def __init__(self, repo_url: str, vercel_endpoint: str) -> None:
        self.kraks: List[Krak] = []
        self.github_handler = GitHubHandler(repo_url)
        self.vercel_handler = VercelHandler(vercel_endpoint)

    def add_krak(self, krak: Krak) -> None:
        """Add a krak and record it to GitHub."""
        self.kraks.append(krak)
        self.github_handler.commit_task(krak)

    def distribute_krak(self) -> str:
        """Activate and trigger a krak if conditions are met."""
        for krak in self.kraks:
            if krak.status == "pending" and random.random() > 0.5:
                activation_message = krak.activate()
                self.vercel_handler.trigger_task(krak)
                self.github_handler.update_task_status(krak)
                return f"Distributed {krak.name}: {activation_message}"
        return "No kraks to distribute"
