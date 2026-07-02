from fastapi import APIRouter, HTTPException
from app.database.db import get_connection
from app.models.user import UserRegister, UserLogin
from app.utils.security import create_access_token
import bcrypt
router = APIRouter()


@router.post("/register")
def register(user: UserRegister):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Hash the password
        hashed_password = bcrypt.hashpw(
            user.password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        cursor.execute(
            """
            INSERT INTO users (name, email, password)
            VALUES (?, ?, ?)
            """,
            (
                user.name,
                user.email,
                hashed_password
            )
        )

        conn.commit()

        return {
            "message": "Registration Successful"
        }

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    finally:
        conn.close()


@router.post("/login")
def login(user: UserLogin):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE email = ?
        """,
        (user.email,)
    )

    existing_user = cursor.fetchone()

    conn.close()

    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Verify password
    if not bcrypt.checkpw(
        user.password.encode("utf-8"),
        existing_user["password"].encode("utf-8")
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    token = create_access_token(
    {
        "user_id": existing_user["id"],
        "email": existing_user["email"]
    }
)
    return {
        "message": "Login Successful",
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": existing_user["id"],
            "name": existing_user["name"],
            "email": existing_user["email"]
        }
    }


@router.get("/users")
def get_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, email FROM users"
    )

    users = [
        dict(row)
        for row in cursor.fetchall()
    ]

    conn.close()

    return users