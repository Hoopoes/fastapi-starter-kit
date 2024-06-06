import time
import asyncio
from app.utils.logger import log
from fastapi import FastAPI, Request
from config import Config
from fastapi.middleware import Middleware
from contextlib import asynccontextmanager
from app.job.cron_job import cron_job
from app.api.collection import collection_router
from fastapi.middleware.cors import CORSMiddleware
from app.db.prisma_client import prisma_client

def init_routers(app_: FastAPI) -> None:
    app_.include_router(collection_router)

def make_middleware() -> list[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        ),
    ]
    return middleware

async def connect_prisma():
    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            await prisma_client.connect()
            log.info("Successfully connected to Prisma.")
            break
        except Exception as e:
            log.error(f"Failed to connect to Prisma (Attempt {attempt}/{max_retries}): {e}")
            await asyncio.sleep(2 ** attempt)
    else:
        log.error("Unable to connect to Prisma after multiple attempts.")
        raise RuntimeError("Unable to connect to Prisma.")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_prisma()
    await cron_job()
    yield
    await prisma_client.disconnect()
    log.info("Successfully disconnected from Prisma")

def create_app() -> FastAPI:
    app_ = FastAPI(
        title=Config.app_name,
        description=Config.description,
        version="1.0.0",
        middleware=make_middleware(),
        lifespan=lifespan,
    )
    init_routers(app_=app_)
    return app_


app = create_app()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.monotonic()
    response = await call_next(request)
    process_time = time.monotonic() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    
    # Log additional information
    # api_type = request.scope.get("type", "Unknown")
    route = request.scope.get("path", "Unknown")
    http_method = request.method
    log.info(f"- {http_method} \"{route}\" Time Taken: {process_time:.2f} s 🚀")
    
    return response