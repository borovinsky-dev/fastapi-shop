from typing import Any
from datetime import datetime, timedelta, timezone
import jwt

from app.core.config import settings


def create_access_token(user_id: int) -> str:
    now = datetime.now(timezone.utc)
    # payload - данные, которые не нужны - не пароль и не секреты
    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": now + timedelta(minutes=settings.authJWT.access_token_expire_minutes),
    }
    return encode_jwt(payload)


def encode_jwt(
    payload: dict[str, Any],
    private_key: str | None = None,
    algorithm: str = settings.authJWT.algorithm,
) -> str:
    if private_key is None:
        private_key = settings.authJWT.private_key_path.read_text(encoding="utf-8")
    return jwt.encode(payload, key=private_key, algorithm=algorithm)


def decode_jwt(
    token: str | bytes,
    public_key: str | None = None,
    algorithm: str = settings.authJWT.algorithm,
) -> dict[str, Any]:
    if public_key is None:
        public_key = settings.authJWT.public_key_path.read_text(encoding="utf-8")

    return jwt.decode(
        token,
        key=public_key,
        algorithms=[algorithm],
        options={"require": ["sub", "iat", "exp"]},
    )
