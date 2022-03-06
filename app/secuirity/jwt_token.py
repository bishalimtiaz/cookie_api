from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException
from fastapi.security import SecurityScopes
from jose import JWTError, jwt
from pydantic import ValidationError
from app.schemas.authentication_schema import TokenData

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

'''
This `create_access_token` will be called when new user is created or user logged in to create session
'''
r"""
 :param expires_delta: sets expiration time of the session. After this time session is expired
"""


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credentials_exception, security_scopes: SecurityScopes,
                        authenticate_value: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("id")
        role: str = payload.get("role")
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=id, role=role)
    except (JWTError, ValidationError):
        raise credentials_exception
    if security_scopes.scopes and not token_data.role:
        raise HTTPException(
            status_code=401,
            detail="Not enough permissions",
            headers={"WWW-Authenticate": authenticate_value},
        )
    if (
            security_scopes.scopes
            and token_data.role not in security_scopes.scopes
    ):
        raise HTTPException(
            status_code=401,
            detail="Not enough permissions",
            headers={"WWW-Authenticate": authenticate_value},
        )


# def verify_end_user_access_token(token: str, credentials_exception, db: Session):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         id: str = payload.get("id")
#         auth_user_id = payload.get("auth_user_id")
#         if id is None:
#             raise credentials_exception
#         end_user_token_data = EndUserTokenData(id=id, auth_user_id=auth_user_id)
#     except JWTError:
#         raise credentials_exception
#     end_user = end_user_repo.get_end_user(db, end_user_token_data.id, end_user_token_data.auth_user_id)
#     if not end_user:
#         raise credentials_exception
#     return end_user
