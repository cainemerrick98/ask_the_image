# Only here to test the query building logic
from src.models import (
    Query, 
    QueryColumn, 
    Filter, 
    GroupBy, 
    OrderBy, 
    Operator,
    Aggregation,
    Sorting
)
from unittest import TestCase

class TestModels(TestCase):

    def test_build_simple_query(self):
        # Using doc strings is a pretty rubbish way to test this as leaving a space can cause a fail!   
        # Same applies below
        # Its not like we can just strip as the spaces are important (new lines aren't though)
        expected_result = """
        SELECT Col1,Col2
        FROM Table1
        """
        query = Query(
            table_name='Table1',
            columns=[QueryColumn(name='Col1'), QueryColumn(name='Col2')]
        )
        self.assertEqual(expected_result, query.to_string())

    def test_build_query_with_agg(self):
        expected_result = """
        SELECT SUM(Col1)
        FROM Table1
        """
        query = Query(
            table_name='Table1',
            columns=[QueryColumn(name='Col1', aggregation=Aggregation.SUM)]
        )
        self.assertEqual(expected_result, query.to_string())
    
    def test_build_query_with_filters(self):
        expected_result = """
        SELECT Col1,Col2
        FROM Table1
        WHERE Col1 < 10
        """
        query = Query(
            table_name='Table1',
            columns=[QueryColumn(name='Col1'), QueryColumn(name='Col2')],
            filters=[Filter(column='Col1', operator=Operator.LESS_THAN, value=10)]
        )
        print(query.to_string())
        print(expected_result)
        self.assertEqual(expected_result, query.to_string())