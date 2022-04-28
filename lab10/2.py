import psycopg2
from config import config

def create_table():
    commands = (
        """
        CREATE TABLE snake (
            user_name text, user_score int, user_level int, x int, y int
        )
        """
    )

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # for command in commands:
        cur.execute(commands)
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

create_table()