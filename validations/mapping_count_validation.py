from utils.query_executor import execute_scalar_query
from utils.file_reader import read_sql

def column_mapping(cursor):
    column_mapping_query=read_sql(r"C:\Users\avina\Documents\python course\21 automation mini project 2\sql files\mapping.sql")
    column_mapping_count=execute_scalar_query(cursor,column_mapping_query)
    return {
        "validation_name":"mapping_count",
        "actual_result":column_mapping_count,
        "expected_result":0,
        "status":"PASS" if column_mapping_count==0 else "FAIL"
    }