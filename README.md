# Painel de Segurança de Código

API de cadastro de usuários (Flask) usada como app de demonstração para um
pipeline de CI/CD que escaneia vulnerabilidades automaticamente a cada commit.

> Este app contém vulnerabilidades **propositais** (SQL Injection, segredo
> fixo no código, modo debug ativo), inseridas de propósito para servir de
> alvo de teste para o scanner de segurança (Bandit) no pipeline.

## Status do projeto

- [x] Etapa 1 — App base
- [ ] Etapa 2 — Dockerizar
- [ ] Etapa 3 — Pipeline CI/CD com SAST
- [ ] Etapa 4 — Histórico de scans
- [ ] Etapa 5 — Dashboard visual
- [ ] Etapa 6 — Documentação final
- [ ] Etapa 7 — Publicação

## Rodando localmente

```bash
pip install -r requirements.txt
python app.py
```

A API sobe em `http://localhost:5000`.

### Endpoints

- `GET /` — status da API
- `POST /usuarios` — cadastra um usuário (`nome`, `email`, `senha`)
- `GET /usuarios/<id>` — busca um usuário pelo id
