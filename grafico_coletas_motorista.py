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
    u.nome AS motorista,
    COUNT(a.id_agenda) AS total_coletas
FROM agenda_coleta a
JOIN motorista m ON a.id_motorista = m.id_motorista
JOIN usuario u ON m.id_motorista = u.id_usuario
GROUP BY u.nome
ORDER BY total_coletas DESC;
"""

df = pd.read_sql(query, conn)
conn.close()

# Gráfico
plt.figure(figsize=(10, 6))
plt.bar(df['motorista'], df['total_coletas'])
plt.title("Total de Coletas por Motorista")
plt.xlabel("Motorista")
plt.ylabel("Quantidade de Coletas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_coletas_motorista.png")
print("Gráfico salvo como 'grafico_coletas_motorista.png'")
