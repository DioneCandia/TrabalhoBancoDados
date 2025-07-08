import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Conexão com o banco PostgreSQL
conn = psycopg2.connect(
    dbname="benedito",
    user="postgres",
    password="ShyvatuanSpin13",
    host="localhost",
    port="5432"
)

# Consulta 1: Produtos por Categoria
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

# Plotando o gráfico
plt.figure(figsize=(10, 6))
plt.bar(df['categoria'], df['total_entregue'])
plt.title("Total de Produtos Entregues por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Quantidade Entregue")
plt.xticks(rotation=45)
plt.tight_layout()

# Salvando a imagem
plt.savefig("grafico_categoria.png")
print("Gráfico salvo como 'grafico_categoria.png'")
