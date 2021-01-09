import sqlite3
con=sqlite3.connect("jasmine.db")
cursor=con.cursor()
username=input("entr username: ")
email=input("enter email : ")
pwd=input("enter password : ")
c_pwd=input("enter confirm_password : ")

if(pwd==c_pwd):
    try:
        query="insert into jasmine_table(USERNAME,EMAIL,PASSWORD,CONFIRM_PWD) values(?,?,?,?)"
        cursor.execute(query,(username,email,pwd,c_pwd))

        con.commit()
        print("succefully REGISTERED....!")
    except Exception as e:
        print(e)

else:
    print(" password and confirm password must be same")
