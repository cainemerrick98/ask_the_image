import sqlite3
from collections import defaultdict
from .models import Schema, Table, Query

class Database():
    """
    represents an in memory database
    """
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.tables = []
        self.relationships = defaultdict(list)

    def create_schema(self, schema: Schema):
        for table in schema.tables:
            self._create_table(table)
    
        self.conn.commit()
        
        for relationship in schema.relationships:
            self.relationships[relationship.case_table].append(relationship.fact_table)

    def query(self, query: Query) -> list:
        ...

    def insert_data(self, table_name: str, data: list[list]):
        self.cursor.execute(
            f"""
            INSERT INTO {table_name} VALUES
            {chr(10).join([",".join(row) for row in data])};
            """
        )
        self.conn.commit()
    
    def _create_table(self, table: Table):
        self.tables.append(table.name)
        self.cursor.execute(
            f"""
            CREATE TABLE {table.name}({",".join([col.name for col in table.columns])});
            """
        )
        