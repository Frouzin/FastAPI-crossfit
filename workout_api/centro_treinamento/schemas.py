from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome:Annotated[str, Field(description='Nome da centro', example='CT King', max_length=20)]
    endereco:Annotated[str, Field(description='Endereço do centro', example='Rua xx, 02', max_length=60)]
    proprietario:Annotated[str, Field(description='Proprietario do centro', example='Marcos', max_length=30)]