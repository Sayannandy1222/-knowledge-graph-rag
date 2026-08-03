from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.ingestion.pipeline import ingest_pdf

router = APIRouter()

# Directory where uploaded PDFs will be stored
UPLOAD_DIR = Path("data/raw")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF and automatically:
    - Save the PDF
    - Load the PDF
    - Split into chunks
    - Generate embeddings
    - Store vectors in PostgreSQL
    - Extract entities
    - Build the Neo4j Knowledge Graph
    """

    # Allow only PDF files
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # Save uploaded file
    destination = UPLOAD_DIR / file.filename

    with open(destination, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run complete ingestion pipeline
    result = ingest_pdf(str(destination))

    return {
        "status": "success",
        "filename": file.filename,
        "chunks_created": result["chunk_count"],
        "entities_created": result["entity_count"],
        "relationships_created": result["relationship_count"],
    }