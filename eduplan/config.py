from pydantic_settings import BaseSettings


class EduplanConfig(BaseSettings):
    data_filepath: str
