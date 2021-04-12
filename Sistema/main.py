from datetime import datetime

import Categoria, Cliente, Produto, Cartao, Venda

carrinho = []
total = 0


def venda():
    while True:
        opcao2 = input("""--MENU DE PRODUTOS--
1) Adicionar Produto
2) Cancelar Produto
3) Receber Pagamento
4) Cancelar compra!
""")
        if opcao2 == "1":
            categorias = Categoria.listar_categorias()
            for cat in range(0, len(categorias)):
                print(f"{cat+1}) {categorias[cat]}")
            opcao_categoria = input("Os produtos de qual categoria deseja ver? ")
            selec_categoria = categorias[int(opcao_categoria) - 1]

            produtos_categoria = Produto.pesquisar_produtos(selec_categoria)
            if not produtos_categoria:
                print("Nenhum produto encontrado")
            else:
                for prod in range(len(produtos_categoria)):
                    print(f"{prod + 1}) {produtos_categoria[prod]['nome']}")

                add_prod = input("Selecione o produto para adicionar ao carrinho: ")
                if int(add_prod) > len(produtos_categoria):
                    print("Este item não está na lista")
                else:
                    carrinho.append(produtos_categoria[int(add_prod) - 1])
                    print(carrinho)
        elif opcao2 == "2":
            print("---Deletar Produto---")
            for produtos in range(0, len(carrinho)):
                print(f"{produtos+1}) {carrinho[produtos]}")
            del_produto = input("Qual produto deseja excluir? ")

            carrinho.pop(int(del_produto) - 1)
            print("Item excluido")

        elif opcao2 == "3":
            pagar_total = 0
            for i in carrinho:
                pagar_total += int(i["preco"])
            print(f"O preço total da compra é R${pagar_total:0.2f}")
            if pagar_total == 0:
                print("O carinho está vazio! Adicione produtos antes de finalizar a compra!")
            else:
                pagamento = input("Selecione a forma de pagamento:\n 1) Dinheiro\n 2) Cartão\n")
                if pagamento == "1":
                    pagar = input("Insira quantos reais você usará para pagar a compra? ")
                    try:
                        if float(pagar) >= pagar_total:
                            troco = float(pagar) - pagar_total
                            print(f"Seu troco foi de R${troco}")
                            venda = {"data_hora":str(datetime.today()),"itens_venda":carrinho,"total_venda":pagar_total}
                            Venda.cadastrar_venda(venda)
                            break
                        else:
                            print("Valor insuficiente\n")
                    except:
                        print("O valor digitado não é valido")
                elif pagamento == "2":
                    numero_cartao = input("Informe o numero do cartão: ")
                    senha_cartao = input("Informe a senha do cartão: ")

                    resposta = Cartao.verificar_cartao(numero_cartao, senha_cartao, pagar_total)

                    if resposta == 1:
                        print("Saldo insuficiente!")
                    elif resposta == 2:
                        print("Validade do cartão expirada!")
                    elif resposta == 3:
                        print("Senha incorreta!")
                    elif resposta == 4:
                        print("Número de cartão inválido!")
                    else:
                        print("Compra realizado com sucesso")
                        venda = {"data_hora": str(datetime.today()), "itens_venda": carrinho, "total_venda": pagar_total}
                        Venda.cadastrar_venda(venda)
                        break
                else:
                    print("Forma de pagamento Inválida")

        elif opcao2 == "4":
            print("Compra cancelada")
            print('-' * 50)
            break

        else:
            print("Opção inválida")


