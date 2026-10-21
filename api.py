class ProdutoRegistro(SQLModel, table=True):
    id: int | None = Field(default=None,
                           primary_key=True)
    nome: str = Field(unique=True)
    preco: float
    tamanho: str
    with Session(engine) as sessao:
          sessao.add(registro)
    sessao.commit()          # grava
    sessao.refresh(registro) # pega o id gerado

    sessao.get(ProdutoRegistro, 1)
    sessao.exec(select(ProdutoRegistro)
        .where(ProdutoRegistro.preco <= 100))