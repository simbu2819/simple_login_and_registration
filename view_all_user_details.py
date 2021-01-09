import sqlite3
connect=sqlite3.connect("jasmine.db")
cursor=connect.cursor()

query="select * from jasmine_table"
cursor.execute(query)
count=1
for rows in cursor.fetchall():
    print(count,":- ",'USERNAME :',rows[0],'|','EMAIL :',rows[1],'|','PASSWORD :',rows[2],'|','CONFIRM_PASSWORD :',rows[3])
    count=+1
cursor.close()
connect.close()
