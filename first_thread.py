#coding=utf-8

import psycopg2
import threading
import time
import json
import logging

USER='postgres'
PASSWORD='lzc'
PORT='5432'
DATABASE='test1'

def write():
    fo_w=open("C:\\Users\\14748\\Desktop\\insert_read.txt","w")
    for i in range(0, 1000):
        id = i
        name = 'test_%d' % i
        t = time.time()
        timeArray = time.localtime(t)
        timeStr = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        sql=json.dumps([id,name,timeStr])
        fo_w.write(sql)
        fo_w.write('\n')
    print 'ok'
    fo_w.close()

def insert():
    conn = psycopg2.connect(user=USER, password=PASSWORD, database=DATABASE, port=PORT)
    cur = conn.cursor()
    fo_r=open("C:\\Users\\14748\\Desktop\\insert_read.txt","r")
    sql='INSERT INTO table_test VALUES(%s,%s,%s);'
    while True:
        link = fo_r.readline()
        if  link :
            link=json.loads(link)
            value=[link[i] for i in range(len(link))]
            cur.execute(sql,value)
        else:
            break
    fo_r.close()
    conn.commit()
    conn.close()
    pass

def search():
    conn1=psycopg2.connect(user=USER, password=PASSWORD, database=DATABASE, port=PORT)
    cur1=conn1.cursor()
    fo_s = open("C:\\Users\\14748\\Desktop\\sql_table.txt", "w")
    sql='''SELECT * FROM table_test;'''
    cur1.execute(sql)
    result =cur1.fetchall()
    for i in range(0, len(result)):
        pass
        fo_s.write(json.dumps(result[i])+'\n')
    fo_s.close()
    pass


if __name__=="__main__":
    start_time=time.time()

    insert_thread=threading.Thread(target=insert)
    search_thread=threading.Thread(target=search)
    thread=[insert_thread,search_thread]

    write()
    for i in range(len(thread)):
        thread[i].start()
    for i in range(len(thread)):
        thread[i].join()

    end_time=time.time()
    print end_time-start_time
