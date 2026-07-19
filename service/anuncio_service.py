from sqlalchemy.ext.asyncio import AsyncSession
from model.entities.anuncio import Anuncio
from model.repository.repo_anuncios import RepoAnuncio
from service.excecoes.execoes_anuncio import AnuncioNaoEncontradoError, AnuncioInvalidoError
from service.excecoes.execoes_produto import ProdutoNaoEncontradoError, ProdutoInvalidoError


class AnuncioService:

    def __init__(self):
        self.repo_anuncio = RepoAnuncio()

    async def adicionar_anuncio(self, anuncio: Anuncio, session: AsyncSession):

        if not anuncio:
            raise AnuncioInvalidoError("Produto inválido!")

        await self.repo_anuncio.cadastra_anuncio(anuncio, session)


    async def deletar_anuncio(self, anuncio_id:int, session: AsyncSession):

        anuncio = await self.repo_anuncio.buscar_anuncio(anuncio_id, session)

        if not anuncio:
            raise AnuncioNaoEncontradoError("Anúncio não encontrado!")

        await self.repo_anuncio.deletar_anuncio(anuncio_id, session)


    async def atualizar_anuncio(self, anuncio_id, novo_anuncio: Anuncio, session: AsyncSession):
        anuncio = await self.repo_anuncio.buscar_anuncio(anuncio_id, session)

        if not anuncio:
            raise ProdutoNaoEncontradoError("Anúncio não encontrado!")

        await self.repo_anuncio.atualizar_anuncio(novo_anuncio,session)


    async def procurar_anuncios(self,anuncio_id: Anuncio,session: AsyncSession):
        anuncio = await self.repo_anuncio.buscar_anuncio(anuncio_id, session)

        if not anuncio:
            raise AnuncioNaoEncontradoError("Anúncio não encontrado!")
        pass

        if not anuncio:
            raise ProdutoInvalidoError("Produto inválido!")

    async def listar_anuncios(self, anuncio_id, session: AsyncSession):
        anuncio = await self.repo_anuncio.buscar_anuncio(anuncio_id, session)

        if not anuncio:
            raise ProdutoNaoEncontradoError("Produto não encontrado!")

        return anuncio




