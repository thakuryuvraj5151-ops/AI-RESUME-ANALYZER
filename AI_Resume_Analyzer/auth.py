import sqlite3

from werkzeug.security import generate_password_hash, check_password_hash


DATABASE_NAME = "resume_analyzer.db"


def create_users_table():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL

        )
    """)

    connection.commit()

    connection.close()


def register_user(username, password):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    hashed_password = generate_password_hash(password)

    try:

        cursor.execute("""
            INSERT INTO users
            (username, password)

            VALUES (?, ?)
        """, (
            username,
            hashed_password
        ))

        connection.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        connection.close()


def login_user(username, password):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, username, password
        FROM users
        WHERE username = ?
    """, (username,))

    user = cursor.fetchone()

    connection.close()


    if user is None:

        return None


    if check_password_hash(
        user[2],
        password
    ):

        return {
            "id": user[0],
            "username": user[1]
        }


    return None