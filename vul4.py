import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping_host():
    host = request.args.get('host')
    result = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return f"<pre>{result.decode()}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
