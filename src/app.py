from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'db'),
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', 'password'),
        database=os.getenv('MYSQL_DATABASE', 'hola_mundo_db')
    )

@app.route('/')
def hello_world():
    db_status = "Desconectada"
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        db_status = "Conectada"
        cursor.close()
        conn.close()
    except Exception as e:
        db_status = f"Error: {str(e)}"
    
    return render_template('index.html', db_status=db_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
