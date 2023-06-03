import os 
from dotenv import load_dotenv 

load_dotenv() 

class Config: 
    def __init__(self) -> None:
        self.es_url = os.getenv("ELASTICSEARCH_HOST", "localhost")
        self.es_port = os.getenv("ELASTICSEARCH_PORT", 9200)
        self.es_username = os.getenv("ELASTICSEARCH_USERNAME", "username")
        self.es_password = os.getenv("ELASTICSEARCH_PASSWORD", "password")
        self.testing = os.getenv("TESTING", 'notread')