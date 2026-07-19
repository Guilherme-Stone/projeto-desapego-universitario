import asyncio
from config.database import db
from model.repository.repo_usuario import RepoUsuario
from model.entities.usuario import Usuario
from model.entities.produto import Produto
from model.entities.anuncio import Anuncio


async def main():
    repo = RepoUsuario()

    async with db.session_maker() as session:

        estudante =Usuario(
            id=1,
            matricula="123333333",
            nome="Guilherme",
            produtos=[],
            anuncios=[],
            senha="122222222"
        )

        await repo.cadastrar_usuario(estudante, session)

        print("ID:", estudante.id)
        print("Nome:", estudante.nome)

        estudante_db = await repo.buscar_usuario(estudante.matricula, session)

        print(estudante_db)


if __name__ == "__main__":
    asyncio.run(main())