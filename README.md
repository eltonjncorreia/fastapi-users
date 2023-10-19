# FastAPI Users

### Executar a aplicação

```bash
docker compose up -d
```

### Executar a criação das tabelas
```bash
docker compose run --rm app alembic upgrade head
```


##### Acesse o link para abrir a documentação da API.

Para ver a documentação no endereço: http://localhost:8000/docs


## Solicitação POST para `/users/`

### Visão Geral
Este documento descreve como fazer uma solicitação POST para o endpoint `/users/` para criar um novo usuário no sistema. O exemplo de payload fornecido será enviado no corpo da solicitação.

### Endpoint
- **URL**: `http://localhost:8000/users/`
- **Método**: POST

### Payload
```json
{
    "name": "John Doe",
    "email": "johndoe@example.com",
    "password": "hashed_password",
    "role_id": 2,
    "created_at": "2023-10-18",
    "updated_at": "2023-10-19",
    "role": {
        "description": "Moderator"
    },
    "claims": [
        {
            "description": "Claim A",
            "active": true
        }
    ]
}
```


## Desenvolvimento 

#### Instalação do pre-commit

Antes de executar os hooks, você precisa ter o gerenciador de pacotes de pre-commit instalado.

```bash
poetry add pre-commit
pre-commit install
pre-commit install --hook-type commit-msg
```

