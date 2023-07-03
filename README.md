# Teste IC

## Objetivo

O objetivo é mostrar os conhecimentos sobre redes tcp/ip, sistemas operacionais linux, containers, balanceadores, automação de tarefas, criação de scripts e programação.

## Estrutura de Arquivos

A estrutura de arquivos do repositório é a seguinte:

```
- appfastapi/
  - app/
    - __init__.py
    - main.py
  - Dockerfile
  - requirements.txt
- appnginx/
  - certs/
    - cert.pem
    - key.pem
  - Dockerfile
  - default.conf
- pymonitora/
  - __init__.py
  - smonitor.py
- scripts/
  - addusertossh.sh
  - firewall.sh
- cluster.sh
- docker-compose.yml
```

## Componentes Principais

### FastAPI App

O diretório `appfastapi` contém a aplicação FastAPI, responsável por fornecer uma API web.

O arquivo `appfastapi/app/main.py` contém o código principal da aplicação FastAPI.

O arquivo `appfastapi/Dockerfile` define a imagem Docker para a aplicação FastAPI.

O arquivo `appfastapi/requirements.txt` lista as dependências da aplicação FastAPI.

### NGINX Reverse Proxy

O diretório `appnginx` contém a configuração do NGINX, que atua como um reverse proxy para as duas instâncias da aplicação FastAPI.

O arquivo `appnginx/Dockerfile` define a imagem Docker para o NGINX.

O arquivo `appnginx/default.conf` contém a configuração do NGINX.

### Monitoramento

O diretório `pymonitora` contém um script Python para monitorar as instâncias da aplicação FastAPI e o NGINX.

O arquivo `pymonitora/smonitor.py` contém o código principal para o monitoramento e exportação dos dados para um arquivo `csv`.

### Scripts

O diretório `scripts` contém scripts úteis para adicionar usuários ao SSH e configurar o firewall.

### Outros Arquivos

O arquivo `cluster.sh` é um script para gerenciar a stack de aplicações no Docker.

O arquivo `docker-compose.yml` define a configuração da stack de aplicações Docker.

## Como Executar

Para executar o projeto em sua máquina basta baixar os arquivos e executar o script `cluster.sh` com a opção `start`.
