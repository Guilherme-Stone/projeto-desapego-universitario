from model.entities.anuncio import Anuncio
from model.entities.produto import Produto
from model.entities.role import Role
from pydantic import BaseModel

from schemas.dto_p import DTOProduto


class DTOUsuarioCriar(BaseModel):
    matricula:str
    nome:str
    role: Role
    senha:str

class DTOUsuario(BaseModel):
    matricula:str
    nome:str
    #ajeitar aqui
    produto:list[DTOProduto]
    anuncio:list[Anuncio]
    ##até aqui
    role: Role

    class Config:
        from_attributes = True

class DTOUsuarioResposta(BaseModel):
    statuscode: int
    message:str
    body: DTOUsuario

class DTOUsuarioRepostaLista(BaseModel):
    statuscode: int
    message: str
    body: list[DTOUsuario]

class DTOAlterarSenha(BaseModel):
    senha:str