from ..models import PetModel
from ..dto import PetSchema
from flask_smorest import abort

class PetService:
    
    def getAll(self):
        return PetModel.getAll()
    
    def create(self, body: PetSchema):
        return PetModel.create(body)
    
    def getById(self, id: int):
        pet = PetModel.getById(id)
        print(f"RESULT: {pet}")
        
        if len(pet) < 1:
            abort(404, message="Item not found")
        
        return pet[0]
        