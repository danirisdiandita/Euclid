from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_token_header
from ..models.location import Location 

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
@router.post("/")
async def geocode_address(location: Location): 
    
    
    return {"address": f"{location.country}, {location.state_province}, {location.city_regency}, {location.district}, {location.subdistrict}, {location.streetname}"}

