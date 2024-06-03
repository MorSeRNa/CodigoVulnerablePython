from flask import Flask, request

app = Flask(__name__)

@app.route('/calculate', methods=['GET'])
def calculate():
    expression = request.args.get('expression')
    result = eval(expression)
    return f"Result: {result}"

if __name__ == '__main__':
    app.run(debug=True)
