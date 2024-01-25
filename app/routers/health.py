from fastapi import APIRouter

router=APIRouter(tags=["health"])

@router.get("/ping")
async def root_fucntion():
    return  {"msg": "pong"}