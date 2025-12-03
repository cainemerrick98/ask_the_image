from dotenv import load_dotenv
import os
import json
from unittest import TestCase

from src.llm import LLM
from src.utils import encode_image_to_base64
from src.models import Schema, Table, Column

load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY')

# I know we should mock the LLM class here to avoid having a test dependent on an API
# But I dont care
class TestLLM(TestCase):
    def setUp(self):
        self.llm = LLM(OPENAI_KEY)
        self.menu_image_url = encode_image_to_base64('tests/test_images/mcdonalds_menu.jpg')
        return super().setUp()
    
    def test_create_schema(self):
        menu_schema = self.llm.create_schema(self.menu_image_url)
        self.assertIsInstance(menu_schema, Schema)
    
    def test_extract_data(self):
        menu_schema = Schema(
            tables=[
                Table(name='menu_items', columns=[
                    Column(name='category'), 
                    Column(name='item'), 
                    Column(name='solo_price'), 
                    Column(name='meal_price')
                    ]
                )
            ], 
            relationships=None
        )
        data = self.llm.extract_data_for_schema(menu_schema, self.menu_image_url)
        
        # If this is successful we're good
        data = json.loads(data)
        
        