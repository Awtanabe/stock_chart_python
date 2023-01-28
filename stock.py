# request: リクエストされるデータを, render_template: templatesのは以下のviewを読み込む
from flask import Flask, request, render_template
# app = Flask(__name__, static_folder='.', static_url_path='')
app = Flask(__name__)
# @app.route('/')
# def index():
#     return app.send_static_file('index.html')

@app.route('/', methods=['GET', 'POST'])
def form():
    # ２回目以降データが送られてきた時の処理です
    if request.method == 'POST':
        print("POSTされたIDは？" + str(request.form['id']))
        print("POSTされたPASSWORDは？" + str(request.form['pwd']))
        return render_template('form.html')
    # １回目のデータが何も送られてこなかった時の処理です。
    else:
        return render_template('form.html')

@app.route('/yahoo')
def yahoo():
    return render_template('yahoo.html')

# アプリケーションを動かすためのおまじない
if __name__ == "__main__":
    app.run(port = 8000, debug=True)



# @app.route('/hello')
# def hello():
#     return app.send_static_file('hello.html')

# app.run(port=8000, debug=True)

