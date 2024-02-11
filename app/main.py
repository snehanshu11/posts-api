from fastapi import FastAPI
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from . import models
from .routers import post, user, health, auth, vote
from .config import settings
import socket
#origins = ["https://www.google.com", "https://www.youtube.com"]
origins = ["*"]
app = FastAPI()
handler = Mangum(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/server")
async def server():
    return  {"msg": socket.gethostname()}

app.include_router(health.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


models.Base.metadata.create_all(bind=engine)