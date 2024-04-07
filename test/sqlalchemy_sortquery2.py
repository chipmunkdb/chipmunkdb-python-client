from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy import inspect
from chipmunkdb.jdbc import *

engine = create_engine('chipmunkdb://localhost')
with engine.connect() as conn:
    query = text("SELECT%20index_symbol%20AS%20index_symbol,%0A%20%20%20%20%20%20%20sum(sum_sma)%20AS%20%60SUM(sum_sma)%60%0AFROM%0A%20%20(SELECT%20index_symbol,%0A%20%20%20%20%20%20%20%20%20%20SUM(sma_volume)%20as%20sum_sma%0A%20%20%20FROM%20%60default%60.options_2023%0A%20%20%20GROUP%20BY%20options_2023.index_symbol%0A%20%20%20ORDER%20BY%20sum_sma%20DESC%0A%20%20%20LIMIT%2010)%20AS%20virtual_table%0AGROUP%20BY%20index_symbol%0AORDER%20BY%20%60SUM(sum_sma)%60%20DESC%0ALIMIT%201000")

    result = conn.execute(query)
    for row in result:
        print(row)