from fastapi import FastAPI, Body , Response , status , HTTPException ,Depends ,APIRouter
from sqlalchemy.orm  import Session
from .. import model, schemas, utils
from ..database import get_db


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/" , status_code = status.HTTP_201_CREATED , response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db:Session = Depends(get_db)):
    
    #hash the password - user.password
    # hashed_password = pwd_context.hash(user.password)
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    
    new_user  = model.User(**user.dict()) # from schemas.UserCreate it will convert to dictionary and then unpack the dictionary.
    db.add(new_user)#add the new user to the database session
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}',response_model=schemas.UserOut)
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.id == id).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"user with id: {id} was not found")
    return user