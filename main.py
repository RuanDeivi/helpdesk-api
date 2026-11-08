from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import Base, engine, get_db
import models
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Help Desk API")


@app.get("/")
def raiz():
    return {"mensagem": "API de chamados funcionando!"}


@app.post("/chamados", response_model=schemas.ChamadoSaida, status_code=201)
def criar_chamado(dados: schemas.ChamadoCriar, db: Session = Depends(get_db)):
    chamado = models.Chamado(**dados.model_dump())
    db.add(chamado)
    db.commit()
    db.refresh(chamado)
    return chamado


@app.get("/chamados", response_model=list[schemas.ChamadoSaida])
def listar_chamados(db: Session = Depends(get_db)):
    return db.query(models.Chamado).all()


@app.get("/chamados/{chamado_id}", response_model=schemas.ChamadoSaida)
def buscar_chamado(chamado_id: int, db: Session = Depends(get_db)):
    chamado = db.get(models.Chamado, chamado_id)
    if not chamado:
        raise HTTPException(status_code=404, detail="Chamado não encontrado")
    return chamado


@app.patch("/chamados/{chamado_id}", response_model=schemas.ChamadoSaida)
def atualizar_chamado(
    chamado_id: int,
    dados: schemas.ChamadoAtualizar,
    db: Session = Depends(get_db),
):
    chamado = db.get(models.Chamado, chamado_id)
    if not chamado:
        raise HTTPException(status_code=404, detail="Chamado não encontrado")
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(chamado, campo, valor)
    db.commit()
    db.refresh(chamado)
    return chamado