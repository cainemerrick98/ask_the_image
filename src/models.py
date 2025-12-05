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
    EQUAL = '='
    NOT_EQUAL = '!='
    IN = 'IN'
    NOT_IN = 'NOT IN'
    IS_NULL = 'IS NULL'
    IS_NOT_NULL = 'IS NOT NULL'


class Sorting(Enum):
    ASC = 'ASC'
    DESC = 'DESC'


class Aggregation(Enum):
    SUM = 'SUM'
    MAX = 'MAX'
    MIN = 'MIN'

class Filter(BaseModel):
    column: str
    operator: Operator
    value: int | str | float | None #TODO Handle value is query

    def to_string(self):
        if self.value is not None:
            if isinstance(self.value, str):
                return f"{self.column} {self.operator.value} \"{self.value}\""    
            return f"{self.column} {self.operator.value} {self.value}"
        else:
            return f"{self.column} {self.operator.value}"

class OrderBy(BaseModel):
    column: str
    sorting: Sorting

    def to_string(self):
        return f"{self.column} {self.sorting.value}"


class GroupBy(BaseModel):
    column: str

    def to_string(self):
        return self.column


class QueryColumn(BaseModel):
    name: str
    aggregation: Optional[Aggregation] = None

    def to_string(self):
        if self.aggregation:
            return f"{self.aggregation.value}({self.name})"
        return self.name



#TODO: how to specify that filters can be joined with and/or?
# At the moment lets just handle with AND
#TODO: how do we handle columns which are a combination of two others 
# e.g. subtraction or concatentation
#TODO: add joins
class Query(BaseModel):
    table_name: str
    columns: list[QueryColumn]
    filters: Optional[list[Filter]] = None
    groupby: Optional[list[GroupBy]] = None
    orderby: Optional[list[OrderBy]] = None

    def to_string(self):
        query_string = f"""
        SELECT {','.join([col.to_string() for col in self.columns])}
        FROM {self.table_name}
        """
        if self.filters:
            query_string += f"WHERE {' AND '.join([f.to_string() for f in self.filters])}\n"
        if self.groupby:
            query_string += f"GROUP BY {','.join([g.to_string() for g in self.groupby])}\n"
        if self.orderby:
            query_string += f"ORDER BY {','.join([o.to_string() for o in self.orderby])}\n"

        return query_string
