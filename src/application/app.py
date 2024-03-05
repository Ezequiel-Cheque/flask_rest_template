from flask import Flask
from flask_smorest import Api

from .controllers import pets

class Config:
    ENV = "TEST"
    TESTING = False
    JSON_SORT_KEYS = False
    API_VERSION = 0.1
    API_TITLE = "My API"
    OPENAPI_VERSION = "3.0.2"
    OPENAPI_URL_PREFIX = "/api"
    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_URL = (
        "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    )
    OPENAPI_SWAGGER_UI_PATH = "/"
    OPENAPI_SWAGGER_UI_URL = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/"
    API_SPEC_OPTIONS = {
        "info": {
            "description": "Template to create an API Restful in python - Flask",
            "contact": {"email": "ezekiel.garcia@platimex.com.mx"},
            "license": {
                "name": "Development Platimex",
                "url": "",
            },
        },
    }

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)


api.register_blueprint(pets)