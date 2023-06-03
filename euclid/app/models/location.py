from pydantic import BaseModel


class Location(BaseModel): 
    """

    =============================================

    Explanation in Bahasa Indonesia (for Indonesian Contributors)

    country -> negara
    state_province -> negara bagian / provinsi 
    city_regency -> kota / kabupaten 
    district -> kecamatan 
    subdistrict -> kelurahan 
    streetname -> nama jalan / blok dll 

    =============================================
    
    Examples:
    country -> Indonesia
    state_province -> Daerah Istimewa Yogyakarta 
    city_regency -> Sleman
    district -> Ngaglik 
    subdistrict -> Minomartani 
    streetname -> Jl. Layur VII No. 3, Mladangan 

    =============================================
    """
    country: str 
    state_province: str 
    city_regency: str 
    district: str 
    subdistrict: str 
    streetname: str 
