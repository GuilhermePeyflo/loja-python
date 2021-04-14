from Sistema import Produto, Categoria
import os


class TesteProduto:
    """
    Classe para testes da classe Produto.
    """

    def __init__(self):
        """
        Método para testar a classe Produto.
        Exclui os dados de produtos e categorias antes de realizar os testes.
        Cadastra novas categorias para realizar os testes dos produtos.
        Testa se retorna uma lista vazia quando não houver produtos salvos.
        Testa se cadastra novos produtos.
        Testa se impede o cadastro de produtos com código repetidos.
        Testa se retorna uma lista com os produtos cadastrados.
        Testa se exclui um produto existente.
        Testa se impede a exclusão de um produto inexistente.
        Testa se cadastra um novo produto após a exclusão dele.
        """
        try:
            os.remove("../BancoDados/produtos.txt")
            os.remove("../BancoDados/categorias.txt")
        except:
            pass
        finally:
            categoria = Categoria.Categoria()
            categoria.cadastrar_categoria("Bebida")
            categoria.cadastrar_categoria("Higiene")
            categoria.cadastrar_categoria("Alimento")
            produto = Produto.Produto()

            if not produto.listar_produtos():
                print("Teste Mostrar Lista Produtos vazia: Passou!")
            else:
                print("Teste Mostrar Lista Produtos vazia: Falhou!")

            if produto.cadastrar_produto({"nome": "Produto 0", "codigo": "003", "preco": "27", "categoria": "Alimento"}):
                print("Teste cadastrar novo produto: Passou!")
            else:
                print("Teste cadastrar novo produto: Falhou!")

            if produto.cadastrar_produto({"nome": "Produto 1", "codigo": "000", "preco": "27", "categoria":"Bebida"}):
                print("Teste cadastrar novo produto: Passou!")
            else:
                print("Teste cadastrar novo produto: Falhou!")

            if produto.cadastrar_produto({"nome": "Produto 2", "codigo": "001", "preco": "27", "categoria":"Higiene"}):
                print("Teste cadastrar novo produto: Passou!")
            else:
                print("Teste cadastrar novo produto: Falhou!")

            if produto.cadastrar_produto({"nome": "Produto 3", "codigo": "002", "preco": "27", "categoria":"Alimento"}):
                print("Teste cadastrar novo produto: Passou!")
            else:
                print("Teste cadastrar novo produto: Falhou!")

            if produto.cadastrar_produto({"nome": "Produto 1", "codigo": "000", "preco": "27", "categoria":"Bebida"}):
                print("Teste cadastrar produto repetido: Falhou!")
            else:
                print("Teste cadastrar produto repetido: Passou!")

            if produto.listar_produtos():
                print("Teste Mostrar Lista Produtos: Passou!")
            else:
                print("Teste Mostrar Lista Produtos: Falhou!")

            if produto.excluir_produto("001"):
                print("Teste excluir produto existente: Passou!")
            else:
                print("Teste excluir produto existente: Falhou!")

            if produto.excluir_produto("004"):
                print("Teste excluir produto inexistente: Falhou!")
            else:
                print("Teste excluir produto inexistente: Passou!")

            if produto.cadastrar_produto({"nome": "Produto 2", "codigo": "001", "preco": "27", "categoria":"Higiene"}):
                print("Teste cadastro produto após exclusão: Passou!")
            else:
                print("Teste cadastrar produto após exclusão: Falhou!")


if __name__ == "__main__":
    TesteProduto()
