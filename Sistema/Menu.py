from datetime import datetime
from Categoria import Categoria
from Cliente import Cliente
from Produto import Produto
from Cartao import Cartao
from Venda import Venda

"""
Classe para representar a função do menu de interação com o usuário do sistema de Loja.
"""
cartao_class = Cartao()
categoria_class = Categoria()
produto_class = Produto()
cliente_class = Cliente()
venda_class = Venda()
carrinho = []
total = 0


def run():
    """

    """
    while True:
        print("*" * 100)
        print("Menu Principal:\n")
        print("\t1) Nova Venda")
        print("\t2) Produtos")
        print("\t3) Consultas")
        print("\t4) Cadastro de Cliente")
        print("\t5) Sair\n")
        opcao_menu_principal = input("Selecione uma opção:\n")
        print("-" * 100)
        if opcao_menu_principal == "1":
            carrinho.clear()
            cpf_user = input("Digite seu CPF (somente números): ")
            if len(cpf_user) != 11:
                print("CPF inválido!")
            else:
                if cliente_class.verificar_cliente(cpf_user):
                    for i in cliente_class.listar_clientes():
                        if i['cpf'] == cpf_user:
                            print(f"Bem Vindo {i['nome']}!")
                            break
                    menu_vendas()
                else:
                    novo_cadastro = input("CPF não cadastrado, deseja cadastrar? \n 1) Sim\n 2) Não\n")
                    if novo_cadastro == '1':
                        menu_cadastrar_cliente()
                        menu_vendas()

                    elif novo_cadastro == "2":
                        menu_vendas()
                    else:
                        print("Opção inválida!")

        elif opcao_menu_principal == "2":
            menu_produtos()

        elif opcao_menu_principal == "3":
            menu_consultas()
            
        elif opcao_menu_principal == "4":
            menu_cadastrar_cliente()

        elif opcao_menu_principal == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


