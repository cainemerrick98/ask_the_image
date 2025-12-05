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
        result = self.conn.execute(query.to_string()).fetchall()
        return result


    def insert_data(self, table_name: str, data: list[list]):
        num_cols = len(data[0])
        placeholders = "(" + ",".join(["?"] * num_cols) + ")"
        insert = f"INSERT INTO {table_name} VALUES {','.join([placeholders] * len(data))}"

        # Flatten the list of lists into a single tuple for executemany-style params
        params = [item for row in data for item in row]

        self.cursor.execute(insert, params)
        self.conn.commit()
    
    def _create_table(self, table: Table):
        self.tables.append(table.name)
        self.cursor.execute(
            f"""
            CREATE TABLE {table.name}({",".join([col.name for col in table.columns])});
            """
        )
        