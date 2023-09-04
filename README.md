## API utilizada =>  **[viacep](https://viacep.com.br/)**
## Biblioteca python utilizada => *[Requests](https://docs.python-requests.org/en/v2.0.0/)*

## Exemplo de como acessar essa API:

~~~
import requests

# 01001000(cep de exemplo)

requisicao = requests.get("https://viacep.com.br/ws/01001000/json/")
print(requisicao)

# Terá um valor 200, significando que a requisição foi e voltou sem problemas.

print(dir(requisicao))

# Retorna todos os atributos e métodos desse objeto.

print(requisicao.json())

# Retorna os dados no formato de um dicionário.
~~~
