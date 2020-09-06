import pandas as pd
from sqlalchemy import create_engine
import numpy as np
from snownlp import SnowNLP


def datahanding():
    connect = create_engine(
        "mysql+pymysql://root:1qaz@WSX@localhost:3306/nms").connect()

    phones = pd.read_sql("Select * from phones", connect)
    phones.replace('', np.nan, inplace=True)
    # print(phones.isnull().sum())

    # 数据预处理
    # 评论去空去重
    phones_handled = phones.dropna().drop_duplicates(subset="comments", keep="first")
    phones_handled.reset_index()

    # 评论倾向性分析
    phones_handled['sentiments'] = phones_handled['comments'].map(lambda x: SnowNLP(x).sentiments)

    # 存储已处理的数据
    phones_handled.to_sql(name='phones_handled', con=connect, if_exists='replace', index=False)
    with connect as con:
        con.execute("ALTER TABLE `phones_handled` ADD PRIMARY KEY (`id`);".format(phones_handled))
        con.execute("alter table `phones_handled` change id id int not null auto_increment;".format(phones_handled))
    # print("ending")


if __name__ == '__main__':
    datahanding()
