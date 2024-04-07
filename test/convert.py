import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa

df = pd.read_parquet('fiveminutetestdata.parquet')


df.to_csv("fiveminutetestdata.csv")