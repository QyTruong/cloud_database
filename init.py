# Khởi tạo và cấu hình cho app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://cloud:admin123456@database-mysql-on-aws.caciaqbx6k2i.us-east-1.rds.amazonaws.com/cloud_db?charset=utf8mb4'

db = SQLAlchemy(app=app)