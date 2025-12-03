from unittest import TestCase
from src.database import Database
from src import models

class TestDatabase(TestCase):
    def setUp(self):
        self.database = Database()
    
    def tearDown(self):
        self.database.conn.close()

    def test_create_schema(self):
        columns = [
            models.Columns(name='Column1'),
            models.Columns(name='Column2'),
            models.Columns(name='Column3')
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

