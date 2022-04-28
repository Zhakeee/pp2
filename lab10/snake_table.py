import psycopg2
from config import config

def create_table():
    commands = (
        """
        CREATE TABLE if not exists snake (
            user_id serial PRIMARY KEY,
            user_name VARCHAR (50) UNIQUE NOT NULL,
            user_score INT,
            user_level INT
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