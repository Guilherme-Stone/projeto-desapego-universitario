from sqlalchemy import String, Boolean
from config.database import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from model.entities.role import Role
from sqlalchemy import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.entities.produto import Produto
    from model.entities.anuncio import Anuncio

class Usuario(Base):
    __tablename__ = "Usuario"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True,nullable=False)
    matricula: Mapped[str] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String)
    produtos: Mapped[list["Produto"]] = relationship(back_populates="negociador",cascade="all, delete-orphan")
    anuncios: Mapped[list["Anuncio"]] = relationship(back_populates="negociador",cascade="all, delete-orphan")
    role: Mapped[Role] = mapped_column(Enum(Role),default=Role.ESTUDANTE)
    senha: Mapped[str] = mapped_column(String)



