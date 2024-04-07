from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy import inspect
from chipmunkdb.jdbc import *

engine = create_engine('chipmunkdb://localhost')
with engine.connect() as conn:
    inspector = inspect(engine)
    schemas = inspector.get_schema_names()
    print(schemas)

    tables = inspector.get_table_names(schema='default')
    print(tables)

    for table_name in tables:
        print("Table: %s" % table_name)
        columns = inspector.get_columns(table_name, schema='default')
        for column in columns:
            print("Column: %s" % column['name'])
            print("Type: %s" % column['type'])
            print("Nullable: %s" % column['nullable'])
            print("Default: %s" % column['default'])
            print("")
