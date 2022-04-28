import csv
import psycopg2
from config import config

conn = None
params = config()
conn = psycopg2.connect(**params)
cur = conn.cursor()

def insert_data(name, number):
    sql = """
    INSERT INTO phonebooook(name, number)
    VALUES(%s, %s);
    """

with open('proverka.csv', 'r') as f:
    cur.copy_from(f, 'phonebooook', sep=',')
    # for i in f:
    #     insert_data(i[0], i[1])
    cur.close()
    conn.commit()


f.close()