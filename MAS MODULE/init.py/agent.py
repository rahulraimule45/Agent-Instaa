# package marker
"""Agent definitions for MAS simulation."""
import asyncio
import random
from dataclasses import dataclass

@dataclass
class Message:
    sender: str
    type: str
    payload: dict

class SimAgent:
    def __init__(self, name, inbox):
        self.name = name
        self.inbox = inbox
        self.followers = random.randint(50, 500)
        self.activity = random.random()

    async def send(self, msg):
        await self.inbox.put(msg)

    async def step(self):
        try:
            msg = self.inbox.get_nowait()
        except asyncio.QueueEmpty:
            msg = None

        if msg and msg.type == "post_announce":
            if random.random() < 0.3:
                return {"event": "promote", "agent": self.name, "target": msg.payload.get("id")}
            return None

        if random.random() < self.activity * 0.25:
            return {"event": "post", "agent": self.name, "followers": self.followers}

        return None
