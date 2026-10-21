from contextlib import asynccontextmanager
from typing import Literal

from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from sqlmodel import Session

from loja.banco import criar_engine, criar_tabelas
from loja.carrinho import Carrinho
from loja.promocao import Percentual
from loja.repositorio import RepositorioProdutos
from loja.servico import (DadosInvalidos, ProdutoJaExiste, ProdutoNaoEncontrado,
                          ServicoCatalogo, com_id)
class ProdutoEntrada(BaseModel):
    tipo: Literal["Produto", "Camiseta", "Calca"] = "Produto"
    nome: str
    preco: float
    tamanho: str
    manga: str | None = None
    modelagem: str | None = None


class ItemPedido(BaseModel):
    produto_id: int
    quantidade: int = Field(gt=0, le=10)