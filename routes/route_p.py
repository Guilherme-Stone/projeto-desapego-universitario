from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import db
from schemas.dto_p import DTOProdutoAdicionar, DTOProdutoResposta, DTOProduto
from service.excecoes.execoes_produto import ProdutoCadastradoError, ProdutoInvalidoError, ProdutoNaoEncontradoError
from service.produto_service import ProdutoService
from model.entities.produto import Produto
from fastapi import HTTPException

router_p = APIRouter()

@router_p.post("/api/cadastro_p", response_model=DTOProdutoResposta)
async def cadastrar_produto(produto_c: DTOProdutoAdicionar,session: AsyncSession = Depends(db.get_db)):
    try:

        produto_service = ProdutoService()

        produto = Produto(
            nome= produto_c.nome,
            doado=produto_c.doado,
            quantidade=produto_c.quantidade
        )

        resultado = await produto_service.adicionar_produto(produto.usuario_id,produto,session)

        return {
            "statuscode":200,
            "message":"Produto adicionado com sucesso",
            "body": resultado
        }

    except ProdutoCadastradoError as p:
        raise HTTPException(status_code=500, detail=p)

    except ProdutoInvalidoError as pe:
        raise HTTPException(status_code=500, detail=pe)

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code,detail=e.detail)


@router_p.delete("/api/produtos/{produto_id}", response_model=DTOProdutoResposta)
async def deletar_produto(usuario_id: int,produto_id: int, session: AsyncSession = Depends(db.get_db)):
    try:
        produto_service = ProdutoService()

        resultado = await produto_service.deletar_produto(usuario_id=usuario_id,produto_id=produto_id,session=session)

        return {
            "statuscode": 200,
            "message": "Produto deletado com sucesso",
            "body": resultado
        }

    except ProdutoNaoEncontradoError as p:
        raise HTTPException(status_code=404, detail=p)

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code,detail=e.detail)


@router_p.put("/api/produtos/{produto_id}", response_model=DTOProdutoResposta)
async def atualizar_produto(usuario_id,produto_id:int,produto: DTOProdutoAdicionar, session: AsyncSession = Depends(db.get_db)):
    try:
        produto_Service = ProdutoService()

        novo_produto = Produto(
            nome= produto.nome,
            quantidade= produto.quantidade,
        )

        resultado = await produto_Service.atualizar_produto(usuario_id=usuario_id,produto_id=produto_id,novo_produto=novo_produto,session=session)

        return {
            "statuscode": 200,
            "message": "Produto atualizado com sucesso",
            "body": resultado
        }

    except ProdutoNaoEncontradoError as p:
        raise HTTPException(status_code=404, detail=p)

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code,detail=e.detail)


@router_p.get("/api/produtos/{produto_id}", response_model=DTOProdutoResposta)
async def buscar_produto(produto_id: int, session: AsyncSession = Depends(db.get_db)):
    try:
        produto_service = ProdutoService()

        resultado = produto_service.procurar_produto(produto_id,session)

        return {
            "statuscode": 200,
            "message": "Produto achado com sucesso",
            "body": resultado
        }

    except ProdutoNaoEncontradoError as p:
        raise HTTPException(status_code=404, detail=p)

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code,detail=e.detail)


@router_p.get("/api/produtos", response_model=DTOProdutoResposta)
async def listar_produtos(produto_id: int, session: AsyncSession = Depends(db.get_db)):
    try:
        produto_service = ProdutoService()

        resultado = produto_service.listar_produtos(session)

        return {
            "statuscode": 200,
            "message": "Produtos listados com sucesso",
            "body": resultado
        }

    except ProdutoNaoEncontradoError as p:
        raise HTTPException(status_code=404, detail=p)

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
