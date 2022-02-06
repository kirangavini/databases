

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
select * from salespeople

"""

cursor.execute(create_table)

x = cursor.fetchall()


print(x)
conn.commit()
conn.close() 
