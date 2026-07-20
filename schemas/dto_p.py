from pydantic import BaseModel

class DTOProdutoBase(BaseModel):
    nome:str
    quantidade: int

class DTOProduto(DTOProdutoBase):
    id: int
    usuario_id: int

    class Config:
        from_attributes = True

class DTOProdutoAdicionar(DTOProdutoBase):
   pass


class DTOProdutoResposta(BaseModel):
    statuscode: int
    message: str
    body: DTOProduto


class DTOProdutoRespostaLista(BaseModel):
    statuscode: int
    message: str
    body: list[DTOProduto]
