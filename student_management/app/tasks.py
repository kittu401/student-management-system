import pymysql
db_name = "student_mgmt"
table = "admin_reg"
def admin_login_func(email,password):

    db = pymysql.connect(host='localhost', database=db_name, user='', passwd='')

    user_email = email.lower()

    user_password = password.lower()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM ' + table + ' WHERE Email = "%s" AND Password = "%s"' %(user_email,user_password))
    db.commit()
    x = cursor.rowcount
    if x > 0:
        for row in cursor:
            email = str(row[2]).lower()
            password = str(row[3]).lower()
            print(email)
            print(password)
            if email == user_email and password == user_password:
                    print("Hello " + row[1])

    else :
        print("Enter Valid Credentials")
        admin_login_func()

def admin_user_reg():

    db = pymysql.connect(host='localhost', database=db_name, user='', passwd='')
    print("Conntcted to "+ table)
    cursor = db.cursor()
    First_Name = str(input("Enter Name: "))
    Last_Name = str(input("Enter Last Name: "))
    Email = str(input("Enter Email : "))
    Email = Email.lower()
    Password = str(input("Enter Password: "))
    Password = Password.lower()
    cursor.execute('SELECT * FROM ' + table + ' WHERE Email = "%s" AND Password = "%s"' % (Email, Password))
    db.commit()
    x = cursor.rowcount
    if x > 0:
        for row in cursor:
            email = str(row[2]).lower()
            if email == Email:
                print("Email Already registered")
                admin_user_reg()
    elif x <= 0:
        cursor.execute('INSERT INTO ' + table + ' VALUES (%s, %s, %s, %s)', (First_Name, Last_Name, Email, Password))
        db.commit()
        print("Hello " + First_Name+" " + Last_Name+" You've Registered successfully")
        admin_login_func()
while True:
    choice =  int(input("Enter 1 for login \n"
                        "enter 2 for register : "))
    if choice == 1:
        admin_login_func()
    elif choice==2:
        admin_user_reg()