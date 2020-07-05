# 学习笔记

## 本周收获和问题
1、
根据老师对作业反馈，修改了部分作业。
在pipeline中将**数据获取**和**数据存储**功能分离暂时还不会改，明天问一下助教老师。
自己闷头死磕效率低下，容易放弃。不可取。

2、
本周作业1改来该去，勉强完成。
自己都觉得还有很多需要优化的地方，但是感觉有心无力，不知道怎么下手。

3、
自己基础太差。知识也有点零散，学着有点晕。需要多学几遍，熟能生巧。


## 部分视频笔记
### 异常捕获与处理

1、Traceback对象，调用过程、错误类型
   所有异常都继承自BaseException，
    错误log从下往上看
 
 自己定义异常继承Exception

```python
try:
    1/0
except Exception as e: # 捕获所有异常
    print(e)
    
```

魔术方法 -- 双下划线包围？ 类当函数，类当字符串？？？？

### PyMySql

### 反爬虫

##### 模拟浏览器头部信息
##### cookies验证
##### 使用WebDriver模拟浏览器识别
* selenium安装和使用
* 大文件下载
##### 验证码识别


#### 爬虫中间件 & 系统代理IP
下载中间件，优先级，数字越小优先级越高

* `scrapy crawl httpbin --nolog`

* 如何重写下载中间件？

evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p380



### 分布式爬虫

evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p381







