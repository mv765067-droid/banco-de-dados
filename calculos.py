def existe_nome(self, nome, exceto_id=None):
          consulta = select(ProdutoRegistro).where(ProdutoRegistro.nome == nome)
          registro = self.sessao.exec(consulta).first()
          return registro is not None and registro.id != exceto_id

def listar(self, tamanho=None, preco_max=None):
        consulta = select(ProdutoRegistro)
        if tamanho is not None:
            consulta = consulta.where(ProdutoRegistro.tamanho == tamanho)
        if preco_max is not None:
            consulta = consulta.where(ProdutoRegistro.preco <= preco_max)
        consulta = consulta.order_by(ProdutoRegistro.id)
        return [(r.id, para_dominio(r)) for r in self.sessao.exec(consulta)]
def test_dados_sobrevivem_ao_reinicio(tmp_path):
    url = f"sqlite:///{tmp_path / 'loja.db'}"
    engine = criar_engine(url)
    criar_tabelas(engine)
    with Session(engine) as sessao:
        RepositorioProdutos(sessao).adicionar(Produto("Moletom", 159.90, "P"))
    engine.dispose()

    outro = criar_engine(url)
    with Session(outro) as sessao:
        assert RepositorioProdutos(sessao).buscar(1).nome == "Moletom"