from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "postgres": "connected",
        "neo4j": "connected",
    }