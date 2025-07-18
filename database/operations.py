from database.connection import conectar


# Inserir usuário
def inserir_usuario(nome, email, tipo, telefone, cpf_cnpj, senha):
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO usuario (nome, email, tipo_usuario, telefone, cpf_cnpj, senha)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (nome, email, tipo, telefone, cpf_cnpj, senha))
        conn.commit()
        print("Usuário inserido com sucesso.")

# Listar usuários
def listar_usuarios():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM usuario;")
        resultados = cur.fetchall()
        if resultados:
            print("\n--- Lista de Usuários ---")
            for linha in resultados:
                print(linha)
        else:
            print("Nenhum usuário encontrado.")

# Atualizar nome de usuário
def atualizar_nome_usuario():
    id_usuario = input("Digite o ID do usuário que deseja atualizar: ")
    novo_nome = input("Digite o novo nome: ")
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("UPDATE usuario SET nome = %s WHERE id_usuario = %s", (novo_nome, id_usuario))
        conn.commit()
        print("Nome atualizado com sucesso.")

# Deletar usuário
def deletar_usuario():
    id_usuario = input("Digite o ID do usuário que deseja deletar: ")
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM usuario WHERE id_usuario = %s", (id_usuario,))
        conn.commit()
        print("Usuário deletado com sucesso.")

def inserir_instituicao():
    id_usuario = input("ID do usuário responsável: ")
    cnpj = input("CNPJ da instituição: ")
    nome_fantasia = input("Nome fantasia: ")
    responsavel = input("Nome do responsável: ")
    area_atuacao = input("Área de atuação: ")
    aceita = input("Aceita doações com valor? (s/n): ").strip().lower() == 's'

    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO instituicao (id_usuario, cnpj, nome_fantasia, responsavel, area_atuacao, aceita_doacao_com_valor)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (id_usuario, cnpj, nome_fantasia, responsavel, area_atuacao, aceita))
        conn.commit()
        print("Instituição inserida com sucesso.")

# Listar instituições
def listar_instituicoes():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM instituicao;")
        resultados = cur.fetchall()
        if resultados:
            print("\n--- Lista de Instituições ---")
            for linha in resultados:
                print(linha)
        else:
            print("Nenhuma instituição encontrada.")

# Inserir categoria
def inserir_categoria():
    nome = input("Nome da categoria: ")
    descricao = input("Descrição: ")
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO categoria (nome, descricao)
            VALUES (%s, %s)
        """, (nome, descricao))
        conn.commit()
        print("Categoria inserida com sucesso.")
# Listar categorias
def listar_categorias():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM categoria;")
        categorias = cur.fetchall()
        if categorias:
            print("\n--- Lista de Categorias ---")
            for cat in categorias:
                print(cat)
        else:
            print("Nenhuma categoria encontrada.")


# Inserir motorista
def inserir_motorista():
    id_usuario = input("Digite o ID do usuário que será motorista: ")
    cnh = input("Digite o número da CNH do motorista: ")
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO motorista (id_motorista, cnh)
            VALUES (%s, %s)
        """, (id_usuario, cnh))
        conn.commit()
        print("Motorista cadastrado com sucesso.")

# Inserir doação
def inserir_doacao():
    id_usuario = input("ID do usuário doador: ")
    id_instituicao = input("ID da instituição: ")
    descricao = input("Descrição da doação: ")
    tipo_doacao = input("Tipo da doação: ")
    preco_estimado = input("Preço estimado: ")
    status_aceitacao = input("Status (pendente/aceita/recusada): ")
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO doacao (id_usuario_doador, id_instituicao, descricao, tipo_doacao, preco_estimado, status_aceitacao, data_doacao)
            VALUES (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP)
        """, (id_usuario, id_instituicao, descricao, tipo_doacao, preco_estimado, status_aceitacao))
        conn.commit()
        print("Doação inserida com sucesso.")

# Inserir produto
def inserir_produto():
    id_entrega = input("ID da entrega: ")
    id_categoria = input("ID da categoria: ")
    nome = input("Nome do produto: ")
    quantidade = input("Quantidade: ")
    validade = input("Validade (YYYY-MM-DD): ")
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO produto (id_entrega, id_categoria, nome, quantidade, validade)
            VALUES (%s, %s, %s, %s, %s)
        """, (id_entrega, id_categoria, nome, quantidade, validade))
        conn.commit()
        print("Produto inserido com sucesso.")

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
>>>>>>> b51b98fb48f76119eedd3060b53dc851393fab03
