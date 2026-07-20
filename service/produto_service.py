from sqlalchemy.ext.asyncio import AsyncSession
from model.entities.produto import Produto
from model.repository.repo_produtos import RepoProduto
from service.excecoes.execoes_produto import ProdutoNaoEncontradoError, ProdutoInvalidoError, ProdutoCadastradoError
from service.excecoes.execoes_usuario import UsuarioInvalidoError


class ProdutoService:

    def __init__(self):
        self.repo_produto = RepoProduto()

    async def adicionar_produto(self,usuario_id:int,produto: Produto,session: AsyncSession) -> Produto | None:

        verificar_produto = await self.repo_produto.buscar_produto(produto_id=produto.id,session=session)

        if usuario_id != produto.usuario_id:
            raise UsuarioInvalidoError("Usuário atual não é dono do produto!")

        if not verificar_produto:
            raise ProdutoCadastradoError("Produto já cadastrado")

        if not produto:
            raise ProdutoInvalidoError("Produto inválido!")


        await self.repo_produto.cadastra_produto(produto,session)


    async def deletar_produto(self,usuario_id: int,produto_id:int , session: AsyncSession)->Produto | None:

        produto = await self.repo_produto.buscar_produto(produto_id,session)

        if usuario_id != produto.usuario_id:
            raise UsuarioInvalidoError("Usuário atual não é dono do produto!")

        if not produto:
            raise ProdutoNaoEncontradoError("Produto não encontrado!")

        await self.repo_produto.deletar_produto(produto_id,session)


    async def atualizar_produto(self,usuario_id:str,produto_id, novo_produto: Produto,session: AsyncSession) ->  Produto | None:
        produto = await self.repo_produto.buscar_produto(produto_id,session)

        if usuario_id != produto.usuario_id:
            raise UsuarioInvalidoError("Usuário atual não é dono do produto!")

        if not produto:
            raise ProdutoNaoEncontradoError("Produto não encontrado!")

        await self.repo_produto.atualizar_produto(novo_produto,session)


    async def procurar_produto(self,produto_id: int,session: AsyncSession)-> Produto | None:
        produto = await self.repo_produto.buscar_produto(produto_id, session)

        if not produto:
            raise ProdutoNaoEncontradoError("Produto não encontrado!")
        pass

    async def listar_produtos(self,session: AsyncSession):
        produto = await self.repo_produto.listar_produtos(session)

        if not produto:
            raise ProdutoNaoEncontradoError("Produto não encontrado!")

        return produto


