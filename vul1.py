import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
conn = sqlite3.connect('example.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
conn.commit()

@app.route('/get_user', methods=['GET'])
def get_user():
    user_id = request.args.get('id')
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    user = cursor.fetchone()
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
