import sqlite3
connect=sqlite3.connect("jasmine.db")
cursor=connect.cursor()

username=input("enter username: ")
password=int(input("enter password: "))


cursor.execute('SELECT * from jasmine_table WHERE USERNAME="%s" AND PASSWORD="%d"' % (username, password))
if cursor.fetchone() is not None:
    print("Welcome : ",username)
    print("you are succesfully logged in")
    cursor.execute('SELECT * from jasmine_table WHERE USERNAME="%s" ' % (username))
    for rows in cursor.fetchall():
        print('USERNAME :',rows[0],'  |   ','EMAIL :',rows[1],'|')
else:
    print("Login failed")

    
cursor.close()
connect.close()
