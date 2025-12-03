from openai import OpenAI
from prompts import CREATE_SCHEMA, CREATE_QUERY_TO_RESPOND_TO_USER
from models import Schema, Query
from database import Database

# TODO: In the init create a conversation object and then the LLM always has all the context from the create schema
# to the creation of different queries
# to the answering of user questions
class LLM():
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
    
    def create_schema(self, image_url: str) -> str:
        return self.client.completions.create(
            model='gpt-4.1',
            messages=[
                {
                    'role': 'user',
                    'content':[
                        {'type': 'text', 'text': CREATE_SCHEMA},
                        {'type': 'image-url', 'image_url': image_url}
                    ]    
                }
            ],
            response_format=Schema
        ).choices[0].message.content
    

    def create_query(self, user_query: str, database: Database) -> Query:
        ...