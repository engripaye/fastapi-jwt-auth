from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from . import models, schemas, utils, deps
from .database import engine, Base, get_db


# CREATE DB TABLES
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple FastAPI JWT Auth")


@app.post("/signup", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def signup(user_in: schemas.UserCreate, db: Session = Depends(get_db)):

    # check existing username/email
    existing_user = db.query(models.User).filter(
        (models.User.username == user_in.username) | (models.User.email == user_in.email)
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="username or email already registered")

    hashed = utils.hash_password(user_in.password)
    user = models.User(username=user_in.username, email=user_in.email, hashed_password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # OAuth2PasswordRequestForm returns username & password fields
    user = deps.authenticate_user(db, form_data.username, form_data.password, utils.verify_password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="incorrect username or password",
                            headers={"WWW-Authenticate": "Bearer"})

@app.get("/me", response_model=schemas.UserOut)
def read_users_me(current_user: models.User = Depends(deps.get_current_user)):
    # Example of secure endpoint using dependency injection
    return current_user

@app.get("/")
def root():
    return {"message": "FastAPI JWT Auth System. Use /signup, /token, /me"}