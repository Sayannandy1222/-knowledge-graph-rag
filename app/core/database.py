from sqlalchemy import create_engine

from app.core.config import settings

DATABASE_URL = (
    f"postgresql://{settings.POSTGRES_USER}:"
    f"{settings.POSTGRES_PASSWORD}@"
    f"{settings.POSTGRES_HOST}:"
    f"{settings.POSTGRES_PORT}/"
    f"{settings.POSTGRES_DB}"
)

engine = create_engine(DATABASE_URL)

print("=" * 60)
print(f"DATABASE_URL = {DATABASE_URL}")
print(f"POSTGRES_USER = {settings.POSTGRES_USER}")
print(f"POSTGRES_DB = {settings.POSTGRES_DB}")
print("=" * 60)