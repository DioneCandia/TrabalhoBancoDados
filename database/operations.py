from database.connection import conectar

def inserir_usuario(nome, email, tipo, telefone, cpf_cnpj):
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO usuario (nome, email, tipo_usuario, telefone, cpf_cnpj, senha)
            VALUES (%s, %s, %s, %s, %s, 'senha123');
        """, (nome, email, tipo, telefone, cpf_cnpj))
        conn.commit()

def listar_usuarios():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM usuario;")
        return cur.fetchall()

def atualizar_usuario(id_usuario, novo_nome):
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("UPDATE usuario SET nome = %s WHERE id_usuario = %s;", (novo_nome, id_usuario))
        conn.commit()

def inserir_categoria(nome, descricao):
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO categoria (nome, descricao)
            VALUES (%s, %s);
        """, (nome, descricao))
        conn.commit()

def listar_categorias():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM categoria;")
        return cur.fetchall()
def inserir_motorista(id_usuario, cnh, veiculo, placa):
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO motorista (id_usuario, cnh, veiculo, placa_veiculo)
            VALUES (%s, %s, %s, %s);
        """, (id_usuario, cnh, veiculo, placa))
        conn.commit()

def listar_motoristas():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM motorista;")
        return cur.fetchall()

def inserir_produto(id_entrega, id_categoria, nome, quantidade, unidade, validade):
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO produto (id_entrega, id_categoria, nome, quantidade, unidade, data_validade)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (id_entrega, id_categoria, nome, quantidade, unidade, validade))
        conn.commit()

def listar_produtos():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM produto;")
        return cur.fetchall()

def inserir_doacao(id_usuario, id_instituicao, data, tipo, quantidade, valor):
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO doacao (id_usuario_doador, id_instituicao, data_doacao, tipo_doacao, quantidade, preco_estimado, status_aceitacao)
            VALUES (%s, %s, %s, %s, %s, %s, 'pendente');
        """, (id_usuario, id_instituicao, data, tipo, quantidade, valor))
        conn.commit()

def listar_doacoes():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM doacao;")
        return cur.fetchall()

def inserir_entrega(id_motorista, id_instituicao, data, status, tipo):
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO entrega (id_motorista, id_instituicao, data_entrega, status_entrega, tipo_entrega)
            VALUES (%s, %s, %s, %s, %s);
        """, (id_motorista, id_instituicao, data, status, tipo))
        conn.commit()

def listar_entregas():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM entrega;")
        return cur.fetchall()

def inserir_agendamento(id_motorista, id_doacao, data, status):
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO agenda_coleta (id_motorista, id_doacao, data_coleta, status)
            VALUES (%s, %s, %s, %s);
        """, (id_motorista, id_doacao, data, status))
        conn.commit()

def listar_agendamentos():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM agenda_coleta;")
        return cur.fetchall()

def inserir_recebimento(id_doacao, id_instituicao, data, aceita):
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO recebimento (id_doacao, id_instituicao, data_recebimento, aceita_doacao)
            VALUES (%s, %s, %s, %s);
        """, (id_doacao, id_instituicao, data, aceita))
        conn.commit()

def listar_recebimentos():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM recebimento;")
        return cur.fetchall()




def deletar_usuario(id_usuario):
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM usuario WHERE id_usuario = %s;", (id_usuario,))
        conn.commit()

def inserir_instituicao(id_usuario, cnpj, nome_fantasia, responsavel, area_atuacao, aceita_valor):
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO instituicao (id_usuario, cnpj, nome_fantasia, responsavel, area_atuacao, aceita_doacao_com_valor)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (id_usuario, cnpj, nome_fantasia, responsavel, area_atuacao, aceita_valor))
        conn.commit()

def listar_instituicoes():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM instituicao;")
        return cur.fetchall()
