from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL:str
    SECRET_key:str
    Token_Expire_Time_Min:int
    Algorithm:str
    class config:
        env_file=".env"


settings=Settings()