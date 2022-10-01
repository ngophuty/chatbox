from fastapi import FastAPI,APIRouter



app = FastAPI()

@app.get('/',tags= ['hello world'])
async def hello():
    return {'fastapi':'hello'}