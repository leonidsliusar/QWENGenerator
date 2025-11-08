import os

import uvicorn
from fastapi import FastAPI

from app.api.handlers import router


def main() -> None:
    """."""
    app = FastAPI()
    app.include_router(router=router)
    try:
        uvicorn.run(app=app, host="0.0.0.0", port=8000)
    except KeyboardInterrupt:
        os._exit(0)


if __name__ == "__main__":  # pragma: no cover
    main()
