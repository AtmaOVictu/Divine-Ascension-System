import random
import time
import json
import urllib.request


class Krak:
    """Represents a task (krak) that an agent must complete."""

    def __init__(self, name: str, condition: str, status: str = "pending"):
        self.name = name
        self.condition = condition
        self.status = status
        self.timestamp = time.time()

    def activate(self) -> str:
        """Activate the krak if it is pending."""
        if self.status == "pending":
            self.status = "in-progress"
            self.timestamp = time.time()
            return (
                f"Krak {self.name} activated at "
                f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.timestamp))}"
            )
        return f"Krak {self.name} is already active."

    def complete(self) -> str:
        """Mark the krak as completed."""
        self.status = "completed"
        self.timestamp = time.time()
        return (
            f"Krak {self.name} completed at "
            f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.timestamp))}"
        )


class GitHubHandler:
    """Simulate synchronization of tasks with GitHub."""

    def __init__(self, repository_url: str):
        self.repository_url = repository_url

    def commit_task(self, task: Krak) -> str:
        print(f"Committing Krak {task.name} to GitHub repository: {self.repository_url}")
        return f"Task {task.name} committed to GitHub."

    def update_task_status(self, task: Krak) -> str:
        print(f"Updating status of Krak {task.name} on GitHub to {task.status}.")
        return f"Status of {task.name} updated to {task.status}."


class VercelHandler:
    """Simulate execution of tasks through Vercel's serverless functions."""

    def __init__(self, vercel_endpoint: str):
        self.vercel_endpoint = vercel_endpoint

    def trigger_task(self, task: Krak) -> str:
        payload = {
            "task_name": task.name,
            "status": task.status,
            "timestamp": time.time(),
        }
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            self.vercel_endpoint,
            data=data,
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req) as response:
            return response.read().decode("utf-8")


class KrakManager:
    """Manage allocation and distribution of kraks."""

    def __init__(self):
        self.kraks = []
        self.github_handler = GitHubHandler("https://github.com/my-repo")
        self.vercel_handler = VercelHandler("https://vercel.com/trigger-function")

    def add_krak(self, krak: Krak) -> None:
        self.kraks.append(krak)
        self.github_handler.commit_task(krak)

    def distribute_krak(self) -> str:
        for krak in self.kraks:
            if krak.status == "pending":
                if random.random() > 0.5:
                    krak.activate()
                    self.vercel_handler.trigger_task(krak)
                    self.github_handler.update_task_status(krak)
                    return f"Distributed Krak {krak.name}"
        return "No kraks to distribute."
