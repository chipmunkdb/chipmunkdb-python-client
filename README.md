
# chipmunkdb :chipmunk: python-client

Modify and save dataframes with timeseries or without to an ultra-fast ipc chipmunk database with olap features. (Powered by duckdb)

## Installation

pip install chipmunkdb-python-client

## Usage

````python 


import sys
sys.path.insert(0,'..')
import pandas as pd
import numpy as np

from chipmunkdb.ChipmunkDb import ChipmunkDb

db = ChipmunkDb("localhost")

#receive all collections
collections = db.collections()

# create a dataframe
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])

print(df)

## save your pandas
db.save_as_pandas(df, "mydf")

## get infos abotu your dataframe
collection = db.collection_info("mydf")

# read your dataframe again
df2 = db.collection_as_pandas("mydf")

print(df2)

# call any query on your data
d = db.query("SELECT * FROM mydf WHERE a=1 LIMIT 100")

print(d)

````

## Info
