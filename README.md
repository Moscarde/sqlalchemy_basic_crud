# SQLAlchemy Basic CRUD

Este repositório contém um exemplo básico de operações CRUD (Create, Read, Update, Delete) utilizando SQLAlchemy com diferentes bancos de dados: PostgreSQL, SQLite e MySQL.

## Descrição

O código define duas classes principais, `Livro` e `Usuario`, que representam tabelas no banco de dados. Além disso, são implementadas funções de CRUD para gerenciar as operações de adição, listagem, atualização e remoção de registros dessas tabelas. A aplicação foi projetada para funcionar com bancos de dados como PostgreSQL, SQLite e MySQL, oferecendo flexibilidade na escolha da plataforma de dados.

### Classes

- **Livro**: Representa uma tabela de livros com os seguintes campos:
  - `id`: Inteiro, chave primária.
  - `titulo`: String, obrigatório.
  - `autor`: String, obrigatório.
  - `preco`: Float, obrigatório.

- **Usuario**: Representa uma tabela de usuários com os seguintes campos:
  - `id`: Inteiro, chave primária.
  - `nome`: String, obrigatório.
  - `email`: String, obrigatório e único.

### Operações CRUD

O código implementa as seguintes operações para as tabelas `livros` e `usuarios`:

- **Adicionar registro**: Adiciona um novo livro ou usuário no banco de dados.
- **Listar registros**: Retorna uma lista de todos os livros ou usuários armazenados.
- **Atualizar registro**: Atualiza informações de um livro ou usuário existente.
- **Deletar registro**: Remove um livro ou usuário do banco de dados.

## Configuração do Banco de Dados

O código é configurado para trabalhar com diferentes bancos de dados. Por padrão, ele se conecta a um banco de dados PostgreSQL, mas pode ser ajustado para usar SQLite ou MySQL modificando a variável `DATABASE_URL`.

### Exemplo de Configuração

#### PostgreSQL

```python
DATABASE_URL = "postgresql://postgres:1234@localhost/biblioteca"
```

#### SQLite

```python
DATABASE_URL = "sqlite:///biblioteca.db"
```

#### MySQL

```python
DATABASE_URL = "mysql+pymysql://root:1234@localhost/biblioteca"
```
Para utilizar um banco de dados diferente, basta descomentar a linha correspondente à sua escolha e garantir que o banco esteja corretamente configurado.
Mais informações na documentação oficial: 
[https://docs.sqlalchemy.org/en/20/core/engines.html#backend-specific-urls](https://docs.sqlalchemy.org/en/20/core/engines.html#backend-specific-urls)

### Como Usar

1. Clone o repositório:
```
git clone https://github.com/Moscarde/sqlalchemy_basic_crud
cd SQLAlchemy-basic-crud
```

2. Instale as dependências:
```
pip install sqlalchemy
```
_Pode ser necessário instalar o pacotes como psycopg2, pymysql ou mysqlclient (dependendo da sua escolha de banco)_

3. **Execute o script:** Execute o script para criar as tabelas e realizar operações CRUD:

```
python basic_crud.py
```

4. O script realizará as seguintes operações:

- Adicionará um livro e um usuário de exemplo.
- Listará todos os livros e usuários.
- Atualizará o preço de um livro.
- Excluirá um usuário.