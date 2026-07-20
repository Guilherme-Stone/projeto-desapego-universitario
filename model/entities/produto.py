from sqlalchemy import String, Integer, Boolean, ForeignKey
from config.database import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from typing import TYPE_CHECKING
from model.entities.anuncio import Anuncio

if TYPE_CHECKING:
    from model.entities.usuario import Usuario

class Produto(Base):
    __tablename__ = "Produto"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True,nullable=False)
    negociador: Mapped["Usuario"] = relationship(back_populates="produtos")
    quantidade: Mapped[int] = mapped_column(Integer)
    nome: Mapped[str] = mapped_column(String)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("Usuario.id"))
    anuncio_id: Mapped[int] = mapped_column(ForeignKey("Anuncio.id"))
    anuncios: Mapped["Anuncio"] = relationship(back_populates="produtos")