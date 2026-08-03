from neo4j import GraphDatabase

from app.core.config import settings

driver = GraphDatabase.driver(
    settings.NEO4J_URI,
    auth=(settings.NEO4J_USERNAME, settings.NEO4J_PASSWORD),
)


def graph_search(entity: str):
    query = """
    MATCH (a:Entity {name: $entity})-[r]->(b)
    RETURN a.name AS source,
           type(r) AS relation,
           b.name AS target
    """

    with driver.session() as session:
        results = session.run(query, entity=entity)

        return [record.data() for record in results]