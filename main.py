# This is a sample Python script.
from fastapi import FastAPI,Depends
from starlette.exceptions import HTTPException

from schemas.tacheCreation import TacheCreation
from schemas.tacheMiseAJour import TacheMiseAJour
from sqlalchemy.orm import Session
from db.database import SessionLocal
from crud import tache

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



app = FastAPI( title="API de gestion des tâches",
               description="""
              Cette application permet de : 
              -Lister les tâches
              -récupérer les détails d'une tâche
              -Ajouter une tâche
              -Mettre à jour une tâche
              -Supprimer une tâche
""")

# 1. Verb Methode Get

@app.get("/taches/",
         summary="Récupérer toutes les tâches",
         description="Toutes les tâche de la BDD se retrouve dans un JSON",
         response_description="Liste de toutes les tâche au format JSON")
def getAllTaches(db : Session = Depends(get_db)):
    return {"message": "Fonction qui va récupérer toutes les tâches"}


# 2. Verb Methode Get Id
@app.get("/taches/{id}")
def getTache(tache_id: int):
    return {"message":f'Récupération des infos de la tache {tache_id}'}

# 3. Verb Methode Post
@app.post("/taches/")
def createTache(t: TacheCreation,db : Session = Depends(get_db)):
    try:
        db_tache = tache.createTache(t,db)
        return db_tache
    except Exception :
        raise  HTTPException(status_code=500, detail="Erreur interne")

"""
# 4. Verb Methode Put
@app.put("/taches/{id}")
def updateTache(id: int, t: TacheCreation,db : Session = Depends(get_db)):
    return {"message":f"Je vais modifier la tache {id}", "nouvelleValeur" : t}

# 5. Verb Methode Delete
@app.delete("/taches/{id}")
def deleteTache(id: int):
    return {"message":f"Je vais supprimer la tache {id}"}
"""
