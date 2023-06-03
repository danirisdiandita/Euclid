from ..config import Config 
from elasticsearch import Elasticsearch 

config = Config() 

class Geocoder: 
    def __init__(self): 
        self.es = Elasticsearch(
            hosts=[{"host": config.es_host, "port": config.es_port}], 
            http_auth=(config.es_username, config.es_password) if config.es_username and config.es_password else None, 
        )

        