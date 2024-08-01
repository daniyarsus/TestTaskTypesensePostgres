import typesense

from src.settings import get_general_settings


class TypesenseSettings:
    def __init__(self) -> None:
        self.TYPESENSE_API_KEY = get_general_settings().TYPESENSE_API_KEY
        self.TYPESENSE_HOST = get_general_settings().TYPESENSE_HOST
        self.TYPESENSE_PORT = get_general_settings().TYPESENSE_PORT

    def get_typesense_client(self) -> object:
        client = typesense.Client({
            'api_key': self.TYPESENSE_API_KEY,
            'nodes': [{
                'host': self.TYPESENSE_HOST,
                'port': self.TYPESENSE_PORT,
                'protocol': 'http'
            }],
            'connection_timeout_seconds': 5
        })
        return client


def get_typesense_settings() -> TypesenseSettings:
    return TypesenseSettings()
