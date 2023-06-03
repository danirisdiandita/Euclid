from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_token_header


router = APIRouter(
    prefix='/geocode', 
    tags=['geocode'], 
    responses={404: {"description": "Location not Found"}}
)


@router.get("/")
async def current_location(): 
    return {
        "latitude": -7.7856768,
        "longitude": 110.3659008
    }
