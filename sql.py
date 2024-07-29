# '''import pymysql as mysql
# connection=mysql.connect(host="localhost",user="root",password="livewire")
# print(connection)

#create database
import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="swetha")
cursor=connection.cursor()
cursor.execute("create database python17")

#show all databases with in root user
import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
cursor.execute("show databases")
for x in cursor:
    print(x)


#create table
import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="python17")
cursor=connection.cursor()
#cursor.execute("CREATE TABLE departments(department_id iNT PRIMARY KEY,department_name VARCHAR(50))")
cursor.execute("show tables")
print("number of tables in database:")
for x in cursor:
    print("\t",x)


import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="python17")
cursor=connection.cursor()
cursor.execute("CREATE TABLE employees(employee_id INT PRIMARY KEY,employee_name VARCHAR(100),department_id INT)")
cursor.execute("show tables")
print("number of tables in database:")
for x in cursor:
    print("\t",x)

import pymysql as mmysql
connection=mmysql.connect(host="localhost",user="root",password="livewire",database="python17")
cursor=connection.cursor()
s="insert into employees values(%s,%s,%s)"
t=(1,"hari",3)
cursor.execute(s,t)
connection.commit()
print(cursor.rowcount,"new row inserted",cursor.lastrowid)


import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="python17")
cursor=connection.cursor()
s="insert into employees values(%s,%s,%s)"
t=[(1,"harish",1),(3,"harish",2)]
cursor.executemany(s,t)
connection.commit()
print(cursor.rowcount,"new row inserted",cursor.lastrowid)


'''import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="python17")
cursor=connection.cursor()
cursor.execute("select*from employees")
result=cursor.fetchall()
print("content in the python:")
for x in result:
    print("\t",x)
    

import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="python17")
cursor=connection.cursor()
sql="update employees set employee_name='bala' where employee_id=1;"
cursor.execute(sql)
connection.commit()


import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="python17")
cursor=connection.cursor()
sql="DELETE FROM employees WHERE employee_id=1"
cursor.execute(sql)
connection.commit()
print(cursor.rowcount,"record(s)deleted")'''


import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="python17")
cursor=connection.cursor()
cursor.execute("show databases")
for x in cursor:
    print(x)


cursor.execute("use database 01")
#cursor.execute("CREATE TABLE departments(department_id INT PRIMARY KEY,department_name VARCHAR(50))")
cursor.execute("show tables")
print("number of tables in database:")
for x in cursor:
    print("\t",x)


s="insert into departments values(%s,%s)"
t=(2,"harish")
cursor.execute(s,t)
connection.commit()
print(cursor.rowcount,"new row inserted",cursor.lastrowid)
cursor.execute("select*from departments")
result=cursor.fetchall()
print("content in the python:")
for x in result:
    print("\t",x)

sql="update departments set department_name='bala'where department_id=1:"
cursor.execute(sql)
connection.commit()
sql="DELETE FROM departments WHERE department_id=1"
cursor.execute(sql)
connection.commit()
print(cursor.rowcount,"record(s)deleted")



