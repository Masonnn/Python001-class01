# 学习笔记


## 变量赋值

#### 使用内存角度划分基本数据类型
**可变类型**
list 列表
dict 字典

**不可变类型**
int 整型
float 浮点型
string 字符串
tuple 元组


#### 是否序列
##### 序列
**容器序列**：
list、tuple、collections.deque等容器序列，能存放不同类型的数据。

**扁平序列**
str、bytes bytearray memoryview(内存视图)、array.array等，存放相同类型的数据，扁平序列只能容纳一种类型。
![0d6865034568063f5a94c1af7f08963b.png](evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p414)


##### 容器序列的深浅拷贝
深拷贝，拷贝所有值，需要重新申请相应内存。
浅拷贝，拷贝对象的引用



## 函数 -- 可调用对象

#### 调用
func
func()

#### 作用域 (命名空间)
##### LEGB原则
L - Local（function）
E - Enclosing function locals 外部嵌套函数的命名空间
G - Global（module）
B - Built-in(Python)
![e90459e8daa0806cee62248656a5ac37.png](evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p415)


#### 参数
位置参数
关键字参数
可变长参数`*args`

`**kargs`



#### 返回值

返回值关键字：return，yield


返回的对象
可调用对象--闭包（装饰器）

### 装饰器
#### 函数装饰器

![477df09c3048fe5646aaad6e7f439d67.png](evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p416)


![89f5f771279b4dc8e206c5c20379cf1c.png](evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p417)

被装饰函数带参数：
![ccf978c361a56d24d763776ffc951579.png](evernotecid://F481C5C1-AA36-4BAD-9D1F-5C9D27099F65/appyinxiangcom/7433901/ENResource/p418)

装饰器函数带参数：


装饰器堆叠：


#### 类装饰器

**使用类做装饰器**

**装饰器装饰类**