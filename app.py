from flask import render_template
from dao import load_users
from init import app

# Dẫn tới trang chủ và render trang index.html (kèm với danh sách users)
@app.route('/')
def index():
    users = load_users()

    return render_template('index.html', users=users)


if __name__ == '__main__':
    # chạy 0.0.0.0 để cho ra public ip
    app.run(host='0.0.0.0', port=5000, debug=True)