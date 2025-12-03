from openai import OpenAI
from .prompts import CREATE_SCHEMA, EXTRACT_DATA_FOR_SCHEMA, CREATE_QUERY_TO_RESPOND_TO_USER
from .models import Schema, Query
from .database import Database

# TODO: In the init create a conversation object and then the LLM always has all the context from the create schema
# to the creation of different queries
# to the answering of user questions
class LLM():
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
    
    def create_schema(self, image_url: str) -> Schema:
        return self.client.responses.parse(
            model='gpt-4.1',
            input=[
                {
                    'role': 'user',
                    'content':[
                        {'type': 'input_text', 'text': CREATE_SCHEMA},
                        {'type': 'input_image', 'image_url': image_url}
                    ]    
                }
            ],
            text_format=Schema
        ).output_parsed
    
    def extract_data_for_schema(self, schema: Schema, image_url: str) -> str:
        return self.client.responses.create(
            model='gpt-4.1',
            input=[
                {
                    'role': 'user',
                    'content':[
                        {'type': 'input_text', 'text': EXTRACT_DATA_FOR_SCHEMA.format(data_schema=schema.model_dump_json())},
                        {'type': 'input_image', 'image_url': image_url}
                    ]
                }
            ]
        ).output[0].content[0].text

    def create_query(self, user_query: str, database: Database) -> Query:
        ...