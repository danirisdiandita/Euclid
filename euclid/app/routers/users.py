from fastapi import APIRouter
from ..services.my_service import MyService 

router = APIRouter()
myservice = MyService() 

@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/dosomething", tags=['users'])
async def user_do_something(): 
    dosomething = myservice.do_something() 
    return {
        "response": dosomething 
    }
    

@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}

