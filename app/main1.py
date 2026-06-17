# from fastapi import FastAPI, Body , Response , status , HTTPException ,Depends
# from pydantic import BaseModel
# from typing import List, Optional # it is used to indicate that a variable can have a value of a specified type or be None. It is often used in function annotations to specify that a parameter or return value can be of a certain type or None.
# from random import randrange


# from sqlalchemy.orm  import Session
# from . import model , schemas , utils
# from .database import engine ,get_db
# from .routers import post, user, auth






# model.Base.metadata.create_all(bind=engine)#this will create the tables in the database based on the models  defined in the models.py file. It will check if the tables already exist and create them if they don't.


# #create an instance of the FastAPI 
# app = FastAPI()


















# #save all the post in a list of dictionary 
# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},{"title": "favourite foods" , "content": "I like pizza ", "id" : 2}]


# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p


# def find_index_post(id):
#     for index, p in enumerate(my_posts):
#         if p['id']==id:
#             return index

# #path operation decorator to define the endpoint for the root URL ("/") and the HTTP method (GET)
# @app.get("/")
# def root():
#     return {"Hello": "Welcome to my api"} # it convert to change into JSON format and return the response to the client.


# app.include_router(post.router) # it will include the post router in the main application. It will allow us to define the endpoints for the post operations in a separate file and then include them in the main application.
# app.include_router(user.router) # it will include the user router in the main application. It will allow us to define the endpoints for the user operations in a separate file and then include them in the main application.
# app.include_router(auth.router)





# #path operation decorator to define the endpoint for the root URL ("/") and the HTTP method (GET)
# @app.get("/")
# def root():
#     return {"Hello": "Welcome to my api"} # it convert to change into JSON format and return the response to the client.

#Postgres connectivity

# while True: # first the database get connected then the server will start otherwise keep trying.

#     try:
#         conn = psycopg2.connect(host = "localhost" , database = "fastapi" , user = "postgres",
#         password = "admin123" , cursor_factory = RealDictCursor)

#         cursor = conn.cursor()
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error:" , error)
#         time.sleep(2) # wait for 2 seconds before trying to connect again