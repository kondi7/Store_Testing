from pydantic import BaseSettings


class Base(BaseSettings):
    TEST_URL: str = "https://www.saucedemo.com"
    USER_NAME: str = "standard_user"
    PASSWORD: str = "secret_sauce"


settings = Base()
