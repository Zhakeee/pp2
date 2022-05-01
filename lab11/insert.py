# -- PROCEDURE: public.ediccc(character varying, character varying)

# -- DROP PROCEDURE IF EXISTS public.ediccc(character varying, character varying);

# CREATE OR REPLACE PROCEDURE public.ediccc(
# 	IN r_name character varying,
# 	IN r_phone_number character varying)
# LANGUAGE 'plpgsql'
# AS $BODY$
# begin
# if (not exists (Select name from phonebooook where name = r_name)) then
#          insert into phonebooook(name, number)
# 		 values(r_name, r_phone_number);
# Else
#           update phonebooook set number = r_phone_number where phonebooook.name = r_name;
# end if;
# end;
# $BODY$;
# ALTER PROCEDURE public.ediccc(character varying, character varying)
#     OWNER TO postgres;


import psycopg2
from config import config

def edit(r_name,r_phone_number):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('call ediccc(%s, %s)', (r_name,r_phone_number))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

edit('Mum', '87770532777')
edit('Daud', '87052984573')