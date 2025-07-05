import time
from .agent import Agent


def simulate_loading(agent: Agent) -> None:
    """Simulate loading progression with agent transitions."""
    stages = [
        "Starting",
        "Initializing",
        "Emotion Update",
        "State Transition",
        "Completion",
    ]

    for stage in stages:
        print(f"Loading: {stage}")
        time.sleep(0.5)
        if stage == "Emotion Update":
            agent.update_emotion(0.8)
        if stage == "State Transition":
            agent.transition()
        print(f"Current State: {agent.state}\n")
    print("System Loaded Successfully!\n")
