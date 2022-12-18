#coding=utf-8
#!/usr/bin/python
import psycopg2

#!!!
#该部分用于创建调试另一个表   records！！！

DATABASE="huawei"
USER="postgres"
PASSWORD="lzc"
PORT="5432"



conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, port=PORT)
cur = conn.cursor()  # 创建游标
#创建records
sql = '''
CREATE TABLE  IF NOT EXISTS records
(
NAME varchar(64) NOT NULL,
SUBJECT varchar(64) NOT NULL,
SCORE int NOT NULL
);
'''
cur.execute(sql)

name=raw_input('name:')
subject=raw_input('subject:')
score=input('score:')
insert_table_sql='INSERT INTO records(NAME,SUBJECT,SCORE) VALUES(%s,%s,%s);'
values=list()
value=(str(name),str(subject),score,)
values.append(value)
cur.executemany(insert_table_sql,values)


conn.commit()
conn.close()

