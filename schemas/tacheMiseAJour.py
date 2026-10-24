from datetime import date

from pydantic import BaseModel, Field
from enum import Enum

class Etat(str, Enum):
    AFAIRE = "A faire"
    ENCOURS = "En cours"
    TERMINEE = "Termine"

class TacheMiseAJour(BaseModel):
    titre       : str = Field(min_length=1)
    description : str = Field(min_length=1)
    etat        : Etat
    dateEch     : date
    dateMaj     : date = date.today()