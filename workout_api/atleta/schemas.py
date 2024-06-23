from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated

class Atleta(BaseModel):
    nome:Annotated[str, Field(description='Nome do Atleta', examples='Joao', max_length=50)]
    cpf:Annotated[str, Field(description='CPF do Atleta', examples='12345678900', max_length=11)]
    idade:Annotated[int, Field(description='Idade do Atleta', examples=25)]
    peso:Annotated[PositiveFloat, Field(description='Peso do Atleta', examples=95.8)]
    altura:Annotated[PositiveFloat, Field(description='Altura do Atleta', examples=1.78)]
    sexo:Annotated[str, Field(description='sexo do Atleta', examples='M', max_length=1)]