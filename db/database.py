from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


user = "apitacheuser"
password = "motDePasse"
dbname = "apitache"
DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@localhost:5432/{dbname}"
engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()