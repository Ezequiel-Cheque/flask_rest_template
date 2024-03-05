from os import getenv
from flask import Flask
from flask_smorest import Api
from flask_cors import CORS
import coloredlogs, logging

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
        "components": {
            "securitySchemes": {
                "Bearer Auth": {
                    "type": "apikey",
                    "in": "header",
                    "name": "Authorization",
                    "bearerFormat": "JWT",
                    "description": "Enter: **'Bearer &lt;JWT&gt;'**, where JWT is the access token"
                }
            }
        },
        "info": {
            "description": "Template to create an API Restful in python - Flask",
            "contact": {"email": "ezekiel.garcia@platimex.com.mx"},
            "license": {
                "name": "Development Platimex",
                "url": "",
            },
        },
    }
    
    SECRET_KEY = getenv("SECRET_KEY")


app = Flask(__name__)
cors = CORS(app, resources={r"*":{"origins": "*"}})
app.debug = True

## logs configuration
logging.basicConfig(format="%(asctime)s %(message)s")
coloredlogs.install(level="WARNING", logger=logging.getLogger(), isatty=True)
coloredlogs.install(level="INFO", logger=logging.getLogger(), isatty=True)

# add configuration
app.config.from_object(Config)
api = Api(app)

#register cors
CORS(pets, supports_credentials=True)

# register modules
api.register_blueprint(pets)


for path, items in api.spec._paths.items():
    for method in items.keys():
        try:
            if api.spec._paths[path][method].get("authorize", False):
                api.spec._paths[path][method]["security"] = [{"Bearer Auth": []}]
        except:
            pass