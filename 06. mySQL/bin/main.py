import mysql.connector

'''
1.install mysql __ **1.use every thing as default, 2. don't forget the passwd**
2.install mysql.connecter __ for python
3.creat a database in mySQL
Example::

show databases;
create database Fahad;
use Fahad;
create table student(name varchar(20), college varchar(20));
insert into student values ('Fahad','BIGC'), ("faysal",("BIGC"));

{ ****use this commands wisely****}
chack yor work with::

select * from student;
'''

mydb = mysql.connector.connect(
host ="localhost",
user ="root",
passwd = "fahadhossen#1998#mysql",
database = "fahad"
)
mycursor = mydb.cursor()

mycursor.execute("select * from student")

result= mycursor.fetchall()  # Temp keep recived data

for i in result:
  print(i)



