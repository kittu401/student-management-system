from flask import Flask

app=Flask(__name__)

from student_management.app import views
