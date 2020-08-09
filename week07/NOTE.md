# 学习笔记

## 类
#### 属性

类属性，只保存一份
对象属性，每个对象保存一份


**查看对象属性：**
`obj.__dict__ # 返回字典`
`dir(obj) # 返回列表`

**区分对象方法：**
`id(obj)`
`obj.__class__()`
不同内存地址，两个不同对象


属性作用域：
`_age = 0 # 单个_变量，人为约定不可修改`
`__fly = False # 双_变量，私有属性，不可修改，有自动改名机制`  
`__init__ # 前后各有双_，魔术方法，不会自动改名`


## 方法
三类方法
1、普通方法，也叫实例方法
* 参数中有self，只能被实例调用，不能用类直接调用
* 也是bound method

#### 语法糖: 例如 @classmethod
2、类方法（@classmethod, 类方法描述器），传入cls参数，代表当前类
* 类和实例都可以使用
* bound method 绑定方法
* 主要用作构造函数？？？

3、静态方法(@staticmethod, 静态方法描述器)
* 做转化或判断功能
* 可以由类直接调用
* 由于不传入self也不传入cls, 所以不能使用类属性和实例属性


初始化函数：` __init__()`
构造函数：`__new__() `



![9312b069432cddfd10ad56b20015c771.png](evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p409)
## 属性操作
**属性描述符**

在类中，**实例**获取属性操作，可使用以下两个函数：
`__getattribute__()`
`__getattr__()`

**异同：**
![67654dd56c2d82f676536402a430dfb5.png](evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p410)
相同：都可以对实例属性进行获取拦截
不同：
`__getattr__()` 适用于未定义的属性
`__getattribute__()` 对所欲属性的访问都会调用该方法



顺序 ： # 如果同时存在，执行顺序是 __getattribute__ > __getattr__ > __dict__
优先级

#### 属性描述符 （property()类）
**什么是描述器（descriptor）？实现特定协议的一组工具，类**
描述器协议，描述符


底层是 __get__(),__set__(),__delete__(),



## 继承

支持多继承 missing？？？

鸭子类型？？？？？？？？？？

Python2.2之前 **经典类**，之后 **新式类**，新式类都继承自object基类
![042f4adea1329bc74bc0bf38e64c813f.png](evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p411)

**type类，元类。object类，基类**

type元类由tpye自身创建，object类由自身创建
tpye类继承了object类

![69823e50d5bfc0f56c1beebfa2b8c07d.png](evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p412)



##### 钻石继承：
经典类：深度优先继承
新式类：广度优先继承

DAG 有向无环图
class.mor()

##### c3算法

## SOLID设计原则与设计模式

#### SOLID设计原则
* 单一责任原则：The Single Responsibility Principle
* 开放封闭原则：The Open Closed Principle。对扩展开放，对修改封闭
* 李氏替换原则：The Liskov Substitution Principle
* 依赖倒置原则：The Dependency Inversion Principle
* 接口分离原则：The Interface Segregation Principle
前三个可以指导Python编程

#### 单例模式
![98fce3f4087c96b2b53a2622e65f028e.png](evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p413)

```Python
# 装饰器实现单实例模式
def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton 
class MyClass:
    pass
```


#### 工厂模式

静态工厂

类工厂

## 元类 metaclass

* 元类是创建类的类，是类的模板
* 元类是用来控制如何创建类的，正如类是创建对象的模板一样。
* 元类的实例为类，正如类的实例为对象
* 创建元类的两种方法
> 1. class
> 2. type
 type(类名，父类的元组，包含属性的字典)
 
 mixin
 
 #### 抽象基类（abstract base class）
 最大特点是不能被实例化 

