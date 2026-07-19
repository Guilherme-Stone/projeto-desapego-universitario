from sqlalchemy.ext.asyncio import AsyncSession

from model.entities.produto import Produto
from model.repository.repo_produtos import RepoProduto
from service.excecoes.execoes_produto import ProdutoNaoEncontradoError, ProdutoInvalidoError


class ProdutoService:

    def __init__(self):
        self.repo_produto = RepoProduto()

    async def adicionar_produto(self, produto: Produto,session: AsyncSession):

        if not produto:
            raise ProdutoInvalidoError("Produto inválido!")

        await self.repo_produto.cadastra_produto(produto,session)


    async def deletar_produto(self,produto_id:int , session: AsyncSession):

        produto = await self.repo_produto.buscar_produto(produto_id,session)

        if not produto:
            raise ProdutoNaoEncontradoError("Produto não encontrado!")

        await self.repo_produto.deletar_produto(produto_id,session)


    async def atualizar_produto(self,produto_id, novo_produto: Produto,session: AsyncSession):
        produto = await self.repo_produto.buscar_produto(produto_id,session)

        if not produto:
            raise ProdutoNaoEncontradoError("Produto não encontrado!")

        await self.repo_produto.atualizar_produto(produto,session)


    async def procurar_produto(self,produto_id: Produto,session: AsyncSession):
        produto = await self.repo_produto.buscar_produto(produto_id, session)

        if not produto:
            raise ProdutoNaoEncontradoError("Produto não encontrado!")
        pass

        if not produto:
            raise ProdutoInvalidoError("Produto inválido!")

    async def listar_produtos(self,session: AsyncSession):
        produto = await self.repo_produto.listar_produtos(session)

        if not produto:
            raise ProdutoNaoEncontradoError("Produto não encontrado!")

        return produto


