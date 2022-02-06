import connexion
from flask_cors import CORS
from server.config.logger import factory_logger
from server.config.before_request import before_request, after_request

logger = factory_logger()


def init_api():
    app = connexion.App(__name__, specification_dir="./swagger/")
    CORS(app.app)
    app.add_api("swagger.yaml", arguments={f"host_with_port": "localhost:8080"})
    app.app.before_request(before_request)
    app.app.after_request(after_request)
    return app
