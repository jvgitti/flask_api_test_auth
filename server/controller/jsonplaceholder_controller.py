from server.service.jsonplaceholder_service import get_by_n_registros


def get_ultimos_cinco():
    return get_by_n_registros(5)
