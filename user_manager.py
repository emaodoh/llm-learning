import json
from pathlib import Path
from uuid import UUID
from database import get_connection

USER_FILE = Path("user.json")


def create_user():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                        INSERT INTO users
                        DEFAULT VALUES
                        RETURNING id;
                        """)
            user_id = cursor.fetchone()[0]

            connection.commit()

            return user_id
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def save_user_id(user_id):
    with USER_FILE.open("w", encoding="utf-8") as file:
        json.dump({"user_id": str(user_id)}, file, indent=4)


def load_user_id():
    if USER_FILE.exists():
        try:
            with USER_FILE.open("r", encoding="utf-8") as file:
                data = json.load(file)
            user_id = UUID(str(data["user_id"]))
            with get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1 FROM users WHERE id = %s", (user_id,))
                    if cursor.fetchone():
                        return user_id
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            pass

    # Missing, malformed, stale, or pre-database IDs get a valid database user.
    user_id = create_user()
    save_user_id(user_id)
    return user_id
