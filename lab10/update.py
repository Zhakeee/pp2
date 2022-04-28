import psycopg2
from config import config

def update_user(name, number):
    sql = """
    update phonebooook
    set number = %s
    where name = %s;
    """
    conn = None
    try: 
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (name, number))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

update_user('Mum', '870215795999')
