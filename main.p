
from database import schema, operations, consultas
from ia import usar_ia

def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Criar Tabelas e Carga Inicial")
        print("2. Inserir Usuário")
        print("3. Listar Usuários")
        print("4. Atualizar Nome de Usuário")
        print("5. Deletar Usuário")
        print("6. Inserir Instituição")
        print("7. Listar Instituições")
        print("8. Inserir Categoria")
        print("9. Inserir Motorista")
        print("10. Inserir Doação")
        print("11. Inserir Produto")
        print("12. Consulta 1: Produtos por Categoria")
        print("13. Consulta 2: Doações por Instituição")
        print("14. Consulta 3: Coletas por Motorista")
        print("15. Excluir TODAS as Tabelas")
        print("16. IA Generativa")
        print("0. Sair")

        escolha = input("Escolha: ")

        if escolha == "1":
            schema.criar_tabelas_e_carga_inicial()

        elif escolha == "2":
            nome = input("Nome: ")
            email = input("E-mail: ")
            tipo = input("Tipo (doador/receptor/motorista): ")
            telefone = input("Telefone: ")
            cpf_cnpj = input("CPF ou CNPJ: ")
            senha = input("Senha: ")
            operations.inserir_usuario(nome, email, tipo, telefone, cpf_cnpj, senha)

        elif escolha == "3":
            operations.listar_usuarios()

        elif escolha == "4":
            id_usuario = int(input("ID do usuário a atualizar: "))
            novo_nome = input("Novo nome: ")
            operations.atualizar_nome_usuario(id_usuario, novo_nome)

        elif escolha == "5":
            id_usuario = int(input("ID do usuário a deletar: "))
            operations.deletar_usuario(id_usuario)

        elif escolha == "6":
            operations.inserir_instituicao()

        elif escolha == "7":
            operations.listar_instituicoes()

        elif escolha == "8":
            operations.inserir_categoria()

        elif escolha == "9":
            operations.inserir_motorista()

        elif escolha == "10":
            operations.inserir_doacao()

        elif escolha == "11":
            operations.inserir_produto()

        elif escolha == "12":
            consultas.consulta1_produtos_por_categoria()

        elif escolha == "13":
            consultas.consulta2_doacoes_por_instituicao()

        elif escolha == "14":
            consultas.consulta3_coletas_por_motorista()

        elif escolha == "15":
            schema.excluir_tabelas()

        elif escolha == "16":
            pergunta = input("\n\U0001F916 Assistente IA\nDigite sua pergunta (ou 'sair' para voltar ao menu):\n>>> ")
            if pergunta.lower() != 'sair':
                try:
                    resposta = usar_ia(pergunta)
                    print("\nResposta da IA:\n", resposta)
                except Exception as e:
                    print(f"❌ Erro ao chamar a IA: {e}")

        elif escolha == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
