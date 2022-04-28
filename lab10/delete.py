import psycopg2
from config import config

def delete_user(name):
    sql = """
    delete from phonebooook
    where name = %s;
    """

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (name))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

delete_user('zhake')
