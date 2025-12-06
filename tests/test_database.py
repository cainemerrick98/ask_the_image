from unittest import TestCase
from src.database import Database
from src import models
from src.models import (
    Query, 
    QueryColumn, 
    Filter, 
    GroupBy, 
    OrderBy, 
    Operator,
    Aggregation,
    Sorting,
    OR
)

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
        database_data =  [[row[column.name] for column in table.columns] for row in menu_data['tables'][0]['columns']]
        self.database.insert_data(table.name, database_data)

        max_price = self.database.conn.execute('SELECT MAX(solo_price) FROM menu_items').fetchone()[0]
        self.assertEqual(max_price, 5.99)


    def test_queries_on_schema(self):
        self.database.create_schema(menu_schema)
        table = menu_schema.tables[0]
        database_data =  [[row[column.name] for column in table.columns] for row in menu_data['tables'][0]['columns']]
        self.database.insert_data(table.name, database_data)

        #Queries
        max_solo_query = Query(
            table_name='menu_items',
            columns=[QueryColumn(name='solo_price', aggregation=Aggregation.MAX)]
        )
        result = self.database.query(max_solo_query)
        self.assertEqual(result[0][0], 5.99)

        cheeseburger_prices = Query(
            table_name='menu_items',
            columns=[
                QueryColumn(name='solo_price'),
                QueryColumn(name='meal_price')
            ],
            filters=[
                Filter(
                    column='item',
                    operator=Operator.EQUAL,
                    value='CHEESEBURGER'
                )
            ]
        )
        result = self.database.query(cheeseburger_prices)
        self.assertEqual(result[0], (2.79, 6.59))

        most_expensive_breakfast_item = Query(
            table_name='menu_items',
            columns=[
                QueryColumn(name='item'),
                QueryColumn(name='solo_price'),
            ],
            filters=[
                Filter(
                    column='category',
                    operator=Operator.EQUAL,
                    value='BREAKFAST'
                )
            ],
            orderby=[
                OrderBy(column='solo_price', sorting=Sorting.DESC)
            ]
        )
        result = self.database.query(most_expensive_breakfast_item)
        self.assertEqual(result[0], ('BIG BREAKFAST® WITH HOTCAKES', 5.49))

        most_expensive_quarter_or_double = Query(
            table_name='menu_items',
            columns=[
                QueryColumn(name='item'),
            ],
            filters=[
                OR(filters=[
                    Filter(
                        column='item',
                        operator=Operator.LIKE,
                        value='%QUARTER%'
                    ),
                    Filter(
                        column='item',
                        operator=Operator.LIKE,
                        value='%DOUBLE%'
                    )
                ])    
            ],
            orderby=[
                OrderBy(column='solo_price', sorting=Sorting.DESC)
            ]
        )

        result = self.database.query(most_expensive_quarter_or_double)
        self.assertEqual(result[0][0], 'QUARTER POUNDER® WITH CHEESE BACON')