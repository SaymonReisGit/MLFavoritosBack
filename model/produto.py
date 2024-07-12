from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base


class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True)
    nome = Column(String(200))
    observacoes = Column(String(4000))
    marca = Column(String(200))
    url_produto = Column(String(2048))
    valor = Column(Float)
    id_mercado_livre = Column(String(200))
    quantidade = Column(Integer)
    condicao = Column(String(10))
    url_imagem = Column(String(2048))
    data_registro = Column(DateTime, default=datetime.now())

    def __init__(self, 
                    nome: str,
                    observacoes: str,
                    marca: str,
                    url_produto: str,
                    valor: float,
                    id_mercado_livre: str,
                    quantidade: int,
                    condicao: str,
                    url_imagem: str,
                    data_registro:Union[DateTime, None] = None):
        """
        Cria um Produto

        Arguments:
            nome: nome do produto,
            observacoes: informações adicionais,
            marca: marca do produto,
            url_produto: url do produto no site Mercado Livre,
            valor: valor do produto,
            id_mercado_livre: id do produto no Mercado Livre,
            quantidade: quantidade disponível a venda,
            condicao: produto novo ou usado,
            url_imagem: url da imagem do produto no site Mercado Livre,
            data_registro: data de quando o produto foi inserido à base
        """
        self.nome = nome
        self.observacoes = observacoes
        self.marca = marca
        self.url_produto = url_produto
        self.valor = valor
        self.id_mercado_livre = id_mercado_livre
        self.quantidade = quantidade
        self.condicao = condicao
        self.url_imagem = url_imagem
        if data_registro:
            self.data_registro = data_registro
