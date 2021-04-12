import Categoria, Produto
import os

try:
    os.remove("../BancoDados/categorias.txt")
    with open("../BancoDados/categorias.txt", "a") as file:
        pass
    os.remove("../BancoDados/produtos.txt")
    with open("../BancoDados/produtos.txt", "a") as file:
        pass
except:
    print("Erro")
finally:
    print(Categoria.listar_categorias())
    print(Categoria.cadastrar_categoria("Bebida"))
    print(Categoria.cadastrar_categoria("Higiene"))
    print(Categoria.cadastrar_categoria("Alimento"))
    print(Categoria.cadastrar_categoria("Bebida"))
    print(Categoria.listar_categorias())
    Produto.cadastrar_produto({"nome": "Produto 0", "codigo": "003", "preco": "27", "categoria": "Alimento"})
    Produto.cadastrar_produto({"nome": "Produto 1", "codigo": "000", "preco": "27", "categoria": "Bebida"})
    Produto.cadastrar_produto({"nome": "Produto 2", "codigo": "001", "preco": "27", "categoria": "Higiene"})
    Produto.cadastrar_produto({"nome": "Produto 3", "codigo": "002", "preco": "27", "categoria": "Alimento"})
    print(Categoria.excluir_categoria("Alimento"))
    print(Categoria.excluir_categoria("Construção"))
    print(Categoria.listar_categorias())
    print(Categoria.cadastrar_categoria("Alimento"))
    print(Categoria.listar_categorias())