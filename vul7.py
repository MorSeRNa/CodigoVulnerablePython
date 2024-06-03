from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['data']
    try:
        if int(data) > 10:
            return "Data is greater than 10"
        else:
            return "Data is not greater than 10"
    except ValueError:
        return "Invalid input"

if __name__ == '__main__':
    app.run(debug=True)
