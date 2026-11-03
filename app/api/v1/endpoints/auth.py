from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_current_user
from app.auth.jwt_utils import create_access_token
from app.auth.passwords import hash_password, verify_password
from app.core.database import db_session
from app.models.user import User
from app.repositories.user import UserRepo
from app.schemas.user import AccessToken, LoginRequest, UserCreate, UserRead

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
async def register_user(
    data: UserCreate,
    session: AsyncSession = Depends(db_session.get_session),
) -> UserRead:
    user_repo = UserRepo(session)
    email = str(data.email)

    if await user_repo.get_by_email(email) is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists",
        )

    try:
        user = await user_repo.create(
            username=data.username,
            email=email,
            password_hash=hash_password(data.password),
        )
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists",
        ) from None

    return user


@router.post("/login", response_model=AccessToken)
async def login(
    data: LoginRequest,
    session: AsyncSession = Depends(db_session.get_session),
) -> AccessToken:
    user_repo = UserRepo(session)
    user = await user_repo.get_by_email(str(data.email))

    if user is None or not verify_password(data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return AccessToken(access_token=create_access_token(user.id))


@router.get("/me", response_model=UserRead)
async def read_current_user(
    current_user: User = Depends(get_current_user),
) -> User:
    return current_user
