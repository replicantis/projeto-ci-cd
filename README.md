# Conversor de Temperatura com CI/CD

Projeto acadêmico desenvolvido para praticar:

- Git e GitHub
- Branches e Pull Requests
- GitHub Actions
- Continuous Integration (CI)
- Continuous Delivery/Deployment (CD)
- Docker

## Funcionalidade

A aplicação converte uma temperatura de Celsius para Fahrenheit.

## Como executar localmente

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python app.py
```

Depois, abra no navegador:

```text
http://localhost:5000
```

## Como executar com Docker

Crie a imagem:

```bash
docker build -t conversor-temperatura .
```

Execute o container:

```bash
docker run -d -p 5000:5000 --name conversor-temperatura conversor-temperatura
```

Acesse:

```text
http://localhost:5000
```

## Alertas

O GitHub Actions envia notificações automáticas ao Discord quando há commits ou alterações em Pull Requests.

## Testes unitários

Os testes automatizados são executados pelo GitHub Actions sempre que uma Pull Request é criada ou atualizada com um novo commit.