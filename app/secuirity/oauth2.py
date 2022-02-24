# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, SecurityScopes
# from sqlalchemy.orm import Session
#
# from security.database import get_db
# from security.jwt_token import verify_access_token, verify_end_user_access_token
# from constants.role import Role
#
# oauth2_scheme = OAuth2PasswordBearer(
#     tokenUrl="api/web/v1/auth",
#     scopes={
#         Role.GUEST["name"]: Role.GUEST["description"],
#         Role.ADMIN["name"]: Role.ADMIN["description"],
#         Role.SUPER_ADMIN["name"]: Role.SUPER_ADMIN["description"],
#     }
# )
#
#
# async def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
#     if security_scopes.scopes:
#         authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
#     else:
#         authenticate_value = f"Bearer"
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": authenticate_value},
#     )
#     return verify_access_token(token, credentials_exception, security_scopes, authenticate_value)
#
#
# async def get_current_end_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     return verify_end_user_access_token(token, credentials_exception, db)