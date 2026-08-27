import snowflake.connector
from configuration.config import snowflake_config

def get_connection():
    return snowflake.connector.connect(
        user=snowflake_config["user"],
        password=snowflake_config["password"],
        account=snowflake_config["account"],
        warehouse=snowflake_config["warehouse"],
        database=snowflake_config["database"],
        schema=snowflake_config["schema"]
    )

# snowflake_config is a dictionary here we are getting values by using keys and assigning to the variable