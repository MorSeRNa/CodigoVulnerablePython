from flask import Flask, request

app = Flask(__name__)

@app.route('/exec', methods=['GET'])
def exec_code():
    code = request.args.get('code')
    exec(code)
    return "Code executed"

if __name__ == '__main__':
    app.run(debug=True)
