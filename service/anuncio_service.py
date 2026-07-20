from sqlalchemy.ext.asyncio import AsyncSession
from model.entities.anuncio import Anuncio
from model.repository.repo_anuncios import RepoAnuncio
from service.excecoes.execoes_anuncio import AnuncioNaoEncontradoError, AnuncioInvalidoError, AnuncioCadastradoError
from service.excecoes.execoes_produto import ProdutoNaoEncontradoError, ProdutoInvalidoError
from service.excecoes.execoes_usuario import UsuarioInvalidoError


class AnuncioService:

    def __init__(self):
        self.repo_anuncio = RepoAnuncio()

    async def adicionar_anuncio(self,usuario_id: int, anuncio: Anuncio, session: AsyncSession) -> Anuncio | None:
        anuncio_c = await self.repo_anuncio.buscar_anuncio(anuncio.id, session)

        if not anuncio_c:
            raise AnuncioCadastradoError("Anúncio já cadastrado")

        if usuario_id != anuncio.usuario_id:
            raise UsuarioInvalidoError("Usuário atual não pode fazer anúncio!")

        if not anuncio:
            raise AnuncioInvalidoError("Anúncio inválido!")

        if anuncio.doado:
            anuncio.preco = 0

        await self.repo_anuncio.cadastra_anuncio(anuncio, session)


    async def deletar_anuncio(self, usuario_id:int,anuncio_id:int, session: AsyncSession)-> Anuncio | None:

        anuncio = await self.repo_anuncio.buscar_anuncio(anuncio_id, session)

        if usuario_id != anuncio.usuario_id:
            raise UsuarioInvalidoError("Usuário atual não pode fazer anúncio!")

        if not anuncio:
            raise AnuncioNaoEncontradoError("Anúncio não encontrado!")

        await self.repo_anuncio.deletar_anuncio(anuncio_id, session)


    async def atualizar_anuncio(self,usuario_id:int, anuncio_id:int, novo_anuncio: Anuncio, session: AsyncSession)-> Anuncio | None:
        anuncio = await self.repo_anuncio.buscar_anuncio(anuncio_id, session)

        if usuario_id != anuncio.usuario_id:
            raise UsuarioInvalidoError("Usuário atual não pode fazer anúncio!")

        if not anuncio:
            raise ProdutoNaoEncontradoError("Anúncio não encontrado!")

        await self.repo_anuncio.atualizar_anuncio(novo_anuncio,session)


    async def procurar_anuncios(self,anuncio_id: int,session: AsyncSession)-> Anuncio | None:
        anuncio = await self.repo_anuncio.buscar_anuncio(anuncio_id, session)

        if not anuncio:
            raise AnuncioNaoEncontradoError("Anúncio não encontrado!")
        pass

        if not anuncio:
            raise AnuncioInvalidoError("Anúncio inválido!")

    async def listar_anuncios(self, session: AsyncSession)-> list[Anuncio] | None:
        anuncio = await self.repo_anuncio.listar_anuncios(session)

        if not anuncio:
            raise AnuncioNaoEncontradoError("Anúncio não encontrado!")

        return anuncio




