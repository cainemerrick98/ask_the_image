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
import re


def normalize_sql(sql: str) -> str:
    """
    this solves the problem of comparing triple quotes strings :)
    """
    # Remove leading/trailing whitespace
    sql = sql.strip()

    # Replace any sequence of whitespace (spaces, tabs, newlines) with a single space
    sql = re.sub(r'\s+', ' ', sql)

    # Remove space before commas and ensure one space after commas
    sql = re.sub(r'\s*,\s*', ', ', sql)

    return sql

class TestModels(TestCase):

    def test_build_simple_query(self):
        expected_result = """
        SELECT Col1,Col2
        FROM Table1
        """
        query = Query(
            table_name='Table1',
            columns=[QueryColumn(name='Col1'), QueryColumn(name='Col2')]
        )
        self.assertEqual(normalize_sql(expected_result), normalize_sql(query.to_string()))

    def test_build_query_with_agg(self):
        expected_result = """
        SELECT SUM(Col1)
        FROM Table1
        """
        query = Query(
            table_name='Table1',
            columns=[QueryColumn(name='Col1', aggregation=Aggregation.SUM)]
        )
        self.assertEqual(normalize_sql(expected_result), normalize_sql(query.to_string()))
    
    def test_build_query_with_filters(self):
        expected_result = """
        SELECT Col1,Col2
        FROM Table1
        WHERE Col1 < 10 AND Col2 IS NULL
        """
        query = Query(
            table_name='Table1',
            columns=[QueryColumn(name='Col1'), QueryColumn(name='Col2')],
            filters=[
                Filter(column='Col1', operator=Operator.LESS_THAN, value=10),
                Filter(column='Col2', operator=Operator.IS_NULL, value=None)
            ]
        )
        self.assertEqual(normalize_sql(expected_result), normalize_sql(query.to_string()))

    def test_build_query_with_groupby(self):
        expected_result = """
        SELECT SUM(Col2)
        FROM Table1
        GROUP BY Col1
        """
        query = Query(
            table_name='Table1',
            columns=[QueryColumn(name='Col2', aggregation=Aggregation.SUM)],
            groupby=[GroupBy(column='Col1')]
        )
        self.assertEqual(normalize_sql(expected_result), normalize_sql(query.to_string()))

    def test_build_query_with_orderby(self):
        expected_result = """
        SELECT Col1, Col2
        FROM Table1
        ORDER BY Col1 ASC, Col2 DESC
        """
        query = Query(
            table_name='Table1',
            columns=[QueryColumn(name='Col1'), QueryColumn(name='Col2')],
            orderby=[
                OrderBy(column='Col1', sorting=Sorting.ASC), 
                OrderBy(column='Col2', sorting=Sorting.DESC)
            ]
        )
        self.assertEqual(normalize_sql(expected_result), normalize_sql(query.to_string()))