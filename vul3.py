import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/list_files', methods=['GET'])
def list_files():
    directory = request.args.get('directory')
    result = os.popen(f"ls {directory}").read()
    return f"<pre>{result}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
