from fastapi_cloud_cli.commands.apps import list_apps
from sqlalchemy.ext.asyncio import AsyncSession
from service.excecoes.execoes_usuario import MatriculaCadastradaError, MatriculaInvalidaError, SenhaInvalidaError, NomeInvalidaError, UsuarioNaoEncontradoError
from model.repository.repo_usuario import RepoUsuario
from model.entities.usuario import Usuario
from passlib.context import CryptContext


class UsuarioService:
    def __init__(self):
        self.repo_usuario = RepoUsuario()
        self.criptografador = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Métodos deletar_user, alterar_senha , listar_usuarios

    async def cadastrar_usuario(self, usuario: Usuario, session: AsyncSession):

        usuario_procurado = await self.repo_usuario.buscar_usuario(usuario.matricula, session)

        if usuario_procurado is not None:
            raise MatriculaCadastradaError("Usuário já cadastrado!")

        if not usuario.nome:
            raise NomeInvalidaError("Nome inválido")

        if not usuario.senha or len(usuario.senha) < 8:
            raise SenhaInvalidaError("Senha inválida! Senha deve obedecer as regras!")

        if not usuario.matricula or len(usuario.matricula) < 7:
            raise MatriculaInvalidaError("Matrícula inválida! Atenda aos requisitos!")

        usuario.senha = self.criptografador.hash(usuario.senha)

        await self.repo_usuario.cadastrar_usuario(usuario, session)

    async def deletar_usuario(self,usuario_matricula: str,session: AsyncSession)-> Usuario:

        usuario = await self.repo_usuario.buscar_usuario(usuario_matricula,session)

        if not usuario:
            raise UsuarioNaoEncontradoError("Usuário não encontrado...")

        await self.repo_usuario.deletar_usuario(usuario_matricula,session)

        return usuario

    async def alterar_senha(self,usuario_matricula,nova_senha:str,session: AsyncSession):

        usuario = await self.repo_usuario.buscar_usuario(usuario_matricula,session)

        if not usuario:
            raise UsuarioNaoEncontradoError("Usuário não encontrado...")

        if not nova_senha:
            raise SenhaInvalidaError("Senha inválida! Senha deve obedecer as regras!")

        await self.repo_usuario.atualizar_senha(usuario_matricula,nova_senha,session)


    async def listar_usuarios(self,session: AsyncSession)-> list[Usuario]:

        lista_de_usuario = await self.repo_usuario.listar_usuario(session)

        if not lista_de_usuario:
            raise UsuarioNaoEncontradoError("Não há nenhum usuário cadastrado ainda...")

        return lista_de_usuario

