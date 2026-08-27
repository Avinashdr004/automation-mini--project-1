from utils.file_reader import read_sql
from utils.query_executor import execute_query

def record_count_f(cursor):
    record_count_query=read_sql(r"C:\Users\avina\Documents\python course\21 automation mini project 2\sql files\record_count.sql")
    source_count,target_count=execute_query(cursor,record_count_query)
    return {
        "validation_name":"record_count",
        "actual_result":source_count,
        "expected_result":target_count,
        "status":"PASS" if source_count==target_count else "FAIL"
    }