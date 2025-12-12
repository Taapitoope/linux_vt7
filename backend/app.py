from flask import Flask, jsonify
import os
import mysql.connector

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppass")
DB_NAME = os.getenv("DB_NAME", "appdb")


@app.route("/api")
def api_root():
    return jsonify({"message": "Hello from API root"})


@app.route("/api/db")
def api_db():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from MySQL!'")
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify({"message": row[0]})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)