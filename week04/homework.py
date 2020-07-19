import pandas as pd
from sqlalchemy import create_engine

conn1 = create_engine(
    "mysql+pymysql://root:1qaz@WSX@localhost:3306/Scrapy_learn").connect()

# 1. SELECT * FROM data;
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
data = pd.read_sql_table("maoyanMovies", conn1)
data

# 2. SELECT * FROM data LIMIT 10;
data.head(10)
data.tail(10)
data[:10]
data[-10:]

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
data['id']

# 4. SELECT COUNT(id) FROM data;
data['id'].count()

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
data[(data["id"] < 1000) & (data["age"] > 30)]

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
data.groupby("id").aggregate({'order_id': 'count'})

# 7. SELECT * FROM table1 t1 INNER_JOIN table2 t2 ON t1.id = t2.id;
pd.merge(t1, t2, on='id', how='inner')

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
pd.merge(table1, table2)

# 9. DELETE FROM table1 WHERE id=10;
data[data["id"] != 10]

# 10. ALTER TABLE table1 DROP COLUMN column_name;
data.drop("column_name")
