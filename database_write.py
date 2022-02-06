# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 16:24:02 2022

@author: kgavini
"""

endpoint = "test4.ckxoexlglhpt.us-east-1.rds.amazonaws.com"

username = "test4"
password = "Tinbin.93"
port = 3306


import pymysql

conn = pymysql.connect(
    host=endpoint,
    port=int(port),
    user=username,
    passwd=password,
    db=username,
    charset='utf8mb4')

cursor=conn.cursor()
create_table="""
create table salespeople (
salesPersonId int,
salesPersonName varchar(20) 
)
"""

cursor.execute(create_table)

insert_statement="""
Insert into salespeople
(salesPersonId,salesPersonName)
values
(1,'Daffy Duck')

"""

cursor.execute(insert_statement)

conn.commit()
conn.close() 
