from fastapi import APIRouter, Depends, HTTPException
from httpcore import HTTPConnection
from sqlalchemy.ext.asyncio import AsyncSession

from config import database
from model.entities.anuncio import Anuncio
from model.entities.produto import Produto
from model.entities.role import Role
from model.entities.usuario import Usuario
from config.database import db
from schemas.dto_u import DTOUsuarioCriar, DTOUsuarioResposta,DTOUsuarioRepostaLista
from service.excecoes.execoes_usuario import MatriculaCadastradaError, NomeInvalidaError, SenhaInvalidaError, \
    MatriculaInvalidaError, UsuarioNaoEncontradoError
from service.usuario_service import UsuarioService


router = APIRouter()


@router.post("/api/cadastro", response_model= DTOUsuarioResposta)
async def criar_usuario(dto_u: DTOUsuarioCriar, session: AsyncSession = Depends(db.get_db)):
 try:
   usuario = Usuario(matricula=dto_u.matricula,nome = dto_u.nome, produtos= [], anuncios= [],role=dto_u.role)

   usuario_service = UsuarioService()

   resultado = await usuario_service.cadastrar_usuario(usuario,session)

   return {
       "statuscode": 201,
       "message": "Usuário criado com sucesso",
       "body": resultado
   }

 except MatriculaCadastradaError as m:
     raise HTTPException(status_code=500, detail=m)

 except NomeInvalidaError as n:
     raise HTTPException(status_code=500, detail=n)

 except SenhaInvalidaError as s:
     raise HTTPException(status_code=500, detail=s)

 except MatriculaInvalidaError as me:
     raise HTTPException(status_code=500, detail=me)

 except HTTPConnection as ex:
     raise HTTPException(status_code=400, detail=ex)


@router.get("/api/usuarios/{usuario_matricula}",response_model=DTOUsuarioResposta)
async def buscar_usuario(usuario_matricula: str, session: AsyncSession = Depends(db.get_db)):
    try:
        usuario_service = UsuarioService()

        resultado = await usuario_service.busca_usuario(usuario_matricula,session)

        return {
            "statuscode": 200,
            "message": "Usuario buscado com sucesso",
            "body": resultado
        }
    except UsuarioNaoEncontradoError as u:
        raise HTTPException(status_code=500,detail=u)

    except HTTPConnection as ex:
        raise HTTPException(status_code=400, detail=ex)

@router.get("/api/usuarios",response_model=DTOUsuarioRepostaLista)
async def listar_usuarios(session:AsyncSession = Depends(db.get_db)):
    try:
        service = UsuarioService()

        resultado = await service.listar_usuarios(session)

        return {
            "statuscode":200,
            "message":"Usuarios listados com sucesso",
            "body": resultado
        }

    except UsuarioNaoEncontradoError as u:
        raise HTTPException(status_code=500,detail=u)

    except HTTPConnection as ex:
        raise HTTPException(status_code=400, detail=ex)

@router.patch("/api/usuarios/{usuario_matricula}", response_model= DTOUsuarioResposta)
async def atualizar_senha(usuario_matricula,session: AsyncSession = Depends(db.get_db)):
    try:
        usuario_service = UsuarioService()

        resultado = await usuario_service.alterar_senha(usuario_matricula,session)

        return {
            "statuscode": 200,
            "message": "Usuários atualizado com sucesso",
            "body": resultado
        }

    except UsuarioNaoEncontradoError as u:
        raise HTTPException(status_code=500,detail=u)

    except HTTPConnection as ex:
        raise HTTPException(status_code=400, detail=ex)

    except SenhaInvalidaError as s:
        HTTPException(status_code=500, detail=s)

@router.delete("/api/usuarios/{usuario_matricula}", response_model= DTOUsuarioResposta)
async def deletar_usuario(usuario_matricula,session: AsyncSession = Depends(db.get_db)):
    try:

        usuario_service =  UsuarioService()

        resultado = await usuario_service.deletar_usuario(usuario_matricula,session)

        return {
            "statuscode": 200,
            "message": "Usuários atualizado com sucesso",
            "body": resultado
        }

    except UsuarioNaoEncontradoError as e:
        raise HTTPException(status_code=500, detail=e)

    except HTTPConnection as ex:
        raise HTTPException(status_code=400, detail=ex)
