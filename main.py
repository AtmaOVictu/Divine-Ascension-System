from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


def run_conversation(rounds: int = 3) -> None:
    """Run a demonstration conversation for a number of rounds."""
    a1 = Agent("Agent1")
    a2 = Agent("Agent2", state="Jaz")

    transcript = []
    for i in range(rounds):
        transcript.append(f"--- Round {i + 1} ---")
        transcript.extend(philosophical_dialogue(a1, a2))

    for line in transcript:
        print(line)

    print(f"\nFinal states: {a1.name} -> {a1.state}, {a2.name} -> {a2.state}")
    print(f"{a1.name} history: {a1.history}")
    print(f"{a2.name} history: {a2.history}")


if __name__ == "__main__":
    run_conversation()
