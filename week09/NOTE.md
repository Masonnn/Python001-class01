# 学习笔记

## manage.py

`python manage.py runserver 8080`

做了5件事：

1. 解析对应参数 （runserver，ip, port）
2. 加载runserver文件
3. 检查端口、ORM
4. 实例化WSGI server
5. 动态创建类


## URLconf
### partial() 偏函数

##### Python实现
```Python
def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*args, *fargs, **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc
```

partial() 会被“冻结了”一部分函数参数和/或关键字的部分函数应用所使用，从而得到一个具有简化签名的新对象。 例如，partial() 可用来创建一个行为类似于 int() 函数的可调用对象，其中 base 参数默认为二：
##### 官方demo，方便记忆
```Python
from functools import partial

basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int.'
basetwo('10010')
# 输出： 18
```

##### 注意事项
1、partial第一个参数必须是可调用对象
2、参数传递顺序是从左到右，但不能超过原函数参数个数
3、关键字参数会覆盖partial中定义好的参数


### include() 



## HttpRequest & HttpResponse(从请求到响应)

![815d954e4b5ee1defab7efc27cbb6bf6.png](evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p424)



## models

动态创建类：
```Python
    @classmethod
    def from_queryset(cls, queryset_class, class_name=None):
        if class_name is None:
            class_name = '%sFrom%s' % (cls.__name__, queryset_class.__name__)
        return type(class_name, (cls,), {
            '_queryset_class': queryset_class,
            **cls._get_queryset_methods(queryset_class),
        })

```


## template

1/ 如何找到html文件？




## 管理界面
创建超级用户
`python3 manage.py createsuperuser`


### 表单

#### csrf中间件
`'django.middleware.csrf.CsrfViewMiddleware',`
settings.py
post请求

#### auth功能
验证中间件 in settings
  `'django.contrib.auth.middleware.AuthenticationMiddleware',`

```python
python3 manage.py shell

from django.contrib.auth.models import User

user = User.objects.create_user('user_name', 'email', 'password')

user.save()
```


## 信号

``` python
# receiver
def my_callback1(sender, **kwargs):
    print("Request started!")
    
# connect
from django.core.signals import request_started

request_started.connect(my_callback1)

```
## 中间件



## Django生产环境部署

转换器：Nginx


**gunicorn**
安装： pip install gunicorn
在项目目录执行： gunicorn MyProjectName.wsgi
![b26e79b3ed9923193b9ee490f95c5458.png](evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p425)



## celery定时任务


![dd833268522356988f7b9a6ffc23288f.png](evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p426)
