from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from schemas.tacheCreation import TacheCreation
from models.tache import Tache


def createTache( t :TacheCreation,db : Session):
    try:
        db_tache = Tache(
            title       = t.titre,
            description = t.description,
            etat        = t.etat.value,
            dateEch     = t.dateEch,
            dateCre     = t.dateCre,
            dateMaj     = t.dateMaj
        )
        db.add(db_tache)
        db.commit()
        db.refresh(db_tache)
        return db_tache
    except SQLAlchemyError as e:
        db.rollback()
        raise

# def updateTache(id : int, tache: Tache, db : Session):
#     pass
#
# def getTaches(db : Session):
#     pass
#
# def getTache(id : int,db : Session):
#     pass
#
# def deleteTache(id : int,db : Session):
#     pass
