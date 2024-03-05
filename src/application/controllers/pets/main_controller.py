from flask_smorest import Blueprint
from flask.views import MethodView
from ...dto import PetSchema, PetQueryArgsSchema
from ...services.pets_service import PetService

pets = Blueprint("pets", "pets", url_prefix="/pets", description="")

@pets.route("/")
class Pets(MethodView):
    @pets.response(200, PetSchema(many=True))
    def get(self):
        """List of all pets"""
        return PetService().getAll()
    
    @pets.arguments(PetSchema)
    @pets.response(201, PetSchema)
    def post(self, body):
        """Create a new pet"""
        return PetService().create(body)

@pets.route("/<pet_id>")
class PetsById(MethodView):
    @pets.response(200, PetSchema)
    def get(self, pet_id: int):
        """Get pet by Id"""
        return PetService().getById(int(pet_id))