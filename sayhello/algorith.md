## Python 面试算法

- **发送电子邮件**
```
import sys
import time
import smtplib

def send_mail():
    try:
        hanlder = smtplib.SMTP('smtp.163.com', 25)
        hanlder.login('huazhicai110@163.com', 25)
        msg = 'hello world!'
        handler.sendmail(from_addr, to_addr, msg)
        handler.close()
        return "send successfully!"
    except:
        return "send  fail"

```
- **递归函数**
```
# 汉诺塔
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
```
- **函数生成器**
```
# 斐波那契
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b 
        a, b = b, a+b
        n += 1
    return 'done'
```
- **装饰器**
```
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper 
    return decorator
```
- **写个栈结构**
```
class Stack:
    def __init__(self):
        self.itmes = []
        
    def isEmpty(self):
        return self.items == []
        
    def push(self, item):
        self.itmes.append(item)
        
    def pop(self):
        return self.itmes.pop()
        
    def peek(self):
        return self.itmes[len(self.itmes)-1]
        
    def size(self):
        return len(self.items)        
```
- **写个队列**
```
clas Queue:
    def __init__(self):
        self.itmes = []
        
    def isEmpty(self):
        return self.itmes == []
        
    def enqueue(self):
        return items.insert(0, item)
        
    def dequeue(self):
        return self.itmes.pop()
        
    def size(self):
        return len(sel.itmes)       
```
- **写个hello world!**
``` 
from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
```
- **冒泡排序 BubbleSort**
``` 
def bubble_sort(arry):
    n = len(arry)
    for i in range(n):
        for j in range(1, n-i):
            if arry[j-1] > arry[j]:
                arry[j-1], arry[j] = arry[j], arry[j-1]
    return arry
```
- **选择排序selectionsort**
``` 
def select_sort(arry):
    n = len(arry)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arry[j] < arry[min]:
                min = j 
        arry[min], arry[i] = arry[i], arry[min]
    return arry
```
- **插入排序insertionSort**
``` 
def insert_sort(arry):
    n = len(arry)
    for i in range(1, n):
        if arry[i] < arry[i-1]:
            temp = arry[i]
            arry[i] = arry[i-1]
            index = i-1 
            for j in range(i-1, -1, -1):
                if arry[j] > temp:
                    arry[j+1] = arry[j]
                    index = j
                else:
                    break
            arry[index] = temp
    return arry
```
- **快速排序**
``` 
def quick_sort():

            
```
- ****
``` 

```
- ****
``` 

```
- ****
``` 

```
- ****
``` 

```
- ****
``` 

```
- ****
``` 

```
- ****
``` 

```
- ****
``` 

```
- ****
``` 

```
- ****
``` 

```
- ****
``` 

```
