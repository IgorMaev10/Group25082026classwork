import psycopg2
import config

with psycopg2.connect(
    dbname=config.PGDATABASE,
    user=config.PGUSER,
    password=config.PGPASSWORD,
    host=config.PGHOST,
    port=5432,
) as connection:
    with connection.cursor() as cursor:
        sql_query_table_brand = """
        CREATE TABLE IF NOT EXISTS brand (
        id SERIAL PRIMARY KEY,
        name VARCHAR(75) NOT NULL UNIQUE 
        )
        """
        cursor.execute(sql_query_table_brand)
