import asyncio
from fastapi import APIRouter, BackgroundTasks
from services.generation import render_template
from schemas.generation import RenderSchema

router = APIRouter(prefix="/generation")


@router.get("/")
async def check():
    return {"render": "I am online"}


@router.post("/render")
async def render(render: RenderSchema, background_tasks: BackgroundTasks):
    text = render.text
    background_tasks.add_task(render_template, text)
    return {"render": "Render was launched"}
