from Sistema.Produto import Produto


class Categoria:
    """
    Classe para manipular dados das categorias dos produtos.
    Permite cadastrar, listar e excluir categorias.
    """

    caminho_banco = "../BancoDados/categorias.txt"

    def __init__(self):
        """
        Método para criar o arquivo de banco das categorias caso ainda não exista.
        Verifica se a categoria None já está cadastrada, caso não esteja ela é adicionada.
        """
        with open(self.caminho_banco, "a") as file:
            pass
        with open(self.caminho_banco, "r+") as file:
            if file.read() == "":
                file.write("None\n")

    def cadastrar_categoria(self, nome_categoria: str) -> bool:
        """
        Método para cadastrar uma nova categoria de produtos.
        Caso a categoria já exista, retorna False.
        Caso a categoria seja cadastrada com sucesso, retorna True.

        :param nome_categoria: str
        :return bool
        """
        if self.verificar_categoria(nome_categoria):
            return False
        else:
            with open(self.caminho_banco, "a") as file:
                file.write(f"{nome_categoria}\n")
            return True

    def listar_categorias(self) -> list:
        """
        Método para listar as categorias cadastradas.
        Retorna uma lista com as categorias cadastradas.
        Caso nenhuma categoria for encontrada ou ocorra algum erro na leitura do arquivo, retorna uma lista vazia.

        :return list
        """
        categorias = list()
        try:
            with open(self.caminho_banco, "r") as file:
                for c in list([i.strip() for i in file.readlines()]):
                    categorias.append(c)
        except:
            pass
        finally:
            return categorias

    def excluir_categoria(self, nome_categoria: str) -> bool:
        """
        Método para excluir uma categoria cadastrada.
        Caso a categoria esteja cadastrada, ela será excluída do arquivo e todos os produtos que possuírem a categoria referenciada 
        serão alterados para uma categoria nula, retornando True.
        Caso a categoria não esteja cadastrada, retorna False.
        Caso a categoria passado for None ele não é deletada e retorna False.

        :param nome_categoria: str
        :return bool
        """
        if self.verificar_categoria(nome_categoria):
            if nome_categoria == "None":
                return False
            else:
                with open(self.caminho_banco, "r+") as file:
                    categorias = list()
                    for c in list([i.strip() for i in file.readlines()]):
                        if nome_categoria != c:
                            categorias.append(c)
                    file.seek(0)
                    for c in categorias:
                        file.write(f"{c}\n")
                    file.truncate()
                classe_produto = Produto()
                produtos = classe_produto.pesquisar_produtos(nome_categoria)
                for p in produtos:
                    p["categoria"] = "None"
                    classe_produto.alterar_produto(p)
                return True
        else:
            return False

    def verificar_categoria(self, nome_categoria: str) -> bool:
        """
        Método para verificar se uma categoria já está cadastrada.
        Caso a categoria seja encontrada, retorna True.
        Caso a categoria não seja encontrada, retorna False.

        :param nome_categoria: str
        :return bool
        """
        encontrado = False
        categorias = self.listar_categorias()
        if len(categorias) > 0:
            for c in categorias:
                if nome_categoria == c:
                    encontrado = True
        return encontrado
