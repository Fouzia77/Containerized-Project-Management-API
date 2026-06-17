from src.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def test_password_hash():

    password = "123456"

    hashed = hash_password(password)

    assert hashed != password
    assert verify_password(password, hashed)


def test_password_wrong():

    hashed = hash_password("123456")

    assert verify_password(
        "wrong",
        hashed
    ) == False


def test_create_token():

    token = create_access_token(
        {
            "user_id":1
        }
    )

    assert token is not None