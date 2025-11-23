"""
    File để load models, đây cũng là nơi để query để lấy data từ model và trả về cho server
    (cụ thể server là file app.py)
"""

from models import User

def load_users():
    query = User.query

    return query.all()