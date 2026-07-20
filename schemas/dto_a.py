from pydantic import BaseModel

class DTOAnuncioBase(BaseModel):
    nome:str
    preco: int
    data_inicio: str
    doado:bool


class DTOAnuncio(DTOAnuncioBase):
    id: int
    usuario_id: int

    class Config:
        from_attributes = True

class DTOAnuncioAdicionar(DTOAnuncioBase):
    usuario_id:int
    pass

class DTOAnuncioResposta(BaseModel):
    statuscode: int
    message: str
    body: DTOAnuncio


class DTOAnuncioRespostaLista(BaseModel):
    statuscode: int
    message: str
    body: list[DTOAnuncio]



