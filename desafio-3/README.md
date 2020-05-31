# Desafio de programação orientada a testes

Dark sky é um serviço de previsão do tempo por API. Temos uma função que faz uma requisição para a api
do Dark sky passando a latitude e a longitude de algum lugar no planeta e a api retorna a temperatura. Nossa função
converte para celsius e retorna o valor da temperatura.


Escreva um teste que seja possível testar off-line a chamada para api do Dark sky e a conversão para celsius.
Use a bibliteca Pytest e os seguntes dados para testar a função **get_temperature**.

    lat = -14.235004
    lng = -51.92528
    temperature = 62
    expected = 16

A função a ser testada esta no arquivo **main.py** e a implementação do teste deve ser feita no arquivo **test_main.py**. O objetivo deste desafio é que você pratique a criação de testes unitários, por isso crie os testes pensando nos cenários possíveis de erro e acerto, de modo que seus testes possam cobrir o maior número de casos. Após a criação dos testes, use a funcionalidade de Code Review para validar sua implementação com a [comunidade](https://comunidade.codenation.dev).

## Tópicos

Neste desafio você vai aprender:

- Testes unitários
- Mock
- Pytest
- Monkeypatch
