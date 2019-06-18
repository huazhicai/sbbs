## Python 面试题

- 到底什么是Python？你可以在回答中与其他技术进行对比（也鼓励这样做）
    - Python是一种解释型语言。这就是说，与C语言和C的衍生语言不同，Python代码在运行之前不需要编译。其他解释型语言还包括PHP和Ruby。
    - Python是动态类型语言，指的是你在声明变量时，不需要说明变量的类型。你可以直接编写类似x=111和x="I'm a string"这样的代码，程序不会报错。
    - Python非常适合面向对象的编程（OOP），因为它支持通过组合（composition）与继承（inheritance）的方式定义类（class）。
    Python中没有访问说明符（access specifier，类似C++中的public和private），这么设计的依据是“大家都是成年人了”。
    - 在Python语言中，函数是第一类对象（first-class objects）。这指的是它们可以被指定给变量，函数既能返回函数类型，
    也可以接受函数作为输入。类（class）也是第一类对象。
    - Python代码编写快，但是运行速度比编译语言通常要慢。好在Python允许加入基于C语言编写的扩展，因此我们能够优化代码，
    消除瓶颈，这点通常是可以实现的。numpy就是一个很好地例子，它的运行速度真的非常快，因为很多算术运算其实并不是通过Python实现的。
    - Python用途非常广泛——网络应用，自动化，科学建模，大数据应用，等等。它也常被用作“胶水语言”，帮助其他语言和组件改善运行状况。
    - Python让困难的事情变得容易，因此程序员可以专注于算法和数据结构的设计，而不用处理底层的细节。

- **python中is和==的区别**
    - Python中对象包含的三个基本要素，分别是：id(身份标识) 、type(数据类型)和value(值)。  
    - '=='比较的是value值
    - 'is' 比较的是id
    
- **简述read、readline、readlines的区别**
    - read读取整个文件
    - readline 每次读取一行数据
    - readlines()一次读取所有内容并按行返回list 
    
- **Python自省**
    - 运行时能够获得对象的类型.比如type(),dir(),getattr(),hasattr(),isinstance().
          
- **字典推导式**      
    - d = {key: value for key, value in iterable}
    
- **Python中单下划线和双下划线**      
    - __foo__:一种约定,Python内部的名字,用来区别其他用户自定义的命名,以防冲突.
    - _foo:一种约定,用来指定变量私有.程序员用来指定私有变量的一种方式.
    
- **`*args and **kwargs`**
    - *args 可变参数：args接收的是一个tuple
    - **kw是关键字参数，kw接收的是一个dict。
    - 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
    - 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
          
- **装饰器**
    - 装饰器的作用就是为已经存在的对象添加额外的功能。
          
- **鸭子类型**      
    - “当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”
    - 我们并不关心对象是什么类型，到底是不是鸭子，只关心行为。
    - 比如在python中，有很多file-like的东西，比如StringIO,GzipFile,socket。它们有很多相同的方法，我们把它们当作文件使用。
    - 又比如list.extend()方法中,我们并不关心它的参数是不是list,只要它是可迭代的,所以它的参数可以是list/tuple/dict/字符串/生成器等.
    
- **__new__和__init__的区别**      
    - __new__是一个静态方法,而__init__是一个实例方法.
    - __new__方法会返回一个创建的实例,而__init__什么都不返回.
    - 只有在__new__返回一个cls的实例时后面的__init__才能被调用.
    - 当创建一个新实例时调用__new__,初始化一个实例时用__init__.

- **单例模式**
    - 这个绝对常考啊.绝对要记住1~2个方法,当时面试官是让手写的.
    ```
    class Singleton(object):
        def __new__(cls, *args, **kw):
            if not hasattr(cls, '_instance'):
                orig = super(Singleton, cls)
                cls._instance = orig.__new__(cls, *args, **kw)
            return cls._instance
 
    class MyClass(Singleton):
        a = 1
    ```  
    - 共享属性: 创建实例时把所有实例的__dict__指向同一个字典,这样它们具有相同的属性和方法.
    ```
    class Borg(object):
        _state = {}
        def __new__(cls, *args, **kw):
            ob = super(Borg, cls).__new__(cls, *args, **kw)
            ob.__dict__ = cls._state
            return ob
        
    class MyClass2(Borg):
        a = 1
    ```    
    - 装饰器版本
    ```
    def singleton(cls, *args, **kw):
        instances = {}
        def getinstance():
            if cls not in instances:
                instances[cls] = cls(*args, **kw)
            return instances[cls]
        return getinstance
     
    @singleton
    class MyClass:
      ...
    ```
    - import方法 : 作为python的模块是天然的单例模式
    ```
    # mysingleton.py
    class My_Singleton(object):
        def foo(self):
            pass
     
    my_singleton = My_Singleton()
     
    # to use
    from mysingleton import my_singleton
     
    my_singleton.foo() 
    ```
    
- **Python中的作用域**  
    - 在Python中，所有的名字都存在于一个空间中，它们在该空间中存在和被操作——这就是命名空间。
    它就好像一个盒子，每一个变量名字都对应装着一个对象。当查询变量的时候，会从该盒子里面寻找相应的对象。    
    - 本地作用域（Local）→当前作用域被嵌入的本地作用域（Enclosing locals）→全局/模块作用域（Global）→内置作用域（Built-in）
    
