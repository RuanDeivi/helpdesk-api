# Help Desk API

API de sistema de chamados (help desk) feita com Python, FastAPI e SQLite.

## Como rodar

1. Crie e ative o ambiente virtual:

```
python -m venv venv
venv\Scripts\activate
```

2. Instale as dependências:

```
pip install -r requirements.txt
```

3. Inicie o servidor:

```
uvicorn main:app --reload
```

4. Abra http://127.0.0.1:8000/docs

## Rotas

- `POST /chamados`: abre um chamado
- `GET /chamados`: lista os chamados
- `GET /chamados/{id}`: busca um chamado
- `PATCH /chamados/{id}`: atualiza status ou prioridade

## Próximos passos

- Autenticação com JWT e senhas com bcrypt
- Testes automatizados com pytest
- Docker
- Testes de segurança