# my_service.py
from ..config import Config 



config = Config() 

class MyService:
    def do_something(self):
        # Business logic implementation
        return "Something " + config.testing 
