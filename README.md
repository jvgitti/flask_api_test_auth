Para subir o projeto, execute os comando abaixo:
-> run pip install -r requirements.txt
-> python -m server

A Api estará dispoível em http://localhost:8080/
Documentação das rotas: http://localhost:8080/ui

Basic Authentication necessária para as rotas diferentes de /ui e /ping

Logins cadastrados:
usuario: usuario1
senha: 123

usuario: usuario2
senha abc

Endpoint para a consulta dos 5 ultimos registros: http://localhost:8080/jsonplaceholder

Para rodas os testes, execute os comandos:
-> pip install -r test-requirements.txt
-> coverage run -m unittest server/test/jsonplaceholder_test.py
-> coverage report
