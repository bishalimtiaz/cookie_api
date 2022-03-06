from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int
    role: str = None


class EndUserTokenData(BaseModel):
    id: str
    auth_user_id: str
