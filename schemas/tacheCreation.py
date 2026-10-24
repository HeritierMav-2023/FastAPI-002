from datetime import date

from pydantic import BaseModel, Field
from enum import Enum

class Etat(str, Enum):
    AFAIRE = "A faire"
    ENCOURS = "En cours"
    TERMINEE = "Termine"

class TacheCreation(BaseModel):
    titre       : str = Field(min_length=1)
    description : str = Field(min_length=1)
    etat        : Etat
    dateEch     : date
    dateCre     : date =  date.today()
    dateMaj     : date = date.today()