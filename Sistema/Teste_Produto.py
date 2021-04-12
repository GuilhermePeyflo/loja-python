import Produto, Categoria
import os

try:
    os.remove("../BancoDados/produtos.txt")
    with open("../BancoDados/produtos.txt", "a") as file:
        pass
    os.remove("../BancoDados/categorias.txt")
    with open("../BancoDados/categorias.txt", "a") as file:
        pass
except:
    print("erro")
finally:
    Categoria.cadastrar_categoria("Bebida")
    Categoria.cadastrar_categoria("Higiene")
    Categoria.cadastrar_categoria("Alimento")
    print(Produto.listar_produtos())
    print(Produto.cadastrar_produto({"nome": "Produto 0", "codigo": "003", "preco": "27", "categoria": "Alimento"}))
    print(Produto.cadastrar_produto({"nome": "Produto 1", "codigo": "000", "preco": "27", "categoria":"Bebida"}))
    print(Produto.cadastrar_produto({"nome": "Produto 2", "codigo": "001", "preco": "27", "categoria":"Higiene"}))
    print(Produto.cadastrar_produto({"nome": "Produto 3", "codigo": "002", "preco": "27", "categoria":"Alimento"}))
    print(Produto.cadastrar_produto({"nome": "Produto 1", "codigo": "000", "preco": "27", "categoria":"None"}))
    print(Produto.listar_produtos())
    print(Produto.excluir_produto("001"))
    print(Produto.excluir_produto("004"))
    print(Produto.listar_produtos())
    print(Produto.cadastrar_produto({"nome": "Produto 2", "codigo": "001", "preco": "27", "categoria":"Higiene"}))
    print(Produto.listar_produtos())