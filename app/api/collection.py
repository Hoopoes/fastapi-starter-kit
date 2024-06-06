import prisma
from app.utils.logger import log
from fastapi.responses import JSONResponse
from app.db.prisma_client import prisma_client
from prisma.partials import CollectionSubFields
from fastapi import APIRouter, Depends, HTTPException
from app.response.error import CollectionNotExist, UserIDAlreadyExist
from app.schema.collection_schema import (
    CollectionImageDelReq,
    Collection, 
    CollectionReq,
    CollectDict
)

tag: str = "Collection"
collection_router: APIRouter = APIRouter(tags=[tag])

@collection_router.post('/api/db/collection/create', response_model=Collection)
async def create(req: CollectionReq = Depends()) -> Collection:

    try:
        collection = await prisma_client.collection.create(
            data={"user_id": req.user_id, "name": req.name, "action": req.action}
        )
    except prisma.errors.UniqueViolationError:
        raise UserIDAlreadyExist()

    log.debug("Create in db")
    return collection
                         
@collection_router.delete('/api/db/collection/delete')
async def delete_single_or_whole_collection(req: CollectionImageDelReq = Depends()) -> JSONResponse:

    collection = await prisma_client.collection.delete(where={"user_id": req.id})
    if not collection:
        raise CollectionNotExist()
    
    log.debug("Delete in db")
    return JSONResponse(content="Successfully Deleted", status_code=200)

@collection_router.get('/api/db/collection')
async def get_collection() -> CollectDict:
    
    collections = await CollectionSubFields.prisma().find_many()
    if not collections:
        raise CollectionNotExist()
    
    collection_dict: CollectDict = CollectDict(data={
        collection.user_id: Collection(
            collection_id=collection.id, 
            user_id=collection.user_id, 
            action=collection.action
        )
        for collection in collections
    })

    return collection_dict
