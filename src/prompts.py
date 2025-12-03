CREATE_SCHEMA = """
Your job is to create a data schema to make the data in image searchable in a conversational manner.
Once you have created the schema you will need to answer questions by querying the schema you created so consider
the kinds of questions a user would want to ask when desiging your schema. The format you must design your 
schema accoridng to is specificed in the response format.
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