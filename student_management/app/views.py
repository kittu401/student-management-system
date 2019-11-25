from app import app
from flask import flash, request, redirect, render_template

# from student_management.app.tasks import *
import pymysql
db_name = "student_mgmt"
table = "admin_reg"
table2 = "student_reg"

@app.route('/')
def Main():
    return render_template('index.html')

@app.route('/admin_login')
def admin_login():
    return render_template('adm_login.html')

@app.route('/admin_login1',methods=['POST'])
def admin_login1():
    db = pymysql.connect(host='localhost', database=db_name, user='', passwd='')
    Email_addr = request.form.get("email")
    passwd= request.form.get("password")

    if request.method == 'POST':

        user_email = Email_addr.lower()

        user_password = passwd.lower()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM ' + table + ' WHERE Email = "%s" AND Password = "%s"' %(user_email,user_password))
        db.commit()
        x = cursor.rowcount
        if x > 0:
            for row in cursor:
                email = str(row[2]).lower()
                password = str(row[3]).lower()
                if email == user_email and password == user_password:
                    return render_template('admin_profile.html',name=str(row[0]))
                else:
                    flash('Enter valid credentials')
                    return redirect('/admin_login')
        else:
            return redirect('/admin_login')

@app.route('/admin_reg')
def admin_reg():
    db = pymysql.connect(host='localhost', database=db_name, user='', passwd='')
    name = request.form.get("username")
    course = request.form.get("course")
    semester = request.form.get("semester")
    Form_no = request.form.get("Form_no")
    Contact = request.form.get("Contact")
    Email = request.form.get("email")
    Password = request.form.get("password")
    Address = request.form.get("Address")
    cursor = db.cursor()
    cursor.execute('INSERT INTO ' + table2 + ' VALUES (%s, %s, %s, %s,%s, %s, %s, %s)',
                   (name, course, semester, str(Form_no), str(Contact),
                    Email, Password, Address))
    db.commit()
    return render_template('login.html')
@app.route("/admin_reg1",methods=['POST'])
def admin_reg1():

    return render_template('admin_reg.html')

@app.route('/stu_login')
def stu_login():
    return render_template('login.html')

@app.route("/stu_login1",methods=['POST'])
def stu_login1():
    db = pymysql.connect(host='localhost', database=db_name, user='', passwd='')
    Email_addr = request.form.get("email")
    passwd = request.form.get("password")

    if request.method == 'POST':

        user_email = Email_addr.lower()

        user_password = passwd.lower()
        cursor = db.cursor()
        cursor.execute(
            'SELECT * FROM ' + table2 + ' WHERE Email_address = "%s" AND Password = "%s"' % (user_email, user_password))
        db.commit()
        x = cursor.rowcount
        if x > 0:
            for row in cursor:
                email = str(row[5]).lower()
                password = str(row[6]).lower()
                if email == user_email and password == user_password:
                    return render_template('profile.html', name=str(row[0]))
                else:
                    flash('Enter valid credentials')
                    return redirect('/stu_login')
        else:
            return redirect('/stu_login')


@app.route('/stu_reg')
def stu_reg():

    return render_template('stu_reg.html')

@app.route("/stu_reg1",methods=['POST'])
def stu_reg1():
    db = pymysql.connect(host='localhost', database=db_name, user='', passwd='')
    name = request.form.get("username")
    course = request.form.get("course")
    semester = request.form.get("semester")
    Form_no = request.form.get("Form_no")
    Contact = request.form.get("Contact")
    Email = request.form.get("email")
    Password = request.form.get("password")
    Address = request.form.get("Address")
    cursor = db.cursor()
    cursor.execute('INSERT INTO ' + table2 + ' VALUES (%s, %s, %s, %s,%s, %s, %s, %s)', (name,course,semester,str(Form_no),str(Contact),
                                                                                         Email,Password,Address))
    db.commit()
    return render_template('login.html')
