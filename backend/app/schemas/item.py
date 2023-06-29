# @Author: Lanbao Shen
# @Create: 2023/6/28 22:10
from typing import Optional

from pydantic import BaseModel


# Shared properties
class ItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    owner_id: Optional[int] = None


# Properties to receive via API on creation
class ItemCreate(ItemBase):
    title: str
    owner_id: int


# Properties to receive via API on update
class ItemUpdate(ItemBase):
    pass


# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Item(ItemInDBBase):
    pass


# Additional properties stored in DB
class ItemInDB(ItemInDBBase):
    pass
