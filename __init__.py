from loja.produto import Calca, Camiseta, Produto


def test_produto_vira_dicionario():
    moletom = Produto("Moletom", 159.90, "P")
    assert moletom.para_dict() == {
        "tipo": "Produto", "nome": "Moletom", "preco": 159.90, "tamanho": "P"}


def test_camiseta_acrescenta_a_manga():
    camiseta = Camiseta("Camiseta básica", 39.90, "M", "curta")
    dados = camiseta.para_dict()
    assert dados["tipo"] == "Camiseta"
    assert dados["manga"] == "curta"


def test_calca_acrescenta_a_modelagem():
    calca = Calca("Calça jeans", 129.90, "G", "reta")
    assert calca.para_dict()["modelagem"] == "reta"
    pytest
    URL_BANCO = "sqlite:///loja.db"

# trocar para o MySQL do laboratório:
# pip install pymysql cryptography
# URL_BANCO = "mysql+pymysql://usuario:senha@localhost:3306/loja"


def criar_engine(url=URL_BANCO):
    argumentos = {"check_same_thread": False} if url.startswith("sqlite") else {}
    return create_engine(url, connect_args=argumentos)

from sqlalchemy.pool import StaticPool
from sqlmodel import Field, SQLModel, create_engine

URL_BANCO = "sqlite:///loja.db"


class ProdutoRegistro(SQLModel, table=True):
    """Uma linha da tabela produto: o produto do jeito que o banco guarda."""
    __tablename__ = "produto"

    id: int | None = Field(default=None, primary_key=True)
    tipo: str
    nome: str = Field(unique=True)
    preco: float
    tamanho: str
    manga: str | None = None
    modelagem: str | None = None