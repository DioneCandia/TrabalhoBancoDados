from database.connection import conectar

def criar_tabelas():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS usuario (
                id_usuario SERIAL PRIMARY KEY,
                nome VARCHAR(100),
                email VARCHAR(100),
                telefone VARCHAR(100),
                tipo_usuario VARCHAR(20),
                cpf_cnpj VARCHAR(20),
                data_cadastro DATE DEFAULT CURRENT_DATE,
                senha VARCHAR(100)
            );

            CREATE TABLE IF NOT EXISTS instituicao (
                id_instituicao SERIAL PRIMARY KEY,
                id_usuario INT UNIQUE REFERENCES usuario(id_usuario),
                cnpj VARCHAR(20),
                nome_fantasia VARCHAR(100),
                responsavel VARCHAR(100),
                area_atuacao TEXT,
                aceita_doacao_com_valor BOOLEAN
            );

            CREATE TABLE IF NOT EXISTS categoria (
                id_categoria SERIAL PRIMARY KEY,
                nome VARCHAR(100),
                descricao TEXT
            );

            CREATE TABLE IF NOT EXISTS entrega (
                id_entrega SERIAL PRIMARY KEY,
                id_motorista INT,
                id_instituicao INT REFERENCES instituicao(id_instituicao),
                data_entrega DATE,
                status_entrega VARCHAR(30),
                tipo_entrega VARCHAR(30)
            );

            CREATE TABLE IF NOT EXISTS produto (
                id_produto SERIAL PRIMARY KEY,
                id_entrega INT REFERENCES entrega(id_entrega),
                id_categoria INT REFERENCES categoria(id_categoria),
                nome VARCHAR(100),
                quantidade INT,
                unidade VARCHAR(20),
                data_validade DATE
            );
        """)
        conn.commit()

def deletar_tabelas():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")
        conn.commit()
