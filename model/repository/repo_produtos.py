from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, session
from model.entities.produto import Produto


class RepoProduto:

    def __init__(self):
        self.produto = Produto()

    async def cadastra_produto(self,produto: Produto,session: AsyncSession) -> Produto:
         session.add(produto)
         await session.commit()
         await session.refresh(produto)

         return produto

    async def  buscar_produto(self,produto_id, session: AsyncSession) -> Produto:
        resultado = await session.execute(
            select(Produto).where(Produto.id==produto_id)
        )

        return resultado.scalar_one_or_none()

    async def listar_produtos(self,session: AsyncSession) -> list[Produto]:
        resultado = await session.execute(
            select(Produto)
        )

        return resultado.scalars().all()

    async def atualizar_produto(self, novoProduto: Produto,session: AsyncSession) -> Produto:
        resultado = await session.execute(
            select(Produto).where(Produto.id==novoProduto.id)
        )

        produto = resultado.scalars().first()

        produto.nome = novoProduto.nome
        produto.quantidade = novoProduto.quantidade
        produto.doado = novoProduto.doado
        produto.negociador = novoProduto.negociador

        await session.commit()
        await session.refresh(produto)

        return produto


    async def deletar_produto(self,produto_id,session: AsyncSession) -> Produto:
        resultado = await session.execute(
            select(Produto).where(Produto.id == produto_id)
        )
        produto = resultado.scalar_one_or_none()

        await session.delete(produto)
        await session.commit()

        return produto

