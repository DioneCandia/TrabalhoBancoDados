from database.connection import conectar

# Inserir usuário
def inserir_usuario(nome, email, tipo, telefone, cpf_cnpj, senha):
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO usuario (nome, email, tipo_usuario, telefone, cpf_cnpj, senha)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (nome, email, tipo, telefone, cpf_cnpj, senha))
        conn.commit()
        print("Usuário inserido com sucesso.")

# Listar todos os usuários
def listar_usuarios():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM usuario;")
        resultados = cur.fetchall()
        if resultados:
            print("\n=== Lista de Usuários ===")
            for linha in resultados:
                print(linha)
        else:
            print("Nenhum usuário encontrado.")

# Atualizar nome de usuário
def atualizar_nome_usuario():
    id_usuario = input("ID do usuário a ser atualizado: ")
    novo_nome = input("Novo nome: ")
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            UPDATE usuario SET nome = %s WHERE id_usuario = %s;
        """, (novo_nome, id_usuario))
        conn.commit()
        print("Nome atualizado com sucesso.")

# Deletar usuário
def deletar_usuario():
    id_usuario = input("ID do usuário a ser deletado: ")
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM usuario WHERE id_usuario = %s;", (id_usuario,))
        conn.commit()
        print("Usuário deletado com sucesso.")

# Inserir instituição
def inserir_instituicao():
    nome = input("Nome da instituição: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO instituicao (nome, endereco, telefone, email)
            VALUES (%s, %s, %s, %s);
        """, (nome, endereco, telefone, email))
        conn.commit()
        print("Instituição inserida com sucesso.")

# Listar todas as instituições
def listar_instituicoes():
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM instituicao;")
        resultados = cur.fetchall()
        if resultados:
            print("\n=== Lista de Instituições ===")
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
            VALUES (%s, %s);
        """, (nome, descricao))
        conn.commit()
        print("Categoria inserida com sucesso.")

# Inserir motorista
def inserir_motorista():
    id_usuario = input("ID do usuário que será motorista: ")
    cnh = input("Número da CNH: ")
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO motorista (id_motorista, cnh)
            VALUES (%s, %s);
        """, (id_usuario, cnh))
        conn.commit()
        print("Motorista inserido com sucesso.")

# Inserir doação
def inserir_doacao():
    id_usuario_doador = input("ID do usuário doador: ")
    descricao = input("Descrição da doação: ")
    data = input("Data da doação (YYYY-MM-DD): ")
    tipo = input("Tipo da doação: ")
    preco = input("Preço estimado: ")
    status = input("Status da aceitação (aceita/recusada/pendente): ")
    id_instituicao = input("ID da instituição receptora: ")
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO doacao (id_usuario_doador, descricao, data_doacao, tipo_doacao, preco_estimado, status_aceitacao, id_instituicao)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """, (id_usuario_doador, descricao, data, tipo, preco, status, id_instituicao))
        conn.commit()
        print("Doação inserida com sucesso.")

# Inserir produto
def inserir_produto():
    id_entrega = input("ID da entrega: ")
    id_categoria = input("ID da categoria: ")
    nome = input("Nome do produto: ")
    quantidade = input("Quantidade: ")
    validade = input("Data de validade (YYYY-MM-DD): ")
    with conectar() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO produto (id_entrega, id_categoria, nome, quantidade, validade)
            VALUES (%s, %s, %s, %s, %s);
        """, (id_entrega, id_categoria, nome, quantidade, validade))
        conn.commit()
        print("Produto inserido com sucesso.")