def menu_vendas():
    """

    """
    while True:
        print("-" * 100)
        print("Menu venda:\n")
        print("1) Adicionar Produto")
        print("2) Deletar Produto")
        print("3) Receber Pagamento")
        print("4) Cancelar compra")
        opcao_menu_venda = input("Selecione uma opção:\n")

        if opcao_menu_venda == "1":
            print("-" * 100)
            print("Adicionando produtos no carrinho...")
            if not produto_class.listar_produtos():
                print("Nenhum produto cadastrado!")
            else:
                categoria_selecionada = "None"
                lista_categorias = categoria_class.listar_categorias()
                ok = False
                if not lista_categorias:
                    ok = True
                else:
                    print("Categorias cadastradas:\n")
                    for cat in range(0, len(lista_categorias)):
                        print(f"{cat + 1}) {lista_categorias[cat]}")
                    opcao_categoria = input("Os produtos de qual categoria deseja ver?\n")
                    try:
                        categoria_selecionada = lista_categorias[int(opcao_categoria) - 1]
                        ok = True
                    except:
                        print("Opção inválida!")
                if ok:
                    produtos_categoria = produto_class.pesquisar_produtos(categoria_selecionada)
                    if not produtos_categoria:
                        print("Nenhum produto encontrado!")
                    else:
                        print("ID |\tNome |\tPreço")
                        for prod in range(len(produtos_categoria)):
                            print(f"{prod + 1}) |\t{produtos_categoria[prod]['nome']} |\t{produtos_categoria[prod]['preco']}")
                        add_prod = input("Selecione o produto para adicionar ao carrinho:\n")
                        try:
                            carrinho.append(produtos_categoria[int(add_prod) - 1])
                            print("Produtos no carrinho:")
                            print("ID |\tNome |\tPreço |\tCategoria")
                            for prod in range(len(carrinho)):
                                print(
                                    f"{prod + 1}) |\t{carrinho[prod]['nome']} |\t{carrinho[prod]['preco']} "
                                    f"|\t{carrinho[prod]['categoria']}")
                        except:
                            print("Este item não está na lista!")
                            pass

        elif opcao_menu_venda == "2":
            print("-" * 100)
            print("Produtos no carrinho:")
            print("ID |\tNome |\tPreço |\tCategoria")
            for prod in range(len(carrinho)):
                print(
                    f"{prod + 1}) |\t{carrinho[prod]['nome']} |\t{carrinho[prod]['preco']} "
                    f"|\t{carrinho[prod]['categoria']}")
            del_produto = input("Qual produto deseja excluir?\n")
            try:
                carrinho.pop(int(del_produto) - 1)
                print("Item excluido!")
            except:
                print("Item não encontrado!")
                pass

        elif opcao_menu_venda == "3":
            print("-" * 100)
            print("Realizar Pagamento:")
            total = 0
            for i in carrinho:
                total += int(i["preco"])
            print(f"O preço total da compra é R${total:0.2f}")
            if total == 0:
                print("O carrinho está vazio! Adicione produtos antes de finalizar a compra!")
            else:
                forma_pagamento = input("Selecione a forma de pagamento:\n 1) Dinheiro\n 2) Cartão\n")
                if forma_pagamento == "1":
                    pagar = input("Insira quantos reais você usará para pagar a compra?\n")
                    try:
                        if float(pagar) >= total:
                            troco = float(pagar) - total
                            print(f"Seu troco foi de R${troco}")
                            venda = {"data_hora": str(datetime.today()), "itens_venda": carrinho,
                                     "total_venda": total}
                            venda_class.cadastrar_venda(venda)
                            print("Venda finalizada!")
                            break
                        else:
                            print("Valor insuficiente!")
                    except:
                        print("O valor digitado não é valido!")

                elif forma_pagamento == "2":
                    numero_cartao = input("Informe o numero do cartão: ")
                    senha_cartao = input("Informe a senha do cartão: ")

                    resposta = cartao_class.verificar_cartao(numero_cartao, senha_cartao, total)

                    if resposta == 1:
                        print("Saldo insuficiente!")
                    elif resposta == 2:
                        print("Validade do cartão expirada!")
                    elif resposta == 3:
                        print("Senha incorreta!")
                    elif resposta == 4:
                        print("Número de cartão inválido!")
                    else:
                        print("Compra realizado com sucesso!")
                        venda = {"data_hora": str(datetime.today()), "itens_venda": carrinho,
                                 "total_venda": total}
                        venda_class.cadastrar_venda(venda)
                        print("Venda finalizada!")
                        break
                else:
                    print("Forma de pagamento Inválida!")

        elif opcao_menu_venda == "4":
            print("-" * 100)
            print("Compra cancelada!")
            break

        else:
            print("Opção inválida")


