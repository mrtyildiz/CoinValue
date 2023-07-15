from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# PostgreSQL bağlantısı oluştur
conn = psycopg2.connect(
    host="192.168.1.140",
    database="postgres",
    user="postgres",
    password="postgres"
)

# Tablodaki tüm verileri al ve HTML template ile göster
@app.route("/")
def show_table():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.coinmarket")
    rows = cursor.fetchall()
    cursor.close()

    # Sütun adlarını al
    columns = [desc[0] for desc in cursor.description]

    return render_template("table.html", columns=columns, rows=rows)

if __name__ == "__main__":
    app.run(port=80,host='0.0.0.0')
