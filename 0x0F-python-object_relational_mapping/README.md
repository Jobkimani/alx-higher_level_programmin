  Overview
Object-Relational Mapping (ORM) is a programming technique enabling developers to interact with a relational database using an object-oriented paradigm in their chosen programming language. Within the Python ecosystem, several popular ORM libraries, such as SQLAlchemy, Django ORM, and Peewee, empower developers to engage with databases using Python objects and methods, eliminating the need for raw SQL queries. ORM libraries contribute to simplifying database interactions, enhancing code readability, and minimizing the amount of boilerplate code required for standard database operations.

Context
This project bridges the realms of Databases and Python. The initial phase involves utilizing the MySQLdb module to establish a connection to a MySQL database and execute SQL queries. Subsequently, the project introduces the SQLAlchemy module, an Object Relational Mapper (ORM). The primary distinction lies in the absence of SQL queries with an ORM, shifting the focus from storage details to object utilization. With an ORM, developers can concentrate on actions involving objects rather than the intricacies of storage.

Without ORM:

python
Copy code
# Traditional SQL-based approach
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
With ORM:

python
Copy code
# ORM-based approach using SQLAlchemy
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
Notice the significant difference? Exciting, isn't it?

The main challenge with ORM lies in its syntax. While many ORM libraries share a similar syntax, it's not always consistent. It's recommended to start with tutorials and delve into documentation as needed rather than overwhelming oneself at the outset.

Resources
Read or watch:

Object-relation mappers
mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)
MySQLdb tutorial
SQLAlchemy tutorial
SQLAlchemy
mysqlclient/MySQLdb
Introduction to SQLAlchemy
Flask-SQLAlchemy
10 common stumbling blocks for SQLAlchemy newbies
Python SQLAlchemy cheatsheet
SQLAlchemy ORM tutorial for python developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)
SQLAlchemy tutorial
Learning Objectives
By the end of this project, you should be able to explain to anyone, without the help of Google:

General
 Why Python programming is awesome :tada:
 How to connect to a MySQL database from a Python script
 How to SELECT rows in a MySQL table from a Python script
 How to INSERT rows in a MySQL table from a Python script
 What ORM means
 How to map a Python Class to a MySQL table
Requirements
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
Your files will be executed with MySQLdb version 2.0.x
Your files will be executed with SQLAlchemy version 1.4.x
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
You are not allowed to use execute with sqlalchemy
Additional Information
Install MySQLdb module version 2.0.x
For installing MySQLdb, you need to have MySQL installed: How to install

python
Copy code
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
Install SQLAlchemy module version 1.4.x
python
Copy code
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
You may encounter this Warning message:

arduino
Copy code
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be removed in a future release.")
  cursor.execute(statement, parameters)  