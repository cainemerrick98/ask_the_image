from pydantic import BaseModel, ConfigDict, Field
from enum import Enum
from typing import Optional

# TODO Dates and times need to also be added here
class DataTypes(Enum):
    FLOAT = 'float'
    INTEGER = 'integer'
    STRING = 'string'


class Column(BaseModel):
    name: str
    data_type: DataTypes


class Table(BaseModel):
    name: str
    columns: list[Column]


class Relationship(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "title": "Relationship",
            "description":"The case table is on the 1 side of a 1-n join. "
                          "If the relationship is 1-1 the choice to case or fact table is irrelevant"
        }
    )
    case_table: str
    fact_table: str

    
class Schema(BaseModel):
    tables: list[Table]
    relationships: Optional[list[Relationship]] = Field(default_factory=list)


class Operator(Enum):
    LESS_THAN = '<'
    GREATER_THAN = '>'
    EQUAL = '=='
    NOT_EQUAL = '!='
    IN = 'IN'
    NOT_IN = 'NOT IN'
    IS_NULL = 'IS NULL'
    IS_NOT_NULL = 'IS NOT NULL'


class Filter(BaseModel):
    column: str
    operator: Operator
    value: int | str | float | None


class Query(BaseModel):
    table_name: str
    columns : list[str]
    filters : Optional[list[Filter]] 

