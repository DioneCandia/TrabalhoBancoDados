from database.connection import conectar


def criar_tabelas_e_carga_inicial():
    with conectar() as conn, conn.cursor() as cur:

        # Tabela usuario

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
                senha VARCHAR(100)
            );
        """)

        # Tabela instituicao
        cur.execute("""
            CREATE TABLE IF NOT EXISTS instituicao (
                id_instituicao SERIAL PRIMARY KEY,
                nome VARCHAR(100),
                cnpj VARCHAR(20),
                telefone VARCHAR(20),
                email VARCHAR(100),
                endereco TEXT
            );
        """)

        # Tabela categoria
        cur.execute("""

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

        """)

        # Tabela motorista (ligada a usuário)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS motorista (
                id_motorista INTEGER PRIMARY KEY REFERENCES usuario(id_usuario)
            );
        """)

        # Tabela doacao
        cur.execute("""
            CREATE TABLE IF NOT EXISTS doacao (
                id_doacao SERIAL PRIMARY KEY,
                id_usuario_doador INTEGER REFERENCES usuario(id_usuario),
                descricao TEXT,
                data_doacao TIMESTAMP,
                tipo_doacao VARCHAR(50),
                preco_estimado NUMERIC,
                status_aceitacao VARCHAR(20),
                justificativa_recusada TEXT,
                id_instituicao INTEGER REFERENCES instituicao(id_instituicao)
            );
        """)

        # Tabela agenda_coleta
        cur.execute("""
            CREATE TABLE IF NOT EXISTS agenda_coleta (
                id_agendamento SERIAL PRIMARY KEY,
                id_doacao INTEGER REFERENCES doacao(id_doacao),
                id_motorista INTEGER REFERENCES motorista(id_motorista),
                data_coleta DATE,
                horario_coleta TIME,
                status VARCHAR(20)
            );
        """)

        # Tabela entrega
        cur.execute("""
            CREATE TABLE IF NOT EXISTS entrega (
                id_entrega SERIAL PRIMARY KEY,
                id_agenda INTEGER REFERENCES agenda_coleta(id_agendamento),
                data_entrega TIMESTAMP,
                status_entrega VARCHAR(20),
                tipo_entrega VARCHAR(20)
            );
        """)

        # Tabela produto
        cur.execute("""
            CREATE TABLE IF NOT EXISTS produto (
                id_produto SERIAL PRIMARY KEY,
                id_entrega INTEGER REFERENCES entrega(id_entrega),
                id_categoria INTEGER REFERENCES categoria(id_categoria),
                nome VARCHAR(100),
                quantidade INTEGER
            );
        """)

        # Tabela recebimento
        cur.execute("""
            CREATE TABLE IF NOT EXISTS recebimento (
                id_recebimento SERIAL PRIMARY KEY,
                id_entrega INTEGER REFERENCES entrega(id_entrega),
                id_instituicao INTEGER REFERENCES instituicao(id_instituicao),
                data_recebimento TIMESTAMP
            );
        """)

        conn.commit()
        print("✅ Todas as tabelas foram criadas com sucesso.")


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
