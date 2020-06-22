# Desafio REST API

REST significa Representational State Transfer. Em português, 
Transferência de Estado Representacional. Trata-se de uma abstração da 
arquitetura da Web. Resumidamente, o REST consiste em princípios/regras/constraints
 que, quando seguidas, permitem a criação de um projeto com interfaces bem definidas. 
 Desta forma, permitindo, por exemplo, que aplicações se comuniquem.

Utilizando os conceitos apresentados nos conteúdo de apoio propostos, utilizando se de boas praticas no desenvolvimento de software,
 implemente uma aplicação utilizando Django e Django REST Framework.

Essa aplicação é uma API que funcionará como um serviço lambda, implemente views baseadas em funções, que retornarão o resultado das funções em um formato json.

Função 1) A função a ser implementada em um endpoint recebe um request com POST com um json, que contem uma lista de numeros, a função deve 
deve retornar uma lista com os numeros ordenados pela quantidade de vezes que eles aparecem na lista.

    Exemplo:
    POST data = {"question": [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12, 5]}
    Response = {"solution":[3 ,3, 3, 3, 2, 2, 2, 5, 5, 12, 12, 4]}
    Função =   solution([2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12, 5]) == [3, 3, 3, 3, 2, 2, 2, 5, 5, 12, 12, 4]]



## Tópicos

Neste desafio você vai aprender:

- Django Rest Framework
  - Serialization
  - Requests and responses
  - Function based views
  - Viewsets and routers
