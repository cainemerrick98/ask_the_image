from dotenv import load_dotenv
import os
from unittest import TestCase
from tabulate import tabulate

from .fixtures import menu_schema, menu_data, menu_data_database
from src.llm import LLM
from src.database import Database


load_dotenv()

api_key = os.getenv('OPENAI_KEY')

# Here I just want to see what kind of queries are being created in response
# To different questions and see what context the model sees
# Without always running main

class TestIntegration(TestCase):

    def setUp(self):
        self.database = Database()
        self.llm = LLM(api_key)

        self.database.create_schema(menu_schema)
        self.database.insert_data('menu_items', menu_data_database)
        return super().setUp()

    def test_max_solo_price_query(self):
        user_query = "What is the most expensive menu item by solo price"
        
        sql_query = self.llm.create_query(user_query, menu_schema)
        print(sql_query)

        query_result = self.database.query(sql_query)
        print(tabulate(query_result, [col.name for col in sql_query.columns], tablefmt='pretty'))

        answer = self.llm.answer(user_query, query_result, sql_query)
        print(answer)
    
    def test_most_expensive_breakfast_item(self):
        user_query = "What is the most expensive breakfast item"
        
        sql_query = self.llm.create_query(user_query, menu_schema)
        print(sql_query)

        query_result = self.database.query(sql_query)
        print(tabulate(query_result, [col.name for col in sql_query.columns], tablefmt='pretty'))

        answer = self.llm.answer(user_query, query_result, sql_query)
        print(answer)

    def test_most_expensive_quarter_or_double(self):
        user_query = "What is the most expensive item with quarter or double in its name"
        
        sql_query = self.llm.create_query(user_query, menu_schema)
        print(sql_query)

        query_result = self.database.query(sql_query)
        print(tabulate(query_result, [col.name for col in sql_query.columns], tablefmt='pretty'))

        answer = self.llm.answer(user_query, query_result, sql_query)
        print(answer)
