import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load', methods=['POST'])
def load_data():
    serialized_data = request.data
    data = pickle.loads(serialized_data)
    return f"Loaded data: {data}"

if __name__ == '__main__':
    app.run(debug=True)
