
from marshmallow import Schema, fields, ValidationError

class repsonseCreateAccountSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String()


class petOutputSchema(Schema):
    success = fields.Boolean(
        required=True, description="Show if the operation is correct"
    )
    message = fields.String(required=True, description="Message action")
    
    class Meta:
        ordered = True
        
        
class getAllPetOutputSchema(petOutputSchema):
    payload = fields.Nested(
        repsonseCreateAccountSchema(many=True), required=True, description="Payload response"
    )
    

class createPetOutputSchema(petOutputSchema):
    payload = fields.Nested(
        repsonseCreateAccountSchema(), required=True, description="Payload response"
    )