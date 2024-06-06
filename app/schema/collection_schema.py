from enum import Enum # or from prisma.enums import Action
from pydantic import BaseModel

class Action(str, Enum):
    ACTIVE = 'ACTIVE'
    PAUSE = 'PAUSE'

class Collection(BaseModel):
    collection_id: int | None = None
    user_id: str
    name: str | None = None
    action: Action

class CollectionReq(BaseModel):
    user_id: str
    name: str | None = None
    action: Action

class CollectDict(BaseModel):
    data: dict[int, Collection]

class CollectionImageDelReq(BaseModel):
    id: str