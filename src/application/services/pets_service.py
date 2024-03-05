from ..models import PetModel
from ..dto import PetSchema, getAllPetOutputSchema, createPetOutputSchema
from flask_smorest import abort

class PetService:
    
    def getAll(self) -> getAllPetOutputSchema:
        response: getAllPetOutputSchema = {}
        response["success"] = True
        response["message"] = "Success to get all pets"
        response["payload"] = PetModel.getAll()
        
        return response
    
    def create(self, body: PetSchema) -> createPetOutputSchema:
        response: createPetOutputSchema = {}
        response["success"] = True
        response["message"] = "Success to create a new pet"
        response["payload"] = PetModel.create(body)
        
        return response
    
    def getById(self, id: int):
        response: createPetOutputSchema = {}
        response["success"] = True
        response["message"] = "Success to get a pet"
        
        pet = PetModel.getById(id)
        
        
        if len(pet) < 1:
            abort(404, message="Item not found")
        
        response["payload"] = pet[0]
        
        return response
        