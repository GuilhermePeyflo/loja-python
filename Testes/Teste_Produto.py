# from Sistema.Produto import Produto
# from Sistema.Categoria import Categoria
from Sistema import Produto, Categoria
import os

try:
    os.remove("../BancoDados/produtos.txt")
    os.remove("../BancoDados/categorias.txt")
except:
    print("erro")
finally:
    c = Categoria.Categoria()
    p = Produto.Produto()
    c.cadastrar_categoria("Bebida")
    c.cadastrar_categoria("Higiene")
    c.cadastrar_categoria("Alimento")
    print(p.listar_produtos())
    print(p.cadastrar_produto({"nome": "Produto 0", "codigo": "003", "preco": "27", "categoria": "Alimento"}))
    print(p.cadastrar_produto({"nome": "Produto 1", "codigo": "000", "preco": "27", "categoria":"Bebida"}))
    print(p.cadastrar_produto({"nome": "Produto 2", "codigo": "001", "preco": "27", "categoria":"Higiene"}))
    print(p.cadastrar_produto({"nome": "Produto 3", "codigo": "002", "preco": "27", "categoria":"Alimento"}))
    print(p.cadastrar_produto({"nome": "Produto 1", "codigo": "000", "preco": "27", "categoria":"None"}))
    print(p.listar_produtos())
    print(p.excluir_produto("001"))
    print(p.excluir_produto("004"))
    print(p.listar_produtos())
    print(p.cadastrar_produto({"nome": "Produto 2", "codigo": "001", "preco": "27", "categoria":"Higiene"}))
    print(p.listar_produtos())