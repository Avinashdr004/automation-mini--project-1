from utils.db_connection import get_connection
from utils.print import print_formating
from validations.record_count_validation import record_count_f
from validations.duplicate_count_validation import duplicate_check
from validations.mapping_count_validation import column_mapping
from validations.null_count_validation import null_check
import pandas as pd

results=[]
conn=get_connection()
cursor=conn.cursor()

results.append(record_count_f(cursor))
results.append(duplicate_check(cursor))
results.append(null_check(cursor))
results.append(column_mapping(cursor))

for result in results:
    print_formating(result)

df=pd.DataFrame(results)
df.to_excel(r"C:\Users\avina\Documents\validation_Report2.xlsx",index=False)

cursor.close()
conn.close()

# added a comment to check changes added to the repo
