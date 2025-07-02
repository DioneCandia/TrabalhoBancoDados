import pandas as pd
import matplotlib.pyplot as plt
from database.connection import conectar

# CONSULTA 1 – Total de Produtos Entregues por Categoria
def consulta1_produtos_por_categoria():
    with conectar() as conn:
        df = pd.read_sql("""
            SELECT
                c.nome AS categoria,
                SUM(p.quantidade) AS total_entregue
            FROM produto p
            JOIN categoria c ON p.id_categoria = c.id_categoria
            JOIN entrega e ON p.id_entrega = e.id_entrega
            WHERE e.status_entrega = 'entregue'
            GROUP BY c.nome
            ORDER BY total_entregue DESC;
        """, conn)

    print("\n=== Consulta 1: Total de Produtos Entregues por Categoria ===")
    print(df.to_string(index=False))

    df.plot(kind='bar', x='categoria', y='total_entregue', legend=False)
    plt.title("Total de Produtos Entregues por Categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# CONSULTA 2 – Total de Doações por Instituição Receptora
def consulta2_doacoes_por_instituicao():
    with conectar() as conn:
        df = pd.read_sql("""
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
        """, conn)

    print("\n=== Consulta 2: Total de Doações por Instituição Receptora ===")
    print(df.to_string(index=False))

    df.plot(kind='bar', x='instituicao', y='valor_estimado_total', legend=False)
    plt.title("Valor Estimado Total de Doações por Instituição")
    plt.xlabel("Instituição")
    plt.ylabel("Valor Estimado (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# CONSULTA 3 – Volume de Coletas por Motorista nos Últimos 30 Dias
def consulta3_coletas_por_motorista():
    with conectar() as conn:
        df = pd.read_sql("""
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
        """, conn)

    print("\n=== Consulta 3: Volume de Coletas por Motorista (últimos 30 dias) ===")
    print(df.to_string(index=False))

    df.plot(kind='bar', x='motorista', y='total_produtos', legend=False)
    plt.title("Total de Produtos Coletados por Motorista (últimos 30 dias)")
    plt.xlabel("Motorista")
    plt.ylabel("Total de Produtos Coletados")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

