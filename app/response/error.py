from fastapi import HTTPException

class CollectionNotExist(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Collection not Found")

class UserIDAlreadyExist(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="User ID already exists")
        
class DatabaseUnreachable(HTTPException):
    def __init__(self):
        super().__init__(status_code=500, detail="Database unreachable")