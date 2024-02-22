#https://naomy-gomes.medium.com/crud-with-python-fastapi-and-mongodb-e830c6c538f4
import uvicorn
from pymongo import MongoClient
from fastapi import FastAPI
from routes.api import router as  routerAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.on_event("startup")
def startup_db_client():
    try:
    
        app.mongodb_client = MongoClient('mongodb://root:[agik]@localhost:27017/')
        app.database = app.mongodb_client['tunawiri_db']
        print("Connected to the MongoDB database!")
    except Exception :
        print(' some error occured ')

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(routerAPI)


if __name__ == '__main__': #this indicates that this a script to be run
    uvicorn.run("main:app", host='127.0.0.1', port=8050, log_level="info", reload = True)
