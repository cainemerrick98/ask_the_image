CREATE_SCHEMA = """
You will be given an image.
Your job is to convert the information in the image into a structured data schema that makes the content easy to query conversationally.

Guidelines for schema desing:
1. Prefer simple, flat structures when possible. 
Use lists of objects rather than deeply nested schemas.

2. Avoid unnecessary relationships. 
Only include relationships if absolutely required for typical questions.
Design schemas around the kinds of questions a user would reasonably ask.
(Example: If the image is a timetable, users will ask about times, routes, locations.)

3. Only include data that appears in the image.
Do not infer or hallucinate extra data.

4. Keep field names short, descriptive, and consistent.

5. Output MUST follow the schema format exactly (defined in the response format section).
"""

EXTRACT_DATA_FOR_SCHEMA =  """
You will be given an image and a data schema.

Your task is to extract data from the image and populate the schema exactly as defined.

Rules:
1. Follow the schema structure exactly.
   - Do not add, remove, or modify fields.
   - Keep lists, objects, and nested structures exactly as defined.

2. Only extract what is visible in the image.
   - If a value is not visible, use null.
   - If the schema includes arrays, include one entry per visible item.

3. Never hallucinate missing information.
   - If unsure, select null.
   - Do not invent text, numbers, or categories.

4. Maintain consistent data types.
   - Strings remain strings.
   - Numbers remain numbers.
   - Booleans remain booleans.

5. Output ONLY valid JSON matching the schema.
   - No explanation, no extra fields, no comments.

Your response must be exactly the JSON object with the schema fields populated.

data schema
____________
{data_schema}
"""

CREATE_QUERY_TO_RESPOND_TO_USER = """
Your job is to create a query to get the data from a database that will be able to answer a user query.
The required format in which you need to give your query is specified in the response format.
Below you are provided with the user's query and the database schema that contains the data that can answer the query

user query:
___________
{user_query}

database schema:
________________
{schema}
"""