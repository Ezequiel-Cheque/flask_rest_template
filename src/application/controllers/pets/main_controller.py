from flask_smorest import Blueprint
from flask.views import MethodView
from ...dto import PetQueryArgsSchema, getAllPetOutputSchema, createPetOutputSchema
from ...services.pets_service import PetService
from flask import jsonify

pets = Blueprint("pets", "pets", url_prefix="/pets", description="Pets")

class Pets(MethodView):
    
    @pets.errorhandler(404)
    def controlled_errors(e):
        return (
            jsonify(code=404, errors=e.description, message="API error", status="API"),
            404,
        )
        
    @pets.errorhandler(Exception)
    def general_exception(e):
        try:
            return (
                jsonify(
                    code=402,
                    errors=e.data["message"]["json"],
                    message="API error",
                    status="API",
                ),
                422
            )
        except:
            return (
                jsonify(code=402, errors=str(e), message="API error", status="API"),
                422,
            )
    
    
    @pets.route("/get", methods=["GET"])
    @pets.response(200, getAllPetOutputSchema, content_type="application/json")
    def get():
        """List of all pets"""
        return PetService().getAll()
    
    @pets.route("/create", methods=["POST"])
    @pets.response(201, createPetOutputSchema, content_type="application/json")
    def create(body):
        """Create a new pet"""
        return PetService().create(body)

    @pets.route("/get/<pet_id>", methods=["GET"])
    @pets.response(200, createPetOutputSchema, content_type="application/json")
    def get(pet_id: int):
        """Get pet by Id"""
        return PetService().getById(int(pet_id))