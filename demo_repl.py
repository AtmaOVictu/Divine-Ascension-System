import asyncio
from divine_agents.agent import Agent
from divine_agents.repl import run_demo_loop

async def main() -> None:
    agent = Agent("OntoAssistant")
    await run_demo_loop(agent)

if __name__ == "__main__":
    asyncio.run(main())
