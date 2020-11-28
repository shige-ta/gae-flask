from flask import Flask, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
   return "hello world"



@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        return "hello world"
    return 0
if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8080, debug=True)