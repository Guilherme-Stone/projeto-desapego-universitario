from model.entities.anuncio import Anuncio
from model.entities.produto import Produto
from model.entities.role import Role
from pydantic import BaseModel



class DTOUsuarioCriar(BaseModel):
    matricula:str
    nome:str
    role: Role
    senha:str

class DTOUsuario(BaseModel):
    matricula:str
    nome:str
    #ajeitar aqui
    produto:list[Produto]
    anuncio:list[Anuncio]
    ##até aqui
    role: Role


class DTOUsuarioResposta(BaseModel):
    statuscode: int
    message:str
    body: DTOUsuario

class DTOUsuarioRepostaLista(BaseModel):
    statuscode: int
    message: str
    body: list[DTOUsuario]


