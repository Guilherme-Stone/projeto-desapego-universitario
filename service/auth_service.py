from model.entities.usuario import Usuario
from model.repository.repo_usuario import RepoUsuario
from sqlalchemy.ext.asyncio import AsyncSession
from service.excecoes.execoes_usuario import MatriculaCadastradaError, MatriculaInvalidaError, SenhaInvalidaError, NomeInvalidaError, UsuarioNaoEncontradoError

class AuthService:

    def __init__(self):
        self.repoUsuario = RepoUsuario()
        self.flag = False

    async def login(self, usuario_matricula: str,session: AsyncSession) -> bool:
        usuario = await self.repoUsuario.buscar_usuario(usuario_matricula,session)

        if usuario is None:
            raise UsuarioNaoEncontradoError("Usuário não encontrado...")

        if not usuario:
            raise SenhaInvalidaError("Senha inválida! Senha deve obedecer as regras!")

        if not usuario.matricula:
            raise MatriculaInvalidaError("Matrícula inválida! Atenda aos requisitos!")

        self.flag = True

        return self.flag



