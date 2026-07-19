from contextlib import asynccontextmanager
from fastapi import FastAPI
from config.database import Database
from routes.routes_u import router

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

app.include_router(router)