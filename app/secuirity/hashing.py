# password hashing
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    def encrypt(self: str):
        return pwd_context.hash(self)

    def verify(self: str, plain_password: str):
        return pwd_context.verify(plain_password, self)
