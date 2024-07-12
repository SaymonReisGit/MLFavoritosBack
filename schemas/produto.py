from unicodedata import category
from pydantic import BaseModel
from typing import List


class ProdutoSchema(BaseModel):
    nome: str = "Kit 5 Camisetas Básicas Masculina Dry Fit Lisa Tradicional"
    observacoes: str = "Insira observações"
    marca: str = "Veronz"
    url_produto: str = "https://produto.mercadolivre.com.br/MLB-2918685347-kit-5-camisetas-basicas-masculina-dry-fit-lisa-tradicional-_JM"
    valor: float = 63.12
    id_mercado_livre: str = "MLB2918685347"
    quantidade: int = 500
    condicao: str = "new"
    url_imagem: str = "http://http2.mlstatic.com/D_693684-MLB54835234994_042023-I.jpg"
    data_registro: str = "04/07/2024"

class ProdutoBuscaSchema(BaseModel):
    id: str

class ProdutoUpdateSchema(BaseModel):
    id: int = 1
    observacoes: str = "Insira observações"

class ProdutoViewSchema(BaseModel):
    id: int = 1
    nome: str = "Kit 5 Camisetas Básicas Masculina Dry Fit Lisa Tradicional"
    observacoes: str = "Insira observações"
    marca: str = "Veronz"
    url_produto: str = "https://produto.mercadolivre.com.br/MLB-2918685347-kit-5-camisetas-basicas-masculina-dry-fit-lisa-tradicional-_JM"
    valor: float = 63.12
    id_mercado_livre: str = "MLB2918685347"
    quantidade: int = 500
    condicao: str = "new"
    url_imagem: str = "http://http2.mlstatic.com/D_693684-MLB54835234994_042023-I.jpg"
    data_registro: str = "04/07/2024"

class ProdutoDelSchema(BaseModel):
    id: int

def apresenta_produto(produto: ProdutoViewSchema):
    return {
        "id": produto.id,
        "nome": produto.nome,
        "observacoes": produto.observacoes,
        "marca": produto.marca,
        "url_produto": produto.url_produto,
        "valor": produto.valor,
        "id_mercado_livre": produto.id_mercado_livre,
        "quantidade": produto.quantidade,
        "condicao": produto.condicao,
        "url_imagem": produto.url_imagem,
        "data_registro": produto.data_registro
    }


class ProdutoListaViewSchema(BaseModel):
    produtos: List[ProdutoViewSchema]


def apresenta_lista_produto(produtos):
    result = []
    for produto in produtos:
        result.append(apresenta_produto(produto))
    return {"produtos": result}
