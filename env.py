from pickle import TRUE
from pydantic import BaseSettings


class ENVIROMENT(BaseSettings):
    HOST : str
    PORT : int
    RELOAD : str 


env = ENVIROMENT(_env_file= '.env')