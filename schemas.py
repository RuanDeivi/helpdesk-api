from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict


class ChamadoCriar(BaseModel):
    titulo: str
    descricao: str
    prioridade: Literal["baixa", "media", "alta"] = "media"


class ChamadoAtualizar(BaseModel):
    status: Literal["aberto", "em_andamento", "fechado"] | None = None
    prioridade: Literal["baixa", "media", "alta"] | None = None


class ChamadoSaida(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    titulo: str
    descricao: str
    status: str
    prioridade: str
    criado_em: datetime