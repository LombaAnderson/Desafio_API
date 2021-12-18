# Desafio_API
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/LombaAnderson/Desafio_API/blob/main/LICENSE)

# Executando a Solução:
- git clone
- É preciso criar o arquivo .env com base no .env_example 

# Linguagem desenvolvida
-Python

- Desenvolver o projeto com os valores:
```
API_EXTRACT=http://challenge.dienekes.com.br/api
```
- docker-compose up --build
- http://127.0.0.1:8000/docs/ -> Documentação e Testes da API
- http://127.0.0.1:8000/numbers/ -> Get para retornar os números ordenados

# Desafio:

é preciso criar uma aplicação que desenvolva um processo de ETL (Extract, Transform and Load). O modus operandi deste projeto está descrito logo abaixo.

## 1. Extract
Realizar chamadas na API REST para extrair um conjunto de números da base de dados.
Exemplo:
GET http://challenge.dienekes.com.br/api/numbers?page=1 Retorno:
{ "numbers":[ 0.4971795774527892, 0.7311238428477732, 0.004048275097350857] }
Note que a API recebe o parâmetro "page" na url. É possível extrair os números de todas as páginas disponíveis da base de dados. É possível saber que se conseguiu extrair todos os números disponíveis quando for solicitada a página e o servidor retornar um array vazio.
Exemplo de retorno quando não existir mais números a serem extraídos:
{ "numbers":[] }


## 2. Transform
A etapa de transformação consiste em ordenar todos os números extraídos na etapa anterior.
IMPORTANTE: a ordenação deve ser feita com o conjunto final contendo todos os números extraídos de todas as páginas.
IMPORTANTE 2: se deve implementar o algoritmo de ordenação. Não é permitido utilizar nenhum recurso da linguagem que faça toda a ordenação.


# 3. Load
A aplicação deve expor uma API que disponibiliza o conjunto final de números ordenados da etapa de transform. 

# Autor:
Anderson Lomba de Oliveira

Linkedin

https://www.linkedin.com/in/anderson-lomba-140279142/

Portfólio

https://www.lombanderson.epizy.com

# Agradecimentos

Agradeço sobretudo a Deus e a minha esposa, minha companheira que torce muito por mim sempre!
