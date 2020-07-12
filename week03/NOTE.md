学习笔记

### 1、 Scrapy并发参数优化原理

### 2、多进程
进程创建，仅支持Mac or Linux：
os.fork()

from multiprocessing import Process, Queue

进程池：
from multiprocessing.pool import Pool


### 3、多线程

调用方
阻塞： 得到调用结果之前，线程会被挂起
非阻塞： 不能立即得到结果，不会阻塞线程

被调用方
同步：得到结果之前，调用不会返回
异步：请求发出后，调用立即返回，没有返回结果，通过回调函数得到实际结果



import threading

普通锁：
threading.Lock()
可嵌套普通锁：
threading.Lock()



并发 & 并行


#### 队列
import queue

优先队列：
queue.PriorityQueue()

__Python3.2 中引入了 concurrent.futures 库，利用这个库可以非常方便的使用多线程、多进程__
from concurrent.futures import ThreadPoolExecutor

### 4、作业
各种参考、东拼西凑，改了又改
