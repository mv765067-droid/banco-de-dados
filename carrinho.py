class RepositorioProdutos:
    """Única parte do sistema que sabe que existe um banco."""

    def __init__(self, sessao: Session):
        self.sessao = sessao

    def adicionar(self, produto):
        registro = para_registro(produto)
        self.sessao.add(registro)
        self.sessao.commit()
        self.sessao.refresh(registro)
        return registro.id

    def buscar(self, produto_id):
        registro = self.sessao.get(ProdutoRegistro, produto_id)
        return None if registro is None else para_dominio(registro)