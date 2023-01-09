from pytest import fixture
from settings.params import settings


@fixture
def user_data() -> dict:
    return {
        "username": settings.USER_NAME,
        "password": settings.PASSWORD
    }
