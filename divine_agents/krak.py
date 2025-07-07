"""Krak management system for task distribution.

This module provides simple classes to represent tasks (Kraks) and
to simulate their distribution through GitHub and Vercel. Network
operations are mocked via urllib.request so the system remains
self-contained and testable.
"""

from __future__ import annotations

import json
import random
import time
from dataclasses import dataclass, field
from typing import List
from urllib import request


@dataclass
class Krak:
    """Represents a task to be executed by an agent."""

    name: str
    condition: str
    status: str = "pending"
    timestamp: float = field(default_factory=time.time)

    def activate(self) -> str:
        """Activate the task if it is still pending."""
        if self.status == "pending":
            self.status = "in-progress"
            self.timestamp = time.time()
            return (
                f"Krak {self.name} activated at "
                f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.timestamp))}"
            )
        return f"Krak {self.name} is already active."

    def complete(self) -> str:
        """Mark the task as completed."""
        self.status = "completed"
        self.timestamp = time.time()
        return (
            f"Krak {self.name} completed at "
            f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.timestamp))}"
        )


class GitHubHandler:
    """Simulate interaction with a GitHub repository."""

    def __init__(self, repository_url: str):
        self.repository_url = repository_url

    def commit_task(self, task: Krak) -> str:
        print(f"Committing Krak {task.name} to GitHub repository: {self.repository_url}")
        return f"Task {task.name} committed to GitHub."

    def update_task_status(self, task: Krak) -> str:
        print(f"Updating status of Krak {task.name} on GitHub to {task.status}.")
        return f"Status of {task.name} updated to {task.status}."


class VercelHandler:
    """Simulate triggering serverless execution via Vercel."""

    def __init__(self, vercel_endpoint: str):
        self.vercel_endpoint = vercel_endpoint

    def trigger_task(self, task: Krak) -> str:
        payload = json.dumps(
            {
                "task_name": task.name,
                "status": task.status,
                "timestamp": time.time(),
            }
        ).encode()
        req = request.Request(
            self.vercel_endpoint, data=payload, headers={"Content-Type": "application/json"}
        )
        try:
            with request.urlopen(req) as resp:
                return resp.read().decode()
        except Exception as exc:  # pragma: no cover - network errors ignored in tests
            return f"Failed to trigger task: {exc}"


class KrakManager:
    """Manage Krak allocation and distribution."""

    def __init__(self) -> None:
        self.kraks: List[Krak] = []
        self.github_handler = GitHubHandler("https://github.com/my-repo")
        self.vercel_handler = VercelHandler("https://vercel.com/trigger-function")

    def add_krak(self, krak: Krak) -> None:
        self.kraks.append(krak)
        self.github_handler.commit_task(krak)

    def distribute_krak(self) -> str:
        for krak in self.kraks:
            if krak.status == "pending" and random.random() > 0.5:
                msg = krak.activate()
                self.vercel_handler.trigger_task(krak)
                self.github_handler.update_task_status(krak)
                return msg
        return "No kraks to distribute."