def menu_produtos():
    """

    """
    while True:
        print("-" * 100)
        print("Menu produtos:\n")
        print("\t1) Cadastrar novo produto")
        print("\t2) Cadastrar nova categoria")
        print("\t3) Alterar Produto")
        print("\t4) Listar produtos")
        print("\t5) Listar categorias")
        print("\t6) Deletar produto")
        print("\t7) Deletar categoria")
        print("\t8) Voltar ao Menu Principal")
        opcao_menu_produtos = input("Selecione uma opção:\n")

        if opcao_menu_produtos == "1":
            print("-" * 100)
            print("Cadastrando novo produto...")
            codigo_produto = input("Qual o codigo do produto: ")
            if len(codigo_produto.strip()) == 0:
                print("Código inválido!")
            elif produto_class.verificar_produto(codigo_produto):
                print("Código já cadastrado!")
            else:
                nome_produto = input("Qual o nome do produto: ")
                if len(nome_produto.strip()) == 0:
                    print("Nome inválido!")
                else:
                    preco_produto = input("Qual o preço do produto: ")
                    ok = False
                    try:
                        if float(preco_produto) > 0:
                            ok = True
                        else:
                            print("Preço inválido!")
                    except:
                        print("Preço inválido!")
                    if ok:
                        categoria_produto = "None"
                        ok = False
                        categorias = categoria_class.listar_categorias()
                        if not categorias:
                            ok = True
                        else:
                            print("-" * 100)
                            print("Categorias cadastradas:")
                            for i in range(0, len(categorias)):
                                print(f"{i + 1}) {categorias[i]}")
                            try:
                                categoria_produto = categorias[
                                    int(input("Escolha a categoria do produto a ser cadastrado: ")) - 1]
                                ok = True
                            except:
                                print("Opção inválida!")
                        if ok:
                            novo_produto = {"codigo": codigo_produto, "nome": nome_produto, "preco": preco_produto,
                                            "categoria": categoria_produto}
                            if produto_class.cadastrar_produto(novo_produto):
                                print("Produto cadastrado com sucesso!")
                            else:
                                print("Erro ao cadastrar o novo produto!")

        elif opcao_menu_produtos == "2":
            print("-" * 100)
            print("Cadastrando nova categoria...")
            nome_categoria = input("Digite o nome da categoria que deseja cadastrar: ")
            if nome_categoria.strip() == "":
                print("Categoria inválida!")
            else:
                if categoria_class.cadastrar_categoria(nome_categoria):
                    print("Categoria cadastrada com sucesso!")
                else:
                    print("Erro ao cadastrar nova categoria!")

        elif opcao_menu_produtos == "3":
            print("-" * 100)
            print("Alterando produtos...")
            produtos = produto_class.listar_produtos()
            print("Produtos cadastrados:")
            if not produtos:
                print("Nenhum produto cadastrado!")
            else:
                print("Codigo |\t Nome |\tPreço |\t Categoria")
                for p in produtos:
                    print(f"{p['codigo']} |\t{p['nome']} |\t{p['preco']} |\t{p['categoria']}")
                print("-" * 100)

                codigo_produto_alterado = input("Qual o codigo do produto?\n")
                if not produto_class.verificar_produto(codigo_produto_alterado):
                    print("Código não encontrado!")
                else:
                    nome_produto_alterado = input("Qual o nome do produto?\n")
                    if nome_produto_alterado.strip() == "":
                        print("Nome inválido!")
                    else:
                        ok = False
                        preco_produto_alterado = input("Qual o preço do produto: ")
                        try:
                            if float(preco_produto_alterado) > 0:
                                ok = True
                            else:
                                print("Preço inválido!")
                        except:
                            print("Preço inválido!")
                        if ok:
                            categoria_produto_alterado = "None"
                            categorias = categoria_class.listar_categorias()
                            if categorias:
                                ok = False
                                print("Categorias cadastradas:")
                                for i in range(0, len(categorias)):
                                    print(f"{i + 1}) {categorias[i]}")
                                try:
                                    categoria_produto_alterado = categorias[
                                        int(input("Escolha a nova categoria do produto:\n")) - 1]
                                    ok = True
                                except:
                                    print("Opção inválida!")
                                if ok:
                                    produto_alterado = {"codigo": codigo_produto_alterado,
                                        "nome": nome_produto_alterado,
                                        "preco": preco_produto_alterado,
                                        "categoria": categoria_produto_alterado}
                                    if produto_class.alterar_produto(produto_alterado):
                                        print("Produto alterado com sucesso!")
                                    else:
                                        print("Erro ao alterar o produto!")

        elif opcao_menu_produtos == "4":
            print("-" * 100)
            print("Produtos cadastrados:\n")
            lista_produtos = produto_class.listar_produtos()
            if not lista_produtos:
                print("Nenhum produto cadastrado!")
            else:
                print("Codigo |\t Nome |\tPreço |\t Categoria")
                for prod in lista_produtos:
                    print(f"{prod['codigo']} |\t{prod['nome']} |\t{prod['preco']} |\t{prod['categoria']}")

        elif opcao_menu_produtos == "5":
            print("-" * 100)
            print("Categorias cadastradas:\n")
            lista_categorias = categoria_class.listar_categorias()
            if not lista_categorias:
                print("Nenhuma categoria cadastrada!")
            else:
                print("Nome:")
                for cat in lista_categorias:
                    print(f"{cat}")

        elif opcao_menu_produtos == "6":
            print("-" * 100)
            print("Produtos cadastrados:\n")
            lista_produtos = produto_class.listar_produtos()
            if not lista_produtos:
                print("Nenhum produto cadastrado!")
            else:
                print("Codigo |\t Nome |\tPreço |\t Categoria")
                for prod in lista_produtos:
                    print(f"{prod['codigo']} |\t{prod['nome']} |\t{prod['preco']} |\t{prod['categoria']}")
                print("-" * 100)
                codigo_produto = input("Informe o codigo do produto que deseja deletar:\n")
                if produto_class.excluir_produto(codigo_produto):
                    print("Produto deletado com sucesso!")
                else:
                    print("Produto não encontrado!")

        elif opcao_menu_produtos == "7":
            print("-" * 100)
            print("Categorias cadastradas:\n")
            lista_categorias = categoria_class.listar_categorias()
            if not lista_categorias:
                print("Nenhuma categoria cadastrada!")
            else:
                for cat in range(len(lista_categorias)):
                    print(f"{cat + 1}) {lista_categorias[cat]}")
                try:
                    num_categoria = int(input("Digite o número da categoria que deseja excluir: "))
                    if categoria_class.excluir_categoria(lista_categorias[int(num_categoria) - 1]):
                        print("Categoria deletada com sucesso")
                    else:
                        print("Categoria não encontrada!")
                except:
                    print("Número inválido!")

        elif opcao_menu_produtos == "8":
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida")


