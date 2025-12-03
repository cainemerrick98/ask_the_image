from dotenv import load_dotenv
import os
from unittest import TestCase

from src.llm import LLM

load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY')

class TestLLM(TestCase):
    def setUp(self):
        self.llm = LLM(OPENAI_KEY)
        return super().setUp()
    
    def test_create_schema():
        ...