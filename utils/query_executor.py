
def execute_query(cursor,query):
    cursor.execute(query)
    return cursor.fetchone()

def execute_scalar_query(cursor,query):
    cursor.execute(query)
    return cursor.fetchone()[0]