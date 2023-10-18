# FastAPI Users

# Para executar a aplicação

```bash
docker compose up -d
```

##### Acesse o link para abrir a documentação da API.

http://localhost:8000/docs


## Pre-commit 

#### Instalação

Antes de executar os hooks, você precisa ter o gerenciador de pacotes de pre-commit instalado.

```bash
poetry add pre-commit
pre-commit install
pre-commit install --hook-type commit-msg
```

