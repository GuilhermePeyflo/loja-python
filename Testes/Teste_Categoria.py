from Sistema.Categoria import Categoria
from Sistema.Produto import Produto
import os


class TesteCategoria:
    """
    Classe de testes da classe Categoria.
    """

    def __init__(self):
        """
        Método para testar a classe Categoria.
        Exclui os dados de categorias e de produtos antes de realizar os testes.
        Testa se retorna uma lista vazia quando não houver dados salvos.
        Testa se cadastra novas categorias.
        Testa se impede o cadastro de uma categoria repetida.
        Testa se retorna uma lista com as categorias cadastradas.
        Testa se exclui uma categoria existente.
        Testa se impede a exclusão de uma categoria inexistente.
        Testa se cadastra uma nova categoria após a exclusão dela.
        Testa se ocorre a alteração de produtos salvos quando a categoria é excluída.
        """
        try:
            os.remove("../BancoDados/categorias.txt")
            os.remove("../BancoDados/produtos.txt")

        except:
            pass
        finally:
            categoria = Categoria()
            if not categoria.listar_categorias():
                print("Teste Mostrar Lista Categorias vazia: Falhou!")
            else:
                print("Teste Mostrar Lista Categorias vazia: Passou!")

            if categoria.cadastrar_categoria("Bebida"):
                print("Teste cadastrar nova categoria: Passou!")
            else:
                print("Teste cadastrar nova categoria: Falhou!")

            if categoria.cadastrar_categoria("Higiene"):
                print("Teste cadastrar nova categoria: Passou!")
            else:
                print("Teste cadastrar nova categoria: Falhou!")

            if categoria.cadastrar_categoria("Alimento"):
                print("Teste cadastrar nova categoria: Passou!")
            else:
                print("Teste cadastrar nova categoria: Falhou!")

            if categoria.cadastrar_categoria("Bebida"):
                print("Teste cadastrar categoria repetida: Falhou!")
            else:
                print("Teste cadastrar categoria repetida: Passou!")

            if categoria.listar_categorias():
                print("Teste Mostrar Lista Categorias: Passou!")
            else:
                print("Teste Mostrar Lista Categorias: Falhou!")

            Produto().cadastrar_produto({"nome": "Produto 0", "codigo": "003", "preco": "27", "categoria": "Alimento"})
            Produto().cadastrar_produto({"nome": "Produto 1", "codigo": "000", "preco": "27", "categoria": "Bebida"})
            Produto().cadastrar_produto({"nome": "Produto 2", "codigo": "001", "preco": "27", "categoria": "Higiene"})
            Produto().cadastrar_produto({"nome": "Produto 3", "codigo": "002", "preco": "27", "categoria": "Alimento"})

            if categoria.excluir_categoria("Alimento"):
                print("Teste Excluir categoria existente: Passou!")
            else:
                print("Teste Excluir categoria existente: Falhou!")

            if categoria.excluir_categoria("Construção"):
                print("Teste Excluir categoria inexistente: Falhou!")
            else:
                print("Teste Excluir categoria inexistente: Passou!")

            if categoria.cadastrar_categoria("Alimento"):
                print("Teste cadastrar nova categoria após excluir: Passou!")
            else:
                print("Teste cadastrar nova categoria após excluir: Falhou!")

            ok = 0
            for p in Produto().listar_produtos():
                if p["nome"] == "Produto 0" and p["categoria"] == "None":
                    ok += 1
                elif p["nome"] == "Produto 3" and p["categoria"] == "None":
                    ok += 1
            if ok == 2:
                print("Teste de alteração da categoria dos produtos após exclusão de categoria: Passou!")
            else:
                print("Teste de alteração da categoria dos produtos após exclusão de categoria: Falhou!")


if __name__ == "__main__":
    TesteCategoria()
