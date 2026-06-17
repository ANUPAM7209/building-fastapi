from fastapi import FastAPI
from . import model 
from .database import engine 
from .routers import post, user, auth ,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

print(settings.database_password) # it will print the value of the database_username from the .env file if it exists, otherwise it will print the default value "localhost".

# model.Base.metadata.create_all(bind=engine)#this will create the tables in the database based on the models  defined in the models.py file. It will check if the tables already exist and create them if they don't.

#create an instance of the FastAPI 
app = FastAPI()

origins = ["*"] # it will allow all the origins to access the api. It is not recommended for production, but it is fine for development. In production, you should specify the allowed origins to enhance security.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # it will allow all the HTTP methods (GET, POST, PUT, DELETE, etc.) to access the api. It is not recommended for production, but it is fine for development. In production, you should specify the allowed methods to enhance security. 
    allow_headers=["*"],# it will allow all the headers to access the api. It is not recommended for production, but it is fine for development. In production, you should specify the allowed headers to enhance security.
)

app.include_router(post.router) # it will include the post router in the main application. It will allow us to define the endpoints for the post operations in a separate file and then include them in the main application.
app.include_router(user.router) # it will include the user router in the main application. It will allow us to define the endpoints for the user operations in a separate file and then include them in the main application.
app.include_router(auth.router)
app.include_router(vote.router)


#path operation decorator to define the endpoint for the root URL ("/") and the HTTP method (GET)
@app.get("/")
def root():
    return {"Hello": "Welcome to my api"} # it convert to change into JSON format and return the response to the client.
