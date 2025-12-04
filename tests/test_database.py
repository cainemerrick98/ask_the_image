from unittest import TestCase
from src.database import Database
from src import models

from .fixtures import menu_schema, menu_data

class TestDatabase(TestCase):
    def setUp(self):
        self.database = Database()
    
    def tearDown(self):
        self.database.conn.close()

    def test_create_schema(self):
        columns = [
            models.Column(name='Column1', data_type='string'),
            models.Column(name='Column2', data_type='string'),
            models.Column(name='Column3', data_type='string')
        ]
        table_1 = models.Table(
            name='Table1',
            columns=columns
        )
        schema = models.Schema(tables=[table_1])
        
        self.database.create_schema(schema)

        self.assertListEqual(
            self.database.tables,
            ['Table1']
        )

        self.assertEqual(
            self.database.conn.execute('SELECT * FROM Table1').fetchall(),
            []
        )

    def test_insert_data_to_schema(self):
        self.database.create_schema(menu_schema)
        table = menu_schema.tables[0]
        database_data =  [[row[column.name] or 'Null' for column in table.columns] for row in menu_data['tables'][0]['columns']]
        print(database_data)
        self.database.insert_data(table.name, database_data)

        max_price = self.database.conn.execute('SELECT MAX(solo_price) FROM menu_items').fetchone()
        self.assertEqual(max_price, 5.99)
