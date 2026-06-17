from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    database_username: str
    database_password: str
    database_port: str 
    database_hostname: str 
    database_name: str # for creating the database URL for connecting to the database.
    secret_key: str # for creating the token.
    algorithm: str # for hashing the password and creating the token.
    access_token_expire_minutes: int # for setting the expiration time of the token.

    class Config:
        env_file = ".env" # it tells pydantic to read the environment variables from the .env file. It will look for the .env file in the root directory of the project.
settings = Settings()

