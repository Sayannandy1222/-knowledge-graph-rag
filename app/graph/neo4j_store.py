from neo4j import GraphDatabase

from app.core.config import settings


driver = GraphDatabase.driver(
    settings.NEO4J_URI,
    auth=(settings.NEO4J_USERNAME, settings.NEO4J_PASSWORD),
)


def create_entity(name: str):
    """
    Create an entity node if it doesn't already exist.
    """

    query = """
    MERGE (e:Entity {name: $name})
    """

    with driver.session() as session:
        session.run(query, name=name)


def create_relationship(source: str, relation: str, target: str):
    """
    Create a relationship between two entities.
    """

    query = f"""
    MERGE (a:Entity {{name: $source}})
    MERGE (b:Entity {{name: $target}})
    MERGE (a)-[r:{relation}]->(b)
    """

    with driver.session() as session:
        session.run(
            query,
            source=source,
            target=target,
        )


def insert_entities(entities):
    """
    Insert all entities into Neo4j.
    """

    for entity in entities:
        create_entity(entity)


def insert_relationships(relationships):
    """
    Insert all relationships into Neo4j.
    """

    for rel in relationships:
        create_relationship(
            rel["source"],
            rel["relation"],
            rel["target"],
        )


def close():
    """
    Close Neo4j driver.
    """

    driver.close()