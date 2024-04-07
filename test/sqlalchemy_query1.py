from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy import inspect
from chipmunkdb.jdbc import *

engine = create_engine('chipmunkdb://localhost:8092')
with engine.connect() as conn:
    query = text("SELECT index_symbol AS index_symbol,\
                   sum(sma_volume) AS `SUM(sma_volume)`\
                    FROM `default`.`options_2023`\
                    GROUP BY index_symbol\
                    ORDER BY `SUM(sma_volume)` DESC\
                    LIMIT 1000")

    result = conn.execute(query)
    for row in result:
        print(row)