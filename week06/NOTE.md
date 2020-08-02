# Week 6 学习笔记

### Django 开发环境配置

##### 安装
1、 创建并激活虚拟环境后，通过以下命令安装：
`python -m pip install Django`


##### 创建项目
**django-admin命令行工具** 
在终端cd到想要放置代码的目录，执行以下命令：
`django-admin startproject mysite<projectname>` 
注：尽量避免使用django或test等可能产生冲突的名字。

###### 生成的目录和文件

* 管理项目的命令行工具 manage.py

##### 创建应用
`python manage.py startapp firstApp`


##### 启动应用
`python manage.py runserver ip:port`


##### Python的<u>模块</u>和<u>包</u>

##### urls调度器


##### Django URL变量 支持的5种数据类型
![b502e6280e40e3704679ef93c2931f0a.png](evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p405)



#### view视图快捷方式
**render**
**redirect**


#### 模型与数据库

* 每个模型都是一个Python类， 这些类继承 django.db.models.Model
* 模型类的每个属性都相当于一个数据库的字段
* Django提供了椅子自动挡生成访问数据库的API


![fb4a03db65be628a5953b2802466de5f.png](evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p406)
**对应SQL：**
![b419bdf30a9971e46afbfe3d6ffd61fc.png](evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p407)

**转换SQL命令：**
```
python manage.py makemigrations
python manage.py migrate
```

**从数据库反向到Django ORM**
```
python manage.py inspectdb > models.py

```


##### ORM API

`python manage.py shell`


#### 模板 models
**模板变量**
![b0cf3113c8f2db4112ef43ba09380e69.png](evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p408)


models管理器



#### 其它

enumerate函数