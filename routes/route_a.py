from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import db
from model.entities.anuncio import Anuncio
from schemas.dto_a import DTOAnuncio, DTOAnuncioResposta, DTOAnuncioAdicionar, DTOAnuncioRespostaLista
from schemas.dto_p import DTOProdutoAdicionar, DTOProdutoResposta, DTOProduto
from service import usuario_service
from service.anuncio_service import AnuncioService
from service.excecoes.execoes_anuncio import AnuncioCadastradoError, AnuncioInvalidoError, AnuncioNaoEncontradoError
from service.excecoes.execoes_produto import ProdutoCadastradoError, ProdutoInvalidoError, ProdutoNaoEncontradoError
from service.produto_service import ProdutoService
from model.entities.produto import Produto
from fastapi import HTTPException

router_a = APIRouter()


@router_a.post("/api/cadastro_a", response_model=DTOAnuncioResposta)
async def cadastrar_anuncio(anuncio_c: DTOAnuncioAdicionar, session: AsyncSession = Depends(db.get_db)):
    try:

        anuncio_service = AnuncioService()


        anuncio = Anuncio(
            nome=anuncio_c.nome,
            data_inicio=anuncio_c.data_inicio,
            preco=anuncio_c.preco,
            doado= anuncio_c.doado
        )

        resultado = await anuncio_service.adicionar_anuncio(usuario_id=anuncio.usuario_id,anuncio=anuncio, session=session)

        return {
            "statuscode": 200,
            "message": "Anúncio criado com sucesso",
            "body": resultado
        }

    except AnuncioCadastradoError as a:
        raise HTTPException(status_code=500, detail=a)

    except AnuncioInvalidoError as ae:
        raise HTTPException(status_code=500, detail=ae)

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router_a.delete("/api/anuncios/{anuncio_id}", response_model=  DTOAnuncioResposta)
async def deletar_anuncio(usuario_id: int,anuncio_id: int, session: AsyncSession = Depends(db.get_db)):
    try:
        anuncio_service = AnuncioService()

        resultado = await anuncio_service.deletar_anuncio(usuario_id=usuario_id,anuncio_id=anuncio_id, session=session)

        return {
            "statuscode": 200,
            "message": "Anúncio deletado com sucesso",
            "body": resultado
        }

    except AnuncioNaoEncontradoError as a:
        raise HTTPException(status_code=404, detail=a)

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router_a.put("/api/anuncios/{anuncio_id}", response_model=DTOAnuncioResposta)
async def atualizar_anuncio(usuario_id: int,anuncio_id: int, anuncio: DTOAnuncioAdicionar, session: AsyncSession = Depends(db.get_db)):
    try:
        anuncio_service = AnuncioService()

        novo_anuncio = Anuncio(
            nome=anuncio.nome,
            preco=anuncio.preco,
            doado=anuncio.doado,
            data_inicio=anuncio.data_inicio,
        )

        resultado = await anuncio_service.atualizar_anuncio(usuario_id=usuario_id,anuncio_id=anuncio_id, novo_anuncio=novo_anuncio,
                                                            session=session)

        return {
            "statuscode": 200,
            "message": "Anúncio atualizado com sucesso",
            "body": resultado
        }

    except AnuncioNaoEncontradoError as p:
        raise HTTPException(status_code=404, detail=p)

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router_a.get("/api/anuncios/{anuncio_id}", response_model=DTOAnuncioResposta)
async def buscar_anuncio(anuncio_id: int, session: AsyncSession = Depends(db.get_db)):
    try:
        anuncio_service = AnuncioService()

        resultado = anuncio_service.procurar_anuncios(anuncio_id, session)

        return {
            "statuscode": 200,
            "message": "Anúncio achado com sucesso",
            "body": resultado
        }

    except AnuncioNaoEncontradoError as p:
        raise HTTPException(status_code=404, detail=p)

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router_a.get("/api/anuncios", response_model=DTOAnuncioRespostaLista)
async def listar_produtos(produto_id: int, session: AsyncSession = Depends(db.get_db)):
    try:
        anuncio_service = AnuncioService()

        resultado = anuncio_service.listar_anuncios(session)

        return {
            "statuscode": 200,
            "message": "Anúncio listados com sucesso",
            "body": resultado
        }

    except AnuncioNaoEncontradoError as p:
        raise HTTPException(status_code=404, detail=p)

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
