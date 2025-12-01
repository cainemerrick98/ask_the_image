from pydantic import BaseModel, ConfigDict


class Columns(BaseModel):
    name: str
    type_: str
    is_pk: bool


class Table(BaseModel):
    name: str
    columns: list[Columns]


class Relationship(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "title": "Relationship",
            "description":"The case table is on the 1 side of a 1-n join. "/ 
                          "If the relationship is 1-1 the choice to case or fact table is irrelevant"
        }
    )
    case_table: str
    fact_table: str

    
class Schema(BaseModel):
    tables: list[Table]
    relationships: list[Relationship]


class Filter(BaseModel):
    columns: str


class Query(BaseModel):
    ...

