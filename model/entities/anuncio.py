from sqlalchemy import String, Float, ForeignKey
from config.database import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.entities.usuario import Usuario


class Anuncio(Base):

    __tablename__ = "Anuncio"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True,nullable=False)
    negociador: Mapped["Usuario"] = relationship(back_populates="anuncios")
    preco: Mapped[float] = mapped_column(Float)
    nome: Mapped[str] = mapped_column(String)
    data_inicio: Mapped[str] = mapped_column(String)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("Usuario.id"))

