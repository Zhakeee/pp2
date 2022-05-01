# CREATE OR REPLACE FUNCTION public.pattern(
# 	)
#     RETURNS TABLE(name character varying) 
#     LANGUAGE 'plpgsql'

# AS $$
# begin
#     return query
#     select phonebooook.name from phonebooook where phonebooook.name like '%Zhandos%';
# end;
# $$;

# ALTER FUNCTION public.pattern()
#     OWNER TO postgres;

import psycopg2
from config import config

def pattern2():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.callproc('pattern2', ())
        row = cur.fetchone()
        while row is not None:
            print(*row)
            row = cur.fetchone()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

pattern2()