from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy import inspect
from chipmunkdb.jdbc import *

engine = create_engine('chipmunkdb://localhost')
with engine.connect() as conn:
    query = text("SELECT%20index_symbol%20AS%20index_symbol,%0A%20%20%20%20%20%20%20sum(sma_volume)%20AS%20sma_vol_sum%0AFROM%20%60default%60.%60options_2023%60%0AGROUP%20BY%20index_symbol%0AORDER%20BY%20sma_vol_sum%20DESC%0ALIMIT%2050")

    result = conn.execute(query)
    for row in result:
        print(row)