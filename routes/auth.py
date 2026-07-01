from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt

from database import users_collection

from schemas.user import UserSignup, UserLogin

from utils.security import hash_password, verify_password
from utils.auth import create_access_token

from config import SECRET_KEY, ALGORITHM


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="auth/login"
)


@router.post("/signup")
def signup(user: UserSignup):

    existing = users_collection.find_one({
        "$or": [
            {"email": user.email},
            {"username": user.username}
        ]
    })

    if existing:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    new_user = {
        "fullname": user.fullname,
        "email": user.email,
        "username": user.username,
        "password": hash_password(user.password),
        "age": user.age
    }

    users_collection.insert_one(new_user)

    token = create_access_token(
        {"sub": user.username}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.post("/login")
def login(user: UserLogin):

    db_user = users_collection.find_one({
        "username": user.username
    })

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        user.password,
        db_user["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": db_user["username"]}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid Token"
    )

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = users_collection.find_one(
        {"username": username},
        {"password": 0}
    )

    if user is None:
        raise credentials_exception

    user["_id"] = str(user["_id"])

    return user


@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return current_user
