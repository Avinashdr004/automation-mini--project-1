from utils.query_executor import execute_scalar_query
from utils.file_reader import read_sql


def null_check(cursor):
    null_check_query=read_sql(r"C:\Users\avina\Documents\python course\21 automation mini project 2\sql files\null_count.sql")
    null_count=execute_scalar_query(cursor,null_check_query)
    return {
        "validation_name":"null_count",
        "actual_result":null_count,
        "expected_result":0,
        "status":"PASS" if null_count==0 else "FAIL"
    }