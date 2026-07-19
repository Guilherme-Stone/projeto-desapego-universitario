from sqlalchemy.ext.asyncio import AsyncSession
from model.entities.usuario import Usuario
from sqlalchemy import select

class RepoUsuario:
    async def cadastrar_usuario(self, usuario: Usuario, session: AsyncSession) -> Usuario:
        session.add(usuario)
        await session.commit()
        await session.refresh(usuario)
        return usuario

    async def buscar_usuario(self, usuario_matricula: str, session: AsyncSession) -> Usuario:
        resultado = await session.execute(
            select(Usuario).where(Usuario.matricula == usuario_matricula)
        )

        return resultado.scalar_one_or_none()

    async def listar_usuario(self,session: AsyncSession) -> list[Usuario]:
        resultado = await session.execute(
            select(Usuario)
        )

        return resultado.scalars().all()

    async def atualizar_senha(self, usuario: Usuario, novaSenha: str, session: AsyncSession) -> Usuario:
        resultado = await session.execute(
            select(Usuario).where(Usuario.id == usuario.id)
        )

        estudante = resultado.scalar_one_or_none()

        usuario.senha = novaSenha

        await session.commit()
        await session.refresh(usuario)

        return usuario

    async def deletar_usuario(self,usuario_matricula: str, session: AsyncSession) -> Usuario:

        resultado = await session.execute(
            select(Usuario).where(Usuario.matricula == usuario_matricula)
        )

        usuario = resultado.scalars().first()

        await session.delete(usuario)
        await session.commit()

        return usuario