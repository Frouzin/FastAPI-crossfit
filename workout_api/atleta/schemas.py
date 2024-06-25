from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated
from workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome:Annotated[str, Field(description='Nome do Atleta', example='Joao', max_length=50)]
    cpf:Annotated[str, Field(description='CPF do Atleta', example='12345678900', max_length=11)]
    idade:Annotated[int, Field(description='Idade do Atleta', example=25)]
    peso:Annotated[PositiveFloat, Field(description='Peso do Atleta', example=95.8)]
    altura:Annotated[PositiveFloat, Field(description='Altura do Atleta', example=1.78)]
    sexo:Annotated[str, Field(description='sexo do Atleta', example='M', max_length=1)]