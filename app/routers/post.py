from fastapi import FastAPI, Body , Response , status , HTTPException ,Depends ,APIRouter
from sqlalchemy.orm  import Session
from typing import List, Optional
from .. import model, schemas 
from ..oauth2 import get_current_user
from ..database import get_db
from sqlalchemy import func


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


#getting all post
@router.get("/", response_model= list[schemas.PostOut]) # it will return a list of posts in the response.
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(get_current_user),
limit: int = 10 , skip: int = 0 ,search: Optional[str] = ""):
    # cursor.execute("""select * from posts""")
    # posts = cursor.fetchall()
    # posts = db.query(model.post).filter(model.post.title.contains(search)).limit(limit).offset(skip).all()

    posts = db.query(model.post , func.count(model.Vote.post_id).label("votes")).join(
        model.Vote, model.Vote.post_id == model.post.id, isouter=True).group_by(
            model.post.id).filter(model.post.title.contains(search)).limit(limit).offset(skip).all()
    return posts


# #creating a posts
# @app.post("/posts" , status_code= status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     # print(post.title) # access the title of the post
#     post_dict = post.dict() # convert the post object to a dictionary
#     post_dict['id'] = randrange(0, 1000000) # generate a random id for the post
#     my_posts.append(post_dict) # add the new post to the list of posts
#     return {"data":post_dict}
# #title str , content str


# creating a new post and save it to the database
@router.post("/" , status_code = status.HTTP_201_CREATED , response_model=schemas.Post)
def create_posts(post: schemas.PostCreate , db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    # # cursor.execute(f "insert into post (title , content , published) values({post.title},{post.content})")# this is not a good way to insert data into as it will lead to sql injection.
    # cursor.execute(""" insert into posts (title, content ,published) values(%s , %s ,%s) returning * """ ,   
    #                (post.title , post.content ,   post.published))
    # new_post = cursor.fetchone()
    # conn.commit()

    #sqlalchemy way to insert data into the database.
    #one way to do this = new_post=model.post(title = post.title , content = post.content , published = post.published)
    
    print(current_user.email)
    new_post =model.post(owner_id=current_user.id ,**post.dict())# this will unpack the post dictionary and pass the values as keyword arguments to the post model. It is a more concise way to create a new post object.
    db.add(new_post)
    db.commit()
    db.refresh(new_post)# this will refresh the new_post object with the data from the database.
    return new_post 

#getting an individual post
@router.get("/{id}", response_model = schemas.PostOut) #path parameter id is defined in the endpoint.
def get_post(id:int,db: Session = Depends(get_db),current_user: int = Depends(get_current_user)): #, response: Response):
    #sql operation
    # cursor.execute(""" select * from posts where id = %s """ , (str(id),))
    # post = cursor.fetchone()
    # print(test_post)
    # # print(id)
    # post = find_post(id)
    post = db.query(model.post).filter(model.post.id == id).first()
    post =  db.query(model.post , func.count(model.Vote.post_id).label("votes")).join(
            model.Vote, model.Vote.post_id == model.post.id, isouter=True).group_by(
            model.post.id).filter(model.post.id == id).first()
    # print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")
        
        # if post.owner_id != current_user.id:
        #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
        #     detail=f"Not authorized to perform requested action")

        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}
    return  post



@router.delete("/{id}" , status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int , db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    #delete the post 
    #find the index in the array that has required id
    #my_post.pop(index)
    ### sql operation
    # cursor.execute(""" delete from posts where id = %s returning *""" , (str(id),))
    # delete_post=cursor.fetchone()
    # conn.commit()
    # index = find_index_post(id)
    # if post == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"post with id: {id} was not found")
    # # my_posts.pop(index)
    # return {"message": "post was successfully deleted"}

    post_query = db.query(model.post).filter(model.post.id == id)
    
    post = post_query.first()

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"post with id: {id} was not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
        detail=f"Not authorized to perform requested action")


    post_query.delete(synchronize_session=False)
    db.commit()

@router.put("/{id}" , response_model=schemas.Post)
def update_post(id:int, updated_post: schemas.PostCreate , db: Session = Depends(get_db) , current_user: int = Depends(get_current_user)):
    # cursor.execute(""" update posts set title = %s , content = %s , published = %s where id = %s returning *""" , (post.title , post.content , post.published , str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    # # index = find_index_post(id)
    # if updated_post == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"post with id: {id} was not found")
    # # post_dict = post.dict()
    # # post_dict['id'] = id
    # # my_posts[index] = post_dict
    #sqlalchemy way to update the post
    post_query = db.query(model.post).filter(model.post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail = f"post with id: {id} was not found")

    post_query.update(updated_post.dict(), synchronize_session=False)
    # post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return  post_query.first()
