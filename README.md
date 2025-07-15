```markdown
# 🏢 Company Microservices

Microsserviços de backend simulando o ambiente técnico de uma empresa fictícia, implementados com Node.js, Python, PostgreSQL, Redis e Docker. Este projeto foi desenvolvido em uma máquina virtual Ubuntu via WSL2 no Windows 11 Pro, espelhando arquitetura real usada por empresas modernas.

---

## 🚀 Tecnologias Utilizadas

- **Node.js + Express** — Serviço de usuários (`users-service`)
- **Python + Flask** — Serviço de pedidos (`orders-service`)
- **PostgreSQL 15** — Banco de dados persistente (`db`)
- **Redis 7** — Sistema de cache (`cache`)
- **Docker & Docker Compose** — Orquestração de todos os serviços
- **WSL2 + Ubuntu** — Ambiente de desenvolvimento no Windows 11 Pro

---

## 📁 Estrutura de Diretórios

```
company-microservices/
├── users-service/         # Microsserviço Node.js de usuários
│   ├── Dockerfile
│   └── index.js
│
├── orders-service/        # Microsserviço Python de pedidos
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
│
├── docker-compose.yml     # Arquivo de orquestração dos serviços
└── README.md              # Este documento
```

---

## ⚙️ Como Executar Localmente

### Pré-requisitos:

- Docker instalado
- WSL2 habilitado (Ubuntu)
- Git inicializado no projeto

---

### 🧪 Testes Manuais (Antes do Docker)

**Users-service:**

```bash
cd users-service
npm install
node index.js
curl http://localhost:3000/users
```

**Orders-service:**

```bash
cd orders-service
pip install -r requirements.txt
python app.py
curl http://localhost:5000/orders
```

---

### 🐋 Com Docker Compose

**Subir todos os serviços:**

```bash
docker-compose up -d --build
```

**Validar execução:**

```bash
docker ps
curl http://localhost:3000/users
curl http://localhost:5000/orders
```

---

### 🗃️ Acesso ao Banco de Dados (PostgreSQL)

```bash
docker exec -it company-microservices_db_1 psql -U dev -d companydb
```

Comandos úteis:

```sql
\l       -- Lista de bancos
\dt      -- Lista de tabelas
SELECT * FROM tabela;
\q       -- Sair do PostgreSQL
```

---

## 🔐 Em breve: Autenticação JWT

Em desenvolvimento:
- Geração de tokens no `users-service`
- Validação de tokens no `orders-service`
- Proteção de endpoints privados
- Fluxo documentado no README

---

## 📘 Sobre o Ambiente

Este projeto foi desenvolvido em:

- **Windows 11 Pro**
- **WSL2 (Ubuntu 20.04 ou superior)**
- **Docker Desktop com integração WSL2**

Toda a lógica e arquivos estão salvos dentro da máquina virtual Ubuntu, mas são acessíveis pelo Windows via:

```
\\wsl.localhost\Ubuntu\home\SEU_USUARIO\company-microservices
```

Ou executando no terminal do WSL:

```bash
explorer.exe .
```

---

## 💡 Aprendizados Pessoais

> Construir esse backend me mostrou como empresas orquestram serviços com tecnologias distintas, como gerenciam cache e persistência, e como integrar serviços reais em containers. É uma base técnica sólida pra qualquer desafio em engenharia de software moderno.

---

## 📫 Contato

Você pode me encontrar no GitHub:
**[github.com/h5s4k](https://github.com/h5s4k)**

---
