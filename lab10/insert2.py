# Create Procedure edit
# (
# r_name varchar,
# r_phone_number varchar
# )
# language 'plpgsql'
# as $$
# begin
# if (not exists (Select name from phonebook where name = r_name)) then
#          insert into phonebook(name, phone_number)
# 		 values(r_name, r_phone_number);
# Else
#           update phonebook set phone_number = r_phone_number where phonebook.name = r_name;
# end if;
# end;
# $$

import psycopg2
from config import config

def edit(r_name, r_phone_number):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('call ediccc(%s, %s)', (r_name, r_phone_number))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

edit('Mum', '87770532777')
edit('Daud', '87052984573')