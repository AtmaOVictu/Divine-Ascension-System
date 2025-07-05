import os
import time
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


def run_task() -> None:
    """Execute a single round of philosophical dialogue."""
    a1 = Agent("Agent 1")
    a2 = Agent("Agent 2", state="Jaz")
    for line in philosophical_dialogue(a1, a2):
        print(line)
    time.sleep(1)


def main() -> None:
    """Run the task multiple times if PYTHONPATH is configured."""
    python_path = os.getenv("PYTHONPATH")
    if not python_path:
        print("PYTHONPATH ni nastavljen!")
        return
    print(f"Trenutni PYTHONPATH: {python_path}")

    repetitions = 5
    for i in range(repetitions):
        print(f"\nPonovitev {i + 1}/{repetitions}")
        run_task()

    print("\nVse ponovitve so zaključene.")


if __name__ == "__main__":
    main()
