from database.connection import conectar

def criar_tabelas():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS usuario (
                id_usuario SERIAL PRIMARY KEY,
                nome VARCHAR(100),
                email VARCHAR(100),
                tipo_usuario VARCHAR(20),
                telefone VARCHAR(20),
                cpf_cnpj VARCHAR(20),
                senha VARCHAR(100),
                data_cadastro DATE
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS categoria (
                id_categoria SERIAL PRIMARY KEY,
                nome VARCHAR(100),
                descricao TEXT
            );
        """)
        conn.commit()
        print("✅ Tabelas criadas com sucesso.")

def carregar_dados_iniciais():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO categoria (nome, descricao) VALUES (%s, %s)", ("Hortifruti", "Frutas e verduras"))
        cur.execute("INSERT INTO categoria (nome, descricao) VALUES (%s, %s)", ("Carnes", "Bovinas e suínas"))
        conn.commit()
        print("✅ Dados iniciais carregados.")

def remover_tabelas():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS categoria CASCADE;")
        cur.execute("DROP TABLE IF EXISTS usuario CASCADE;")
        conn.commit()
        print("✅ Tabelas removidas com sucesso.")
