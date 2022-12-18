#coding=utf-8
#!/usr/bin/python

#基于python2.7的使用，使用的是postgresql
import psycopg2
import logging

DATABASE = 'huawei'
USER = 'postgres'
PASSWORD = 'lzc'
PORT = '5432'
HOST='localhost'
class fun:
    cur = None
    conn = None
    def connect_db(self):#连接数据库并创建表格
        try:
            self.conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, port=PORT)
            self.cur = self.conn.cursor()  # 创建游标
        except Exception as e:
            logging.error(e)
            print 'fail'
        else:
            print 'database is opened'
        create_table_sql = '''
            CREATE TABLE  IF NOT EXISTS HUAWEI
            (
            NAME varchar(64) NOT NULL,
            AGE int NOT NULL
            );
            '''
        self.cur.execute(create_table_sql)
        self.conn.commit()

    # 数据写入列表中 str_view=str(list_view[0])+''.join([','+str(list_view[i]) for i in range(1,len(list_view))])
    def insert(self, name,age):#插入
        insert_table_sql='INSERT INTO HUAWEI(NAME,AGE) VALUES(%s,%s);'
        values=list()
        value=(str(name),int(age))
        values.append(value)
        self.cur.executemany(insert_table_sql,values)
        self.conn.commit()
        pass

    def search_tar(self,name):#查找目标并返回一项
        search_sql='SELECT * FROM HUAWEI where NAME=(%s); '
        value=(str(name),)
        self.cur.execute(search_sql,value)
        result=self.cur.fetchone()
        self.conn.commit()
        return result
        pass

    def search_all(self):#查找表格全部内容，并返回列表
        sql="SELECT * FROM HUAWEI;"
        self.cur.execute(sql)
        result=self.cur.fetchall()
        self.conn.commit()
        return result

#下面的name和age删除采用的是两个函数实现，在main调用处进行判断
    def detele_name(self,tar):#删除name
        delete_sql = 'DELETE FROM HUAWEI WHERE name=(%s)'
        value = (str(tar),)
        self.cur.execute(delete_sql,value)
        self.conn.commit()
        pass

    def delete_age(self,tar):#删除age
        delete_sql = 'DELETE FROM HUAWEI WHERE age=(%s)'
        value = (int(tar),)
        self.cur.execute(delete_sql, value)
        self.conn.commit()
        pass

    def update(self,oldname,oldage,name,age):#update
        update_sql='UPDATE huawei SET name=(%s),age=(%s) where name=(%s) and age=(%s)'
        value=(str(name),age,str(oldname),oldage)
        self.cur.execute(update_sql,value)
        self.conn.commit()
        pass

    def innerjoin(self):#内连接
        innerjoin_sql='SELECT * FROM HUAWEI INNER JOIN RECORDS ON(huawei.name=records.name)'
        self.cur.execute(innerjoin_sql)
        result=self.cur.fetchall()
        self.conn.commit()
        return result

    def leftjoin(self):#内连接
        leftjoin_sql='SELECT * FROM HUAWEI LEFT OUTER JOIN RECORDS ON(huawei.name=records.name)'
        self.cur.execute(leftjoin_sql)
        result=self.cur.fetchall()
        self.conn.commit()
        return result



    def close(self):#关闭连接
        self.conn.commit()
        self.conn.close()
        pass



if __name__=="__main__":
    func=fun()

    #连接数据库huawei
    func.connect_db()

    #调用insert
    '''
    name =raw_input('\n输入插入的name:')
    age = input('输入插入的age:')
    func.insert(name,age)
    print("\ninsert successfully!")
    '''

    #调用search_tar
    name = raw_input('\n输入查询的name:')
    result=func.search_tar(name)
    print(result)

    #调用search_all
    print("\nshow table huawei")
    result_list=[]
    #print(func.search_all())
    for record in func.search_all():
        value=(record[0],record[1])
        result_list.append(value)
    print(result_list)

    #调用delete
    '''
    name=raw_input('\n请输入需要删除的name或age:')
    if  name.isalpha():
        func.detele_name(name)
    elif name.isdigit():
        func.delete_age(name)
    '''

    #调用update
    '''
    oldname=raw_input('\n输入oldname:')
    oldage=input('输入oldage:')
    name=raw_input('输入newname:')
    age=input('输入newage:')
    func.update(oldname,oldage,name,age)
    '''

    #调用内联
    print '\ninnerjoin'
    print func.innerjoin()

    #调用外联
    print '\nleftjoin'
    print func.leftjoin()

    print 'closed '