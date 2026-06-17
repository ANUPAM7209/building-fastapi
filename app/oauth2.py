from jose import JWTError, jwt 
from datetime import datetime, timedelta
from . import schemas ,model
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .schemas import TokenData
from sqlalchemy.orm import Session
from .database import get_db
from .config import settings



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") # we will use this to get the token from the request header.


#three important things to create a token 
# SECRET_KEY, 
# ALGORITHM, 
# EXPIRATION_TIME - if we don't set this then the token will be valid forever.

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict):
    to_encode = data.copy() # we will copy the data to encode it.
    # we will add an expiration time to the token.
    
    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)# we will set the expiration time to 30 minutes from the current time.
    to_encode.update({"exp": expire})# we will add the expiration time to the data to encode it.
    
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)# we will encode the data using the secret key and the algorithm.
    
    
    return encoded_jwt

def verify_access_token(token:str , credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])# we will decode the token using the secret key and the algorithm.
        id: str = payload.get("user_id") # we will get the user id from the payload.
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=id) # we will create a token data object with the user id.
    except JWTError:
        raise credentials_exception
    return token_data

# get_current_user will be used as a dependency in the endpoints that require authentication. 
# It will return the current user based on the token sent in the request header.
def get_current_user(token: str = Depends(oauth2_scheme),db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                        detail=f"Could not validate credentials",
                                        headers={"WWW-Authenticate": "Bearer"})
    token_data = verify_access_token(token, credentials_exception)
    user = db.query(model.User).filter(model.User.id == token_data.id).first()
    return user