# @Author: Lanbao Shen
# @Create: 2023/6/28 22:25
from pydantic import BaseModel


class Msg(BaseModel):
    msg: str
