import asyncio
from .agent import Agent

async def run_demo_loop(agent: Agent) -> None:
    """Run an interactive REPL loop with the given agent."""
    print("Type 'quit' or 'exit' to end the conversation.")
    loop = asyncio.get_event_loop()
    while True:
        try:
            user_input = await loop.run_in_executor(None, input, "You: ")
        except EOFError:
            break
        if user_input.lower() in ("quit", "exit"):
            break
        agent.update_emotion(0.1)
        agent.transition()
        print(f"{agent.name} ({agent.state}): {agent.respond(user_input)}")
    print("Goodbye!")
