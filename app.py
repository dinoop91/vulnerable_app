import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Vulnerable SQL Query (SQL Injection)
@app.route("/search")
def search():
    query = request.args.get('q', '')
    conn = sqlite3.connect('database.db')
    result = conn.execute(f"SELECT * FROM users WHERE name LIKE '%{query}%'").fetchall()
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
