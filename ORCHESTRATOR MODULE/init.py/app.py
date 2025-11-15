"""FastAPI orchestrator."""
from fastapi import FastAPI
from pydantic import BaseModel
from automation.graph_api import InstagramGraphClient
import asyncio
from mas.run_simulation import run_simulation as sim

app = FastAPI()

class PostRequest(BaseModel):
    image_url: str
    caption: str
    dry_run: bool = True

@app.post("/post")
async def post(req: PostRequest):
    client = InstagramGraphClient(dry_run=req.dry_run)
    container = client.create_media_container(req.image_url, req.caption)
    media = client.publish_container(container["id"])
    return {"container": container, "media": media}

@app.get("/simulate")
async def simulate(num_agents: int = 10, cycles: int = 50):
    asyncio.create_task(sim(num_agents, cycles))
    return {"status": "started", "agents": num_agents, "cycles": cycles}
