# Função para criação de Log para scripts de automação python
O projeto foi desenvolvido para suprir a demanda da criação de "logs de execução" de scripts python.

Basta clonar o repositório na pasta do projeto, importar o módulo e chamar as funções.

## Técnologias utilizadas:
* [Python](https://www.python.org/)

## Configurações para rodar o projeto:

### Clonar o repositório:
git clone https://github.com/thiagomandrik/funcao_log_python

### Importar o módulo dentro do seu projeto Python:
from logs.funcaolog import *

### Para incluir registros no arquivo log:
log_msg('String a registrar no arquivo log.')
### Para salvar o arquivo no final do script, basta chamar a função abaixo:
salvar_log()

#### Versão inicial - 06/07/2022
