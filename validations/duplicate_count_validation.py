from utils.query_executor import execute_scalar_query
from utils.file_reader import read_sql

def duplicate_check(cursor):
    duplicate_check_query=read_sql(r"C:\Users\avina\Documents\python course\21 automation mini project 2\sql files\duplicate_count.sql")
    duplicate_count=execute_scalar_query(cursor,duplicate_check_query)
    return {
        "validation_name":"duplicate_count",
        "actual_result":duplicate_count,
        "expected_result":0,
        "status":"PASS" if duplicate_count==0 else "FAIL"
    }
    