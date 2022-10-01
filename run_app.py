import uvicorn
from env import env


if __name__ == "__main__":
    uvicorn.run(
        'app.main:app',
        host=env.HOST,
        port=env.PORT,
        reload=env.RELOAD, 
    )