import psycopg2

def conectar():
    return psycopg2.connect(
        dbname="benedito",
        user="postgres",
        password="ShyvatuanSpin13",
        host="localhost",
        port="5432"
    )
