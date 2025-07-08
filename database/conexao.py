import psycopg2

def criar_conexao():
    try:
        conexao = psycopg2.connect(
            dbname="benedito",
            user="postgres",
            password="ShyvatuanSpin13",
            host="localhost",
            port="5432"
        )
        return conexao
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
