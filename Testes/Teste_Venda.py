from Sistema.Venda import Venda
from datetime import datetime
import os

try:
    os.remove("../BancoDados/vendas.txt")
except:
    print("erro")
finally:
    produto1 = {"nome": "Produto 0", "codigo": "003", "preco": "27", "categoria": "Alimento"}
    produto2 = {"nome": "Produto 1", "codigo": "000", "preco": "27", "categoria":"Bebida"}
    produto3 = {"nome": "Produto 2", "codigo": "001", "preco": "27", "categoria":"Higiene"}
    itens1 = [produto1]
    itens2 = [produto1, produto2]
    itens3 = [produto1, produto2, produto3]
    print(Venda().listar_vendas())
    venda = {"data_hora":str(datetime.today()),"itens_venda":itens1,"total_venda":"27"}
    Venda().cadastrar_venda(venda)
    print(Venda().listar_vendas())
    venda = {"data_hora":str(datetime.today()),"itens_venda":itens2,"total_venda":"54"}
    Venda().cadastrar_venda(venda)
    print(Venda().listar_vendas())
    venda = {"data_hora":str(datetime.today()),"itens_venda":itens3,"total_venda":"81"}
    Venda().cadastrar_venda(venda)
    print(Venda().listar_vendas())