# CREATE OR REPLACE PROCEDURE public.insert_list(
# 	IN p_name character varying,
# 	IN p_phone_number character varying)
# LANGUAGE 'plpgsql'
# AS $BODY$
# begin
# 	insert into phonebooook(name, number) values(p_name, p_phone_number);
# end;
# $BODY$;

data = [('Aliya', '87ф023981276'), ('Dan', '87789127359'), ('Val', '87778126349')]
d_data = []

import psycopg2
from config import config

def check(object):
    list = []
    cnt = -1
    for i in object:
        cnt += 1
        if not i[1].isdigit():
            del object[cnt]
            d_data.append(i[1])
    return object

def insert_list(object):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany('call insert_list(%s, %s)', object)
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            
insert_list(data)
check(data)
print(d_data)