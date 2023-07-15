from fastapi import FastAPI
import psycopg2
from pydantic import BaseModel

app = FastAPI()

# PostgreSQL bağlantısı oluştur
conn = psycopg2.connect(
    host="192.168.1.140",
    database="postgres",
    user="postgres",
    password="postgres"
)


class Coin(BaseModel):
    CoinName: str
    CoinAmount: float

class CoinName(BaseModel):
    CoinName: str
@app.get("/Coin")
def get_Coin():
    # Veritabanından tüm öğeleri al
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.cointable;")
    rows = cursor.fetchall()
    cursor.close()

    # Sütun adlarını al
    columns = [desc[0] for desc in cursor.description]

    # Sütun adlarıyla eşleştirilmiş şekilde öğeleri döndür
    items = []
    for row in rows:
        item = dict(zip(columns, row))
        items.append(item)

    return items

@app.post("/Coin_Create")
def create_coin(data: Coin):
    CoinN = data.CoinName
    CoinA = data.CoinAmount
    cursor = conn.cursor()
    query = "INSERT INTO cointable (coinname, coinamount) VALUES (%s, %s)"
    values = (CoinN, CoinA)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    return {"message": "Coin created successfully"}


@app.put("/Coin/{Coin_id}")
def update_item(Coin_id: int, data: Coin):
    # Öğeyi güncelle
    cursor = conn.cursor()
    CoinN = data.CoinName
    CoinA = data.CoinAmount
    query = "UPDATE public.cointable SET coinname=%s, coinamount=%s WHERE id=%s;"
    values = (CoinN, CoinA, Coin_id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    return {"message": f"Coin {Coin_id} updated successfully"}


@app.post("/coin_delete/")
def delete_item(data: CoinName):
    # Öğeyi sil
    CoinName = data.CoinName
    cursor = conn.cursor()
    query = "DELETE FROM public.cointable WHERE coinname="+"'"+str(CoinName)+"'"+";"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    return {"message": f"{CoinName} deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