def produto():
    while True:
        opcao2 = input("""1) Cadastrar novo produto
2) Cadastrar nova categoria
3) Alterar Produto
4) Listar produtos
5) Listar categoria
6) Deletar produto
7) Deletar categoria
8) Voltar ao menu Principal

Selecione uma opção: """)
        if opcao2 == "1":
            categorias = Categoria.listar_categorias()
            if not categorias:
                print("Cadastre uma categoria antes de cadastrar um produto\n")
            else:
                for i in range(0, len(categorias)):
                    print(f"{i + 1}) {categorias[i]}")
                cat_produto = categorias[int(input("Escolha a categoria do produto a ser cadastrado: ")) - 1]
                print(cat_produto)

                produto = {"codigo": input("Qual o codigo do produto: "), "nome": input("Qual o nome do produto: "),
                           "preco": input("Qual o preço do produto: "), "categoria": cat_produto}
                Produto.cadastrar_produto(produto)
                print("Produto cadastrado com sucesso!!\n")
        elif opcao2 == "2":
            nome_categoria = input("Digite o nome da categoria que deseja cadastrar: ")
            Categoria.cadastrar_categoria(nome_categoria)
        elif opcao2 == "3":
            produtos = Produto.listar_produtos()
            print("Produtos cadastrados:")
            if not produtos:
                print("Nenhum produto cadastrado!")
            else:
                produto_alterado = {}
                print("Codigo |\t Nome |\tPreço |\t Categoria")
                for prod in produtos:
                    print(f"{prod['codigo']} |\t{prod['nome']} |\t{prod['preco']} |\t{prod['categoria']}")
                produto_alterado["codigo"] = input("Qual o codigo do produto")
                produto_alterado["nome"] = input("Qual o nome do produto? ")
                produto_alterado["preco"] = input("Qual o preço do produto? ")
                categorias = Categoria.listar_categorias()
                for i in range(0, len(categorias)):
                    print(f"{i + 1}) {categorias[i]}")
                cat_produto = categorias[int(input("Escolha a categoria do produto a ser cadastrado: ")) - 1]
                produto_alterado["categoria"] = cat_produto
                if Produto.alterar_produto(produto_alterado):
                    print("Produto alterado com sucesso!")
                else:
                    print("Produto não encontrado")

        elif opcao2 == "4":
            produtos = Produto.listar_produtos()
            print("Codigo |\t Nome |\tPreço |\t Categoria")
            for prod in produtos:
                print(f"{prod['codigo']} |\t{prod['nome']} |\t{prod['preco']} |\t{prod['categoria']}")
            print("-" * 50)
        elif opcao2 == "5":
            lista_categorias = Categoria.listar_categorias()
            print("Nome:")
            for cat in lista_categorias:
                print(f"{cat}")
            print("-" * 50)
        elif opcao2 == "6":
            produtos = Produto.listar_produtos()
            print("Codigo |\t Nome |\tPreço |\t Categoria")
            for prod in produtos:
                print(f"{prod['codigo']} |\t{prod['nome']} |\t{prod['preco']} |\t{prod['categoria']}")
            codigo_produto = input("Informe o codigo do produto que deseja deletar : ")
            if Produto.excluir_produto(codigo_produto):
                print("Produto deletado com sucesso")
            else:
                print("Produto não encontrado!")
        elif opcao2 == "7":
            lista_categorias = Categoria.listar_categorias()
            print("Categorias cadastradas")
            for cat in range(len(lista_categorias)):
                print(f"{cat + 1}) {lista_categorias[cat]}")
            try:
                num_categoria = int(input("Digite o número da categoria que deseja excluir: "))
                if Categoria.excluir_categoria(lista_categorias[int(num_categoria) - 1]):
                    print("Categoria deletada com sucesso")
                else:
                    print("Categoria não encontrada!")
            except:
                print("Número inválido!")
            print("-" * 50)
        elif opcao2 == "8":
            print("Voltando ao menu principal")
            break
        else:
            print("Opção inválida")

def criar_banco():
    with open("../BancoDados/clientes.txt", "a") as file:
        pass
    with open("../BancoDados/categorias.txt", "a") as file:
        pass
    with open("../BancoDados/produtos.txt", "a") as file:
        pass

while True:
    criar_banco()
    opcao = input("""1) Comprar 
2) Produtos
3) Consultas
4) Cadastro de Cliente
5) Sair

Selecione uma opção: """)

    if opcao == "1":
        carrinho.clear()
        cpf_user = input("Digite seu cpf: ")

        if Cliente.verificar_cliente(cpf_user):
            for i in Cliente.listar_clientes():
                if i['cpf'] == cpf_user:
                    print(f"Bem Vindo {i['nome']}")
            venda()
        else:
            cadastrar = input("cpf não cadastrado, deseja cadastrar? \n 1) sim\n 2) Não\n")
            if cadastrar == '1':
                print("--Cadastrando cliente--")
                cliente = {"nome": input("Digite seu nome: "), "cpf": input("Digite seu cpf: "),
                           "idade": input("Digite sua idade: ")}
                Cliente.cadastrar_cliente(cliente)
            elif cadastrar == "2":
                venda()
            else:
                print("Opção inválida")

    elif opcao == "2":
        produto()

    elif opcao == "3":
        opcao2 = input("""1) Listar Clientes cadastrados
2) Histórico de vendas
3) Voltar ao menu principal
""")
        if opcao2 == "1":
            clientes = Cliente.listar_clientes()
            print(f"Nome\t\tCpf\t\tidade")
            for cliente in clientes:
                print(f"{cliente['nome']}\t\t{cliente['cpf']}\t\t{cliente['idade']}")
            print("\n")
        elif opcao2 == "2":
            vendas = Venda.listar_vendas()
            if not vendas:
                print("O histórico de vendas está vazio")
            else:
                print("Vendas efetuadas:")
                for v in vendas:
                    print(f"\tData e hora: {v['data_hora']}")
                    print(f"\tValor Total: {v['total_venda']}")
                    print("\tItens da Venda:")
                    for i in v['itens_venda']:
                        print(
                            f"\t\tCodigo: {i['codigo']} \tNome: {i['nome']} \tPreço: {i['preco']} \tCategoria: {i['categoria']}")
                    print("-" * 50)
        elif opcao2 == "3":
            print("Voltando ao menu principal")
            break
    elif opcao == "4":
        print("--Cadastrando cliente--")
        cliente = {"nome": input("Digite seu nome: "), "cpf": input("Digite seu cpf: "),
                   "idade": input("Digite sua idade: ")}
        Cliente.cadastrar_cliente(cliente)

    elif opcao == "5":
        print("Saindo do sistema")
        break