def menu_consultas():
    """

    """
    while True:
        print("-" * 100)
        print("Menu consultas:\n")
        print("\t1) Listar Clientes cadastrados")
        print("\t2) Histórico de Vendas")
        print("\t3) Voltar ao menu principal")
        opcao_menu_consultas = input("Selecione uma opção:\n")
        if opcao_menu_consultas == "1":
            clientes = cliente_class.listar_clientes()
            if not clientes:
                print("Nenhum cliente cadastrado!")
            else:
                print(f"Nome\t\tCPF\t\tIdade")
                for cliente in clientes:
                    print(f"{cliente['nome']}\t\t{cliente['cpf']}\t\t{cliente['idade']}")
                print("\n")
        elif opcao_menu_consultas == "2":
            vendas = venda_class.listar_vendas()
            if not vendas:
                print("O histórico de vendas está vazio!")
            else:
                print("Vendas efetuadas:")
                print("." * 100)
                for v in vendas:
                    print(f"\tData e hora: {v['data_hora']}")
                    print(f"\tValor Total: {v['total_venda']}")
                    print("\tItens da Venda:")
                    for i in v['itens_venda']:
                        print(
                            f"\t\tCodigo: {i['codigo']} \tNome: {i['nome']} \tPreço: {i['preco']} \tCategoria: {i['categoria']}")
                    print("." * 100)
        elif opcao_menu_consultas == "3":
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida")


def menu_cadastrar_cliente():
    """
    Método para interação com o usuário quando for necessário cadastrar um novo cliente.
    Realiza validações de entrada de dados.
    """
    print("-" * 100)
    print("Cadastrando cliente...")
    cpf_cliente = input("Digite seu CPF (somente números): ")
    if len(cpf_cliente) != 11:
        print("CPF inválido!")
    else:
        nome_cliente = input("Digite seu nome: ")
        if nome_cliente.strip() == "":
            print("Nome inválido!")
        else:
            ok = False
            idade_cliente = input("Digite sua idade: ")
            try:
                if int(idade_cliente) > 0:
                    ok = True
                else:
                    print("Valor inválido!")
            except:
                print("Valor inválido!")
            if ok:
                novo_cliente = {"nome": nome_cliente, "cpf": cpf_cliente, "idade": idade_cliente}
                if cliente_class.cadastrar_cliente(novo_cliente):
                    print(f"Bem Vindo {novo_cliente['nome']}!")
                else:
                    print("Ocorreu um erro ao cadastrar o novo cliente!")


if __name__ == "__main__":
    print("Iniciando sistema...")
    run()
