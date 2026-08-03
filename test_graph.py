from app.graph.neo4j_store import (
    create_entity,
    create_relationship,
)

create_entity("CUDA")
create_entity("Memory Hierarchy")
create_entity("Shared Memory")
create_entity("Global Memory")

create_relationship(
    "CUDA",
    "Memory Hierarchy",
    "HAS_COMPONENT",
)

create_relationship(
    "Memory Hierarchy",
    "Shared Memory",
    "CONTAINS",
)

create_relationship(
    "Memory Hierarchy",
    "Global Memory",
    "CONTAINS",
)

print("✅ Graph created successfully!")