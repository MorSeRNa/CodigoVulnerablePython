import logging
from flask import Flask, request

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/divide', methods=['GET'])
def divide():
    a = request.args.get('a')
    b = request.args.get('b')
    try:
        result = int(a) / int(b)
        logging.debug(f"Dividing {a} by {b}")
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except ValueError:
        return "Invalid input"

if __name__ == '__main__':
    app.run(debug=True)
