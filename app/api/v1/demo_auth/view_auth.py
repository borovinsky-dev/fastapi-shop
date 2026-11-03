from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

router = APIRouter(prefix="/demo-auth", tags=["auth"])

security = HTTPBasic()


@router.get("/basic-auth/")
def demo_basic_auth_credentials(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    return {
        "message": "hi",
        "username": credentials.username,
        "password": credentials.password,
    }


username_to_passwords = {"admin": "admin", "john": "password"}


def get_auth_user_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    unauth = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"JWT-Authenticate": "Basic"},
    )

    correct_password = username_to_passwords.get(credentials.username)
    if correct_password is None:
        raise unauth
    if credentials.username not in username_to_passwords:
        raise unauth

    if not secrets.compare_digest(
        credentials.password.encode("utf-8"), correct_password.encode("utf-8")
    ):
        raise unauth

    return credentials.username


@router.get("/basic-auth-username/")
def demo_basic_auth_username(auth_username: str = Depends(get_auth_user_username)):
    return {"message": f"Hi, {auth_username}"}
