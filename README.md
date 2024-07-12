# MLFavoritos API

MLFavoritos API é uma aplicação Flask para gerenciar produtos favoritos do Mercado Livre. A API permite adicionar, atualizar, visualizar e remover produtos da base de dados.

## Tecnologias Utilizadas

- Python
- Flask
- SQLAlchemy
- Flask-OpenAPI3

## Endpoints

### Adicionar Produto

- **URL:** `/produto`
- **Método:** `POST`
- **Tags:** `Produto`
- **Request Body:**
    ```json
    {
        "nome": "string",
        "observacoes": "string",
        "marca": "string",
        "url_produto": "string",
        "valor": "number",
        "id_mercado_livre": "string",
        "quantidade": "integer",
        "condicao": "string",
        "url_imagem": "string"
    }
    ```
- **Responses:**
    - `200`: Produto adicionado com sucesso.
    - `400`: Erro ao adicionar o produto.
    - `409`: Produto já existente.

### Atualizar Produto

- **URL:** `/produto`
- **Método:** `PUT`
- **Tags:** `Produto`
- **Request Body:**
    ```json
    {
        "id": "integer",
        "observacoes": "string"
    }
    ```
- **Responses:**
    - `200`: Produto atualizado com sucesso.
    - `400`: Erro ao atualizar o produto.

### Buscar Produto por ID Mercado Livre

- **URL:** `/produto/<id>`
- **Método:** `GET`
- **Tags:** `Produto`
- **Responses:**
    - `200`: Produto encontrado.
    - `404`: Produto não encontrado.

### Listar Todos os Produtos

- **URL:** `/produtos`
- **Método:** `GET`
- **Tags:** `Produto`
- **Responses:**
    - `200`: Lista de produtos.
    - `404`: Nenhum produto encontrado.

### Deletar Produto por ID

- **URL:** `/produto/<int:id>`
- **Método:** `DELETE`
- **Tags:** `Produto`
- **Responses:**
    - `200`: Produto deletado com sucesso.
    - `404`: Produto não encontrado.

### Como executar 

**Executar:**
    - Criar Imagem Docker: docker build -t mlfav-back-docker .
    - Executar Docker: docker run -p 5000:5000 mlfav-back-docker

---

## Autor

Este sistema foi desenvolvido por Saymon Carvalho dos Reis, apresentado como MVP para o curso de Pós-Graduação em Engenharia de Software - PUC Rio.