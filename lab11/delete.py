# CREATE OR REPLACE PROCEDURE public.delete_data(
# 	IN p_name character varying)
# LANGUAGE 'plpgsql'
# AS $BODY$
# begin
# 	delete from phonebooook
# 	where phonebooook.name = p_name;
# end;
# $BODY$;

import psycopg2
from config import config

def delete_data(p_name):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('call delete_data(%s)', (p_name, ))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

delete_data('Dad')