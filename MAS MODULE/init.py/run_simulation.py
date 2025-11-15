"""Run a simple MAS simulation."""
import asyncio
import random
from mas.agent import SimAgent, Message

async def run_simulation(num_agents=12, cycles=100):
    queue = asyncio.Queue()
    agents = [SimAgent(f"Agent{i}", queue) for i in range(num_agents)]

    for cycle in range(cycles):
        events = []
        for a in agents:
            ev = await a.step()
            if ev:
                events.append(ev)

        for ev in events:
            if ev["event"] == "post":
                post_id = f"post_{cycle}_{random.randint(1000,9999)}"
                await queue.put(Message("system", "post_announce", {"id": post_id, "author": ev["agent"]}))
            elif ev["event"] == "promote":
                print(f"{ev['agent']} promoted {ev['target']}")

        if cycle % 10 == 0:
            print(f"Cycle {cycle}: events={len(events)}, queue={queue.qsize()}")

        await asyncio.sleep(0.02)

    print("Simulation complete.")

if __name__ == "__main__":
    asyncio.run(run_simulation())
