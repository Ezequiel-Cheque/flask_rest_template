petsData = [
    {
        "id": 0,
        "name": "Perro"
    },
    {
        "id": 1,
        "name": "gato"
    },
    {
        "id": 2,
        "name": "Perico"
    },
    {
        "id": 3,
        "name": "Hamster"
    }
]

class PetModel:
    
    def getAll():
        return petsData
    
    
    def create(body):
        try:
            id = len(petsData)
            petsData.append({
                **body,
                "id": id
            })
            return body
        except Exception as err:
            print(str(err))
            return False
    
    
    def getById(id: int):
        try:
            pet = filter(lambda pet: pet["id"] == id, petsData)
            pet = list(pet)
            
            return pet
        
        except Exception as err:
            print(str(err))
            return False