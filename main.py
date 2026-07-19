from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from config.database import Database

db = Database()


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Inicializando banco de dados...")

    await db.init_db()

    print("Banco inicializado!")

    yield

    print("Encerrando aplicação...")

app = FastAPI(
    title="Projeto Desapego Universitário",
    lifespan=lifespan
)

if __name__ == "__main__":
    lifespan(app)