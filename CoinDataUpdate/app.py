from CoinATH import get_historical_prices
from CoinPrice import get_coin_data
import psycopg2
import time

# PostgreSQL bağlantısı oluştur
conn = psycopg2.connect(
    host="192.168.1.140",
    database="postgres",
    user="postgres",
    password="postgres"
)

def get_column_data(table_name, column_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT {column_name} FROM {table_name}")
    data = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return data

def TableFirst():
    column_name = "coinname"
    column_name2 = "coinamount"
    table_name = "public.cointable"
    Table_all_name = "public.coinmarket"
    column_Name = get_column_data(table_name, column_name)
    ColumnAmount = get_column_data(table_name, column_name2)
    lengt_int = len(column_Name)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {Table_all_name}")
    conn.commit()
    cursor.close()
    CoinATH = 0.1
    for i in range(lengt_int):
        ATH_price = get_historical_prices(column_Name[i])
        price = get_coin_data(column_Name[i])
        cursor = conn.cursor()
        query = "INSERT INTO public.coinmarket (coinname, coinprice, coinamount, coinath, coinvalue, coinvalueath) VALUES(%s, %s, %s, %s, %s, %s);"
        CoinV = ColumnAmount[i]*price
        CoinVATH = ColumnAmount[i]*ATH_price
        values = (column_Name[i], price, ColumnAmount[i], ATH_price, CoinV,CoinVATH)
        CoinATH = CoinVATH + CoinATH
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
    print(CoinATH)


if __name__ == "__main__":
    while True:
        time.sleep(15)
        TableFirst()
