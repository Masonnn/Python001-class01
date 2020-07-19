# 数据清洗与预处理学习笔记

## Pandas, pd

pandas两种基本数据类型：series、DataFrame

series, 相当于一列（或一行），自动加索引
DataFrame， 相当于多行或多列，自动加索引

数据预处理：缺失值、重复值

分组、聚合，类比SQL

输出和绘图：
.pkl性能更好
.xls兼容性好
import matplotlib.pyplot as plt






## jieba分词与提取关键词

NLP、语义分析。

stop_words.txt, 屏蔽关键词
jieba.analyse.set_stop_words(stop_words)


自定义字典: user_dict.txt
jieba.load_userdict(user_dict)


## SnowNLP情感倾向分析
