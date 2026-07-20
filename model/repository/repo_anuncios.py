from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, session

from model.entities.anuncio import Anuncio


class RepoAnuncio():

    def __init__(self):
        self.anuncio = Anuncio()

    async def cadastra_anuncio(self,anuncio: Anuncio,session: AsyncSession) -> Anuncio:
         session.add(anuncio)
         await session.commit()
         await session.refresh(anuncio)

         return anuncio

    async def  buscar_anuncio(self,anuncio_id, session: AsyncSession) -> Anuncio:
        resultado = await session.execute(
            select(Anuncio).where(Anuncio.id==anuncio_id)
        )

        return resultado.scalar_one_or_none()

    async def listar_anuncios(self,session: AsyncSession) -> list[Anuncio]:
        resultado = await session.execute(
            select(Anuncio)
        )

        return resultado.scalars().all()

    async def atualizar_anuncio(self, novoAnuncio: Anuncio,session: AsyncSession) -> Anuncio:
        resultado = await session.execute(
            select(Anuncio).where(Anuncio.id==novoAnuncio.id)
        )

        anuncio = resultado.scalars().first()

        anuncio.nome = novoAnuncio.nome
        anuncio.preco = novoAnuncio.preco
        anuncio.data_inicio = novoAnuncio.data_inicio
        anuncio.doado = novoAnuncio.doado

        await session.commit()
        await session.refresh(anuncio)

        return anuncio


    async def deletar_anuncio(self,anuncio_id,session: AsyncSession) -> Anuncio:
        resultado = await session.execute(
            select(Anuncio).where(Anuncio.id == anuncio_id)
        )
        anuncio = resultado.scalar_one_or_none()

        await session.delete(anuncio)
        await session.commit()

        return anuncio