- **GIL线程全局锁**      
    - 线程全局锁(Global Interpreter Lock),即Python为了保证线程安全而采取的独立线程运行的限制,说白了就是一个核只能在同一时间运行一个线程.
    - 解决办法就是多进程和下面的协程(协程也只是单CPU,但是能减小切换代价提升性能).
    
- **闭包**      
    - 必须有一个内嵌函数
    - 内嵌函数必须引用外部函数中的变量
    - 外部函数的返回值必须是内嵌函数
    
- **lambda函数**      
    - lambda函数是匿名函数
    - 使用lambda函数能够创建小型匿名函数。这种函数得名于省略了用def声明函数的标准步骤
    - 如： lambda x, y: x+y
    
- **Python函数式编程**
    - 高阶函数: 变量可以指向函数-> 函数名也是变量:把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。      
    - map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
    - reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
    - filter()也接收一个函数和一个序列,传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
    - sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
    
- **什么是猴子补丁？**
    - 在运行期间动态修改一个类或模块。      
    
- **深拷贝和浅拷贝之间的区别是什么？**
    - 深拷贝就是将一个对象拷贝到另一个对象中 `b=copy.deepcopy(a)`
    - 这意味着如果你对一个对象的拷贝做出改变时，不会影响原对象
    - 浅拷贝则是将一个对象的引用拷贝到另一个对象上
    - 因此，改变拷贝对象会影响原来的对象
    
- **Python中的三元运算子**    
    - [on true] if [expression] else [on false]
    - min=a if a<b else b
    
- **解释一下Python中的继承**    
    - 当一个类继承自另一个类，它就被称为一个子类/派生类，继承自父类/基类/超类。它会继承/获取所有类成员（属性和方法）
    - 继承能让我们重新使用代码，也能更容易的创建和维护应用。Python支持如下种类的继承：
    - 单继承：一个类继承自单个基类
    - 多继承：一个类继承自多个基类
    - 分层继承：多个类继承自单个基类
    - 多级继承：一个类继承自单个基类，后者则继承自另一个基类
    
- **解释Python中的help()和dir()函数**    
    - help()函数是一个内置函数，用于查看函数或模块用途的详细说明
    - dir() 函数 返回对象方法属性列表
    
- **当退出Python时，是否释放全部内存？**    
    - 答案是No。循环引用其它对象或引用自全局命名空间的对象的模块，在Python退出时并非完全释放。
    
- **解释Python中的join()和split()函数**    
    - join()能让我们将指定字符添加至字符串中 `','.join('1234')`
    - split()能让我们用指定字符分割字符串。 `'1,2,3'.split(',')`
- **私有变量和私有方法**    
    - `_foo` 私有变量，只有类和子类可以访问这些变量，不可被导入其他模块
    - `__foo__` 系统变量名和方法
    - `__foo` 类中私有变量名和方法，只有类自己可以访问，子类都不可以访问
    
- **系统变量__name__**
    - 如果模块是被导入，`__name__`的值为模块的名字；
    - 如果模块是被直接执行，`__name__`的值为`__main__`    
- **python序列化**    
    - 把变量从内存中变成可存储或传输的过程称为序列化；
    - 序列化后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
    - 反过来，把变量内容从序列化的对象重新督导内存里称为反序列化
    - pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
    - 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
    - pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
    - json.dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object
    - 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，
    后者从file-like Object中读取字符串并反序列化
- **python标准库**    
    - os 提供与操作系统相关联的函数
    - sys 通常用于命令行参数
    - re 正则匹配
    - math 数学运算
    - datetime 处理日期和时间
    
- **谈下python的GIL**    
    - GIL 是python的全局解释器锁，同一进程中假如有多个线程运行，一个线程在运行python程序的时候会霸占python解释器（加了一把锁即GIL），
    使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程运行。
    所以在多线程中，线程的运行仍是有先后顺序的，并不是同时进行。
    - 多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个python解释器，
    所以多进程可以实现多个进程的同时运行，缺点是进程系统资源开销大

- **Python是如何进行内存管理的**
    - 对象的引用计数机制
        - python内部使用引用计数，来保持追踪内存中的对象，所有对象都有引用计数。
        - 引用计数增加：`一个对象分配一个新名称` `将对象放入一个容器中`
        - 引用计数减少： `使用del语句显示销毁对象别名` `引用超出作用域或者被重新赋值`
    - 垃圾回收机制
        - 当一个对象的引用计数归零时，它将被垃圾收集机制处理掉。
    - 内存池机制    
        - Python提供了对内存的垃圾收集机制，但是它将不用的内存放到内存池而不是返回给操作系统:
        - Pymalloc机制：为了加速Python的执行效率，Python引入了一个内存池机制，用于管理对小块内存的申请和释放。
        - 对于Python对象，如整数，浮点数和List，都有其独立的私有内存池，对象间不共享他们的内存池。也就是说
        如果你分配又释放了大量的整数，用于缓存这些整数的内存就不能再分配给浮点数。
- ****    
- ****    
- ****    
- ****    
- ****    
- ****    
          