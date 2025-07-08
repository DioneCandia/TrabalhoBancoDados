import pandas as pd
import matplotlib.pyplot as plt
from .connection import conectar

def consulta1_produtos_por_categoria():
    conn = conectar()
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
    conn.close()

    print("\n=== Consulta 1: Total de Produtos por Categoria ===")
    print(df)

    df.plot(kind='bar', x='categoria', y='total_entregue', legend=False)
    plt.title("Total de Produtos Entregues por Categoria")
    plt.ylabel("Quantidade")
    plt.xlabel("Categoria")
    plt.tight_layout()
    plt.show()


def consulta2_doacoes_por_instituicao():
    conn = conectar()
    query = """
        SELECT
            i.nome_fantasia AS instituicao,
            COUNT(r.id_recebimento) AS total_doacoes,
            SUM(d.preco_estimado) AS valor_estimado_total
        FROM recebimento r
        JOIN doacao d ON r.id_doacao = d.id_doacao
        JOIN instituicao i ON r.id_instituicao = i.id_instituicao
        WHERE r.aceita_doacao = TRUE
        GROUP BY i.nome_fantasia
        ORDER BY total_doacoes DESC;
    """
    df = pd.read_sql(query, conn)
    conn.close()

    print("\n=== Consulta 2: Total de Doações por Instituição ===")
    print(df)

    df.plot(kind='bar', x='instituicao', y='total_doacoes', legend=False)
    plt.title("Total de Doações por Instituição Receptora")
    plt.ylabel("Total de Doações")
    plt.xlabel("Instituição")
    plt.tight_layout()
    plt.show()


def consulta3_coletas_por_motorista():
    conn = conectar()
    query = """
        SELECT
            u.nome AS motorista,
            COUNT(a.id_agendamento) AS total_coletas,
            SUM(p.quantidade) AS total_produtos
        FROM agenda_coleta a
        JOIN motorista m ON a.id_motorista = m.id_motorista
        JOIN usuario u ON m.id_usuario = u.id_usuario
        JOIN entrega e ON a.id_agendamento = e.id_agendamento
        JOIN produto p ON e.id_entrega = p.id_entrega
        WHERE a.data_coleta >= CURRENT_DATE - INTERVAL '30 days'
          AND a.status = 'realizada'
        GROUP BY u.nome
        ORDER BY total_coletas DESC;
    """
    df = pd.read_sql(query, conn)
    conn.close()

    print("\n=== Consulta 3: Coletas por Motorista (últimos 30 dias) ===")
    print(df)

    df.plot(kind='bar', x='motorista', y='total_coletas', legend=False)
    plt.title("Total de Coletas por Motorista (últimos 30 dias)")
    plt.ylabel("Total de Coletas")
    plt.xlabel("Motorista")
    plt.tight_layout()
    plt.show()
