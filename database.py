import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


def test_connection():
    try:
        connection = psycopg.connect(
            os.getenv("DATABASE_URL")
        )

        print("Connected successfully!")

        connection.close()

    except Exception as error:
        print("Connection failed:")
        print(error)





def get_connection():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL is missing; add your PostgreSQL connection URL to .env")
    return psycopg.connect(database_url)



def create_tables():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_memories (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                    category TEXT NOT NULL,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            # Keep one current value per category, including for databases that
            # already contain duplicate rows from earlier development.
            cursor.execute("""
                DELETE FROM user_memories older
                USING user_memories newer
                WHERE older.user_id = newer.user_id
                  AND older.category = newer.category
                  AND older.id < newer.id;
            """)
            cursor.execute("""
                CREATE UNIQUE INDEX IF NOT EXISTS user_memories_user_category_idx
                ON user_memories (user_id, category);
            """)

        connection.commit()

        # print("Tables created successfully!")

    except Exception as error:
        print("Error creating tables:")
        print(error)

        connection.rollback()
        return 

    finally:
        connection.close()


if __name__ == "__main__":
    create_tables()
