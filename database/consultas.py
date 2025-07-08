import pandas as pd
import matplotlib.pyplot as plt
from database.conexao import criar_conexao

def consulta1_produtos_por_categoria():
    print("\n=== Consulta 1: Total de Produtos por Categoria ===")
    conn = criar_conexao()
    if conn is None:
        return

    query = """
        SELECT
            c.nome AS categoria,
            SUM(p.quantidade) AS total_entregue
        FROM produto p
        JOIN categoria c ON p.id_categoria = c.id_categoria
        JOIN entrega e ON p.id_entrega = e.id_entrega
        WHERE e.status_entrega = 'entregue'
        GROUP BY c.nome
        ORDER BY total_entregue DESC;
    """

    df = pd.read_sql(query, conn)
    print(df)

    df.plot(kind='bar', x='categoria', y='total_entregue', legend=False)
    plt.title('Total de Produtos Entregues por Categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Total Entregue')
    plt.tight_layout()
    plt.show()

    conn.close()

def consulta2_doacoes_por_instituicao():
    print("\n=== Consulta 2: Total de Doações por Instituição Receptora ===")
    conn = criar_conexao()
    if conn is None:
        return

    query = """
        SELECT
            i.nome_fantasia AS instituicao,
            COUNT(r.id_recebimento) AS total_doacoes,
            SUM(d.preco_estimado) AS valor_estimado_total
        FROM recebimento r
        JOIN doacao d ON r.id_doacao = d.id_doacao
        JOIN instituicao i ON r.id_instituicao = i.id_instituicao
        GROUP BY i.nome_fantasia
        ORDER BY total_doacoes DESC;
    """

    df = pd.read_sql(query, conn)
    print(df)

    df.plot(kind='bar', x='instituicao', y='total_doacoes', legend=False)
    plt.title('Total de Doações por Instituição')
    plt.xlabel('Instituição')
    plt.ylabel('Total de Doações')
    plt.tight_layout()
    plt.show()

    conn.close()

def consulta3_coletas_por_motorista():
    import pandas as pd
    import matplotlib.pyplot as plt
    from database.connection import conectar

    query = """
        SELECT
            u.nome AS motorista,
            COUNT(ac.id_agendamento) AS total_coletas,
            COALESCE(SUM(p.quantidade), 0) AS total_produtos
        FROM agenda_coleta ac
        JOIN motorista m ON ac.id_motorista = m.id_motorista
        JOIN usuario u ON m.id_motorista = u.id_usuario
        LEFT JOIN entrega e ON ac.id_agendamento = e.id_agendamento
        LEFT JOIN produto p ON e.id_entrega = p.id_entrega
        WHERE ac.data_coleta >= CURRENT_DATE - INTERVAL '30 days'
        GROUP BY u.nome
        ORDER BY total_coletas DESC;
    """

    try:
        conn = conectar()
        df = pd.read_sql(query, conn)
        print(df)

        plt.figure(figsize=(10, 6))
        plt.bar(df["motorista"], df["total_coletas"], color='blue')
        plt.xlabel("Motorista")
        plt.ylabel("Total de Coletas")
        plt.title("Coletas por Motorista (últimos 30 dias)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("grafico_coletas_motorista.png")
        plt.show()

    except Exception as e:
        print("Erro ao executar a consulta:", e)
    finally:
        if conn:
            conn.close()
