import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Conexão com o banco
conn = psycopg2.connect(
    dbname="benedito",
    user="postgres",
    password="ShyvatuanSpin13",
    host="localhost",
    port="5432"
)

# Consulta
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
conn.close()

# Gráfico
plt.figure(figsize=(10, 6))
plt.bar(df['instituicao'], df['total_doacoes'])
plt.title("Total de Doações por Instituição")
plt.xlabel("Instituição")
plt.ylabel("Quantidade de Doações")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_doacoes_instituicao.png")
print("Gráfico salvo como 'grafico_doacoes_instituicao.png'")
