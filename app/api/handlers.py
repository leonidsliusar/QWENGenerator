import uuid
from pathlib import Path

from fastapi import APIRouter
from starlette.background import BackgroundTasks
from starlette.responses import FileResponse

from app.generators.porn import generate_image

from app.api.schema import ModelParams

router = APIRouter(prefix="/qwen", tags=["QWEN"])


@router.post("/generate")
async def generate(data: ModelParams, background_task: BackgroundTasks):
    task_id = uuid.uuid4()
    background_task.add_task(generate_image, task_id, **data.model_dump())
    return {"task_id": task_id}


@router.get("/get_file")
async def get_file(task_id: str):
    save_path = Path(__file__).parent.parent.parent / "output" / f"{task_id}.png"
    if save_path.exists():
        return FileResponse(path=save_path, filename=f"{task_id}.png", status_code=200)
    else:
        return {"error": "Processing or doesn't exist"}
