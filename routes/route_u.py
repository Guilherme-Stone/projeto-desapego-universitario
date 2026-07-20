from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from model.entities.usuario import Usuario
from config.database import db
from schemas.dto_u import DTOUsuarioCriar, DTOUsuarioResposta, DTOUsuarioRepostaLista, DTOAlterarSenha
from service.excecoes.execoes_usuario import MatriculaCadastradaError, NomeInvalidaError, SenhaInvalidaError, \
    MatriculaInvalidaError, UsuarioNaoEncontradoError
from service.usuario_service import UsuarioService


router_u = APIRouter()


@router_u.post("/api/cadastro_u", response_model= DTOUsuarioResposta)
async def criar_usuario(dto_u: DTOUsuarioCriar, session: AsyncSession = Depends(db.get_db)):
 try:
   usuario = Usuario(matricula=dto_u.matricula,senha=dto_u.senha,nome = dto_u.nome,role=dto_u.role)

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

 except HTTPException as ex:
     raise HTTPException(status_code=400, detail=ex)


@router_u.get("/api/usuarios/{usuario_matricula}",response_model=DTOUsuarioResposta)
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
        raise HTTPException(status_code=404,detail=u)

    except HTTPException as ex:
        raise HTTPException(status_code=400, detail=ex)

@router_u.get("/api/usuarios",response_model=DTOUsuarioRepostaLista)
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
        raise HTTPException(status_code=404,detail=u)

    except HTTPException as ex:
        raise HTTPException(status_code=400, detail=ex)

@router_u.patch("/api/usuarios/{usuario_matricula}", response_model= DTOUsuarioResposta)
async def atualizar_senha(usuario_matricula,dto_senha:DTOAlterarSenha,session: AsyncSession = Depends(db.get_db)):
    try:
        usuario_service = UsuarioService()

        resultado = await usuario_service.alterar_senha(usuario_matricula,dto_senha.senha,session)

        return {
            "statuscode": 200,
            "message": "Usuários atualizado com sucesso",
            "body": resultado
        }

    except UsuarioNaoEncontradoError as u:
        raise HTTPException(status_code=404,detail=u)

    except HTTPException as ex:
        raise HTTPException(status_code=400, detail=ex)

    except SenhaInvalidaError as s:
        HTTPException(status_code=500, detail=s)

@router_u.delete("/api/usuarios/{usuario_matricula}", response_model= DTOUsuarioResposta)
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
        raise HTTPException(status_code=404, detail=e)

    except HTTPException as ex:
        raise HTTPException(status_code=400, detail=ex)
