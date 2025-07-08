# ia.py
from openai import OpenAI

def usar_ia(pergunta):
    try:
        with open("gpt-key.txt") as f:
            chave = f.read().strip()
        
        client = OpenAI(api_key=chave)
        
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente útil que responde de forma clara."},
                {"role": "user", "content": pergunta}
            ],
            temperature=0.7
        )

        return resposta.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Erro ao chamar a IA: \n\n{str(e)}"
