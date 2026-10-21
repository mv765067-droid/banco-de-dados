class Camiseta(Produto):
   ...
   def para_dict(self):
         dados = super().para_dict()
         dados["manga"] = self.manga
         return dados


class Calca(Produto):
    ...
    def para_dict(self):
        dados = super().para_dict()
        dados["modelagem"] = self.modelagem
        return dados

    def criar_engine(url=URL_BANCO):
    # check_same_thread é um argumento só do SQLite: outros bancos não o conhecem
       argumentos = {"check_same_thread": False} if url.startswith("sqlite") else {}
       return create_engine(url, connect_args=argumentos)


def engine_em_memoria():
    """Banco que vive só na memória: ideal para testes rápidos."""
    return create_engine("sqlite://", connect_args={"check_same_thread": False},
                         poolclass=StaticPool)


def criar_tabelas(engine):
    SQLModel.metadata.create_all(engine)