from server.config.logger import get_logger
from flask import Response, g
import json
import connexion
import time


def before_request():
    logger = get_logger()
    g.start = time.time()
    logger.info(f'Iniciando requisicao...: {connexion.request.path}')
    autenticado = verifica_autorizacao()

    if not autenticado:
        return Response(json.dumps({
            "error": {
                "reason": "Invalid Login"
            }
        }), status=401)


def after_request(response):
    logger = get_logger()
    g.end = time.time()
    logger.info(f'Finalizando requisicao...:')
    logger.info(f'Status: {response.status_code}')
    if response.status_code == 200:
        logger.info(f'Resposta: {response.json}')
    logger.info(f'Tempo total de requisicao: {g.end - g.start}s')
    return response


def verifica_autorizacao():
    logger = get_logger()

    acessos_usuarios = {
        "usuario1": '123',
        "usuario2": 'abc'
    }

    urls_permitidas = [
        '/swagger.json',
        '/ping',
        '/ping/'
    ]

    if connexion.request.path[:3] == '/ui':
        return True

    if connexion.request.path not in urls_permitidas:
        if not connexion.request.authorization:
            logger.error("Login invalido")
            return False
        senha = connexion.request.authorization.password
        usuario = connexion.request.authorization.username

        if acessos_usuarios.get(usuario) != senha:
            return False
    return True


