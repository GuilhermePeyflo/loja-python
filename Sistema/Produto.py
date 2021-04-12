from ast import literal_eval


class Produto:
    """
    Classe para manipular dados dos produtos cadastrados.
    Permite cadastrar, listar, alterar, pesquisar por categoria e excluir produtos.
    """

    caminho_banco = "../BancoDados/produtos.txt"

    def __init__(self):
        """
        Método para criar o arquivo de banco dos produtos caso ainda não exista.
        """
        with open(self.caminho_banco, "a") as file:
            pass

    def cadastrar_produto(self, produto: dict) -> bool:
        """
        Método para cadastrar um novo produto.
        Caso o produto não esteja cadastrado, um novo produto será registrado no arquivo e retornará True.
        Caso o produto já esteja cadastrado, retornará False.

        :param produto: dict
        :return bool
        """
        if self.verificar_produto(produto["codigo"]):
            return False
        else:
            with open(self.caminho_banco, "a") as file:
                file.write(f"{produto}\n")
            return True

    def listar_produtos(self) -> list:
        """
        Método para listar os produtos cadastrados.
        Verifica o arquivo e retorna uma lista de produtos no formato de dicionário.
        Caso ocorra erro na leitura do arquivo ou nenhum produto esteja cadastrado, retorna uma lista vazia.

        :return list
        """
        produtos = list()
        try:
            with open(self.caminho_banco, "r") as file:
                for p in list([i.strip() for i in file.readlines()]):
                    produto = literal_eval(p)
                    produtos.append(produto)
                return produtos
        except:
            pass
        finally:
            return produtos

    def pesquisar_produtos(self, nome_categoria: str) -> list:
        """
        Método para pesquisar os produtos cadastrados por categoria.
        Verifica o arquivo e retorna uma lista de produtos no formato de dicionário que possuírem a categoria pesquisada.
        Caso ocorra erro na leitura do arquivo ou nenhum produto for encontrado, retorna uma lista vazia.

        :param nome_categoria: str
        :return list
        """
        produtos = list()
        try:
            with open(self.caminho_banco, "r") as file:
                for p in list([i.strip() for i in file.readlines()]):
                    produto = literal_eval(p)
                    if produto["categoria"] == nome_categoria:
                        produtos.append(produto)
                return produtos
        except:
            pass
        finally:
            return produtos

    def alterar_produto(self, produto_alterado: dict) -> bool:
        """
        Método para alterar os dados de um produto cadastrado.
        Caso for encontrado um produto que possua o código pesquisado, este terá seus dados atualizados e reescrito no arquivo.
        Demais dados serão reescritos sem alteração e será retornado True.
        Caso nenhum produto possua o código pesquisado, retornará False.

        :param produto_alterado: dict
        :return bool
        """
        if self.verificar_produto(produto_alterado["codigo"]):
            with open(self.caminho_banco, "r+") as file:
                produtos = list()
                for p in list([i.strip() for i in file.readlines()]):
                    produto = literal_eval(p)
                    if produto_alterado["codigo"] == produto["codigo"]:
                        produto["nome"] = produto_alterado["nome"]
                        produto["preco"] = produto_alterado["preco"]
                        produto["categoria"] = produto_alterado["categoria"]
                    produtos.append(produto)
                file.seek(0)
                for p in produtos:
                    file.write(f"{p}\n")
                file.truncate()
            return True
        else:
            return False

    def excluir_produto(self, codigo_produto: str) -> bool:
        """
        Método para excluir um produto cadastrado.
        Caso for encontrado um produto que possua o código pesquisado, este será excluído do arquivo e retornará True.
        Caso nenhum produto possua o código pesquisado, retornará False.
        As vendas que possuírem o produto excluído não serão alteradas.

        :param codigo_produto: str
        :return bool
        """
        if self.verificar_produto(codigo_produto):
            with open(self.caminho_banco, "r+") as file:
                produtos = list()
                for p in list([i.strip() for i in file.readlines()]):
                    produto = literal_eval(p)
                    if codigo_produto != produto["codigo"]:
                        produtos.append(produto)
                file.seek(0)
                for p in produtos:
                    file.write(f"{p}\n")
                file.truncate()
            return True
        else:
            return False

    def verificar_produto(self, codigo_produto: str) -> bool:
        """
        Método para verificar se o código do produto já está cadastrado.
        Caso o código for encontrado no arquivo de dados, retorna True.
        Caso não for encontrado, retorna False.

        :param codigo_produto: str
        :return bool
        """
        produtos = self.listar_produtos()
        if produtos:
            for p in produtos:
                if p["codigo"] == codigo_produto:
                    return True
        else:
            return False
