from .llm import LLM
from .database import Database
from .utils import encode_image_to_base64

from dotenv import load_dotenv
import os
import json
from tabulate import tabulate

load_dotenv()

api_key = os.getenv('OPENAI_KEY')

def main():
    database = Database()
    model = LLM(api_key)

    while True:
        image_path = input('Please input the path to your image: ')
        try:
            image_url = encode_image_to_base64(image_path)
            break
        except Exception:
            continue
    
    print('Creating schema for image data...')
    schema = model.create_schema(image_url)
    print(f'Heres the schema I came up with {schema.model_dump_json()}')
    database.create_schema(schema)
    print('Schema successfully created!')

    print('Loading data into schema...')
    data = json.loads(model.extract_data_for_schema(schema, image_url))
    for table_data in data['tables']:
        table_name = table_data['name']
        table_schema = [t for t in schema.tables if t.name == table_name][0]
        table_data = [[row[column.name] for column in table_schema.columns] 
                      for row in table_data['columns']]
        database.insert_data(table_name, table_data)
    
    print(len(database.conn.execute(f'SELECT * FROM {table_name}').fetchall()))
        
    print('Data loaded')

    print('I am ready to answer any question about the data in the image. To exit just type exit')
    while True:
        user_query = input()
        if user_query.lower().strip() == 'exit':
            break
        
        sql_query = model.create_query(user_query, schema)
        print(sql_query)
        query_result = database.query(sql_query)
        answer = model.answer(user_query, query_result, sql_query)
        print('Query Result:')
        print(tabulate(query_result, [col.name for col in sql_query.columns], tablefmt='pretty'))
        print('Answer')
        print(answer)

        


if __name__ == '__main__':
    main()

    