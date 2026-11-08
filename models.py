from datetime import datetime
from sqlalchemy import String, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Chamado(Base):
    __tablename__ = "chamados"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    descricao: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(20), default="aberto")
    prioridade: Mapped[str] = mapped_column(String(20), default="media")
    criado_em: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)