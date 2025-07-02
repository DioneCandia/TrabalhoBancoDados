from database import schema, operations, consultas

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
        print("8. Consulta 1: Produtos por Categoria")
        print("9. Excluir TODAS as Tabelas")
        print("10. Consulta 2: Doações por Instituição")
        print("11. Consulta 3: Coletas por Motorista")
        print("0. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            schema.criar_tabelas()
        elif opcao == "2":
            nome = input("Nome: ")
            email = input("Email: ")
            tipo = input("Tipo (doador, receptor, etc): ")
            telefone = input("Telefone: ")
            cpf_cnpj = input("CPF/CNPJ: ")
            operations.inserir_usuario(nome, email, tipo, telefone, cpf_cnpj)
        elif opcao == "3":
            for u in operations.listar_usuarios():
                print(u)
        elif opcao == "4":
            id_usuario = input("ID do usuário: ")
            novo_nome = input("Novo nome: ")
            operations.atualizar_usuario(id_usuario, novo_nome)
        elif opcao == "5":
            id_usuario = input("ID do usuário a deletar: ")
            operations.deletar_usuario(id_usuario)
        elif opcao == "6":
            nome_fantasia = input("Nome da Instituição: ")
            responsavel = input("Responsável: ")
            area = input("Área de atuação: ")
            aceita = input("Aceita doações com valor? (True/False): ")
            id_usuario = input("ID do usuário vinculado: ")
            cnpj = input("CNPJ: ")
            operations.inserir_instituicao(id_usuario, cnpj, nome_fantasia, responsavel, area, aceita)
        elif opcao == "7":
            for i in operations.listar_instituicoes():
                print(i)
        elif opcao == "8":
            consultas.consulta1_produtos_por_categoria()
        elif opcao == "9":
            schema.deletar_tabelas()
        elif opcao == "10":
            consultas.consulta2_doacoes_por_instituicao()
        elif opcao == "11":
            consultas.consulta3_coletas_por_motorista()
        elif opcao == "12":
            nome = input("Nome da categoria: ")
            desc = input("Descrição: ")
            operations.inserir_categoria(nome, desc)

            

        elif opcao == "0":
            break

if __name__ == "__main__":
    menu()
