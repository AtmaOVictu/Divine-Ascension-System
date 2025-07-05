import time
from typing import List

from .agent import Agent


def simulate_loading(agent: Agent, sleep_duration: float = 1.0) -> List[str]:
    """Simulate system loading by transitioning the agent through stages."""
    stages = ["Starting", "Initializing", "Emotion Update", "State Transition", "Completion"]
    log = []
    for stage in stages:
        log.append(f"Loading: {stage}")
        time.sleep(sleep_duration)
        agent.transition()
        log.append(f"Current State: {agent.philosopher.state}")
    log.append("System Loaded Successfully!")
    return log
