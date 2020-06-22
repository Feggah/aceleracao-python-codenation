# Desafio Data Design

   
Um modelo é a única e definitiva fonte de dados sobre os seus dados.
Ele contém os campos e métodos essenciais para manipular os dados que você está armazenando.  Em geral, cada modelo mapeia uma tabela no seu banco de dados.

Com base no desenho abaixo, modele esse relacionamento com os *models* do Django.

![](challenge.png?raw=true "Imagem")

    Obs:
    Os campos que dever ser validados:
    User.email (validação de e-mail)
    User.password (a senha não pode ser menor do que 8 caráteres)
    Agent.address (validação IPV4)
    Event.level possiveis opções (CRITICAL, DEBUG, ERROR, WARNING, INFO)
    
## Tópicos

Neste desafio você vai aprender:

- Modelagem de dados
- Modelos Django
- Validações
