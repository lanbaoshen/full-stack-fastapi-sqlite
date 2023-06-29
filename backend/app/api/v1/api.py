# @Author: Lanbao Shen
# @Create: 2023/6/29 21:55
from fastapi import APIRouter

from app.api.v1.endpoints import items
from app.api.v1.endpoints import users, login

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
