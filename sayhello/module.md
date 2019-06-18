## 模块操作

- **常用内建模块**
    - re 正则模块
    - subprocess 执行系统命令 
    - json
    - pickle 
    - shutil
    - pbd 调试模块 `python -m pdb myscript.py`
    - venv 创建虚拟环境 `python -m venv venv`
    - datetime
        - datetime是Python处理日期和时间的标准库
        - datetime.now() # 获取当前时间
        - datetime(2018, 10, 22, 12, 20) # 用指定日期时间创建datetime
        - datetime类型转换为timestamp只需要简单调用timestamp()方法
        - 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法
        - 把str转换为datetime。转换方法是通过datetime.strptime()实现; `%Y-%m-%d %H:%M:%S`
        - 转换为str，转换方法是通过strftime()实现
        - 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关
    - random
        - random.randint(12, 20) #生成的随机数n: 12 <= n <= 20
        - random.randrange(0, 101, 2) 随机选取0到100间的偶数
        - random.random() 随机生成[0, 1)的浮点数
        - random.choice('abcdefg&#%^*f') 随机字符
        - random.sample('abcdefghij',3)  选取三个字符        
    - collections 
        - collections是Python内建的一个集合模块，提供了许多有用的集合类。
        - deque 双向队列 append() pop()  appendleft() popleft()
        - Counter是一个简单的计数器, 字母作为键，出现几次作为值
    - hashlib 
        - Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
        - md5=hashlib.md5();  md5.update('seven'.encode('utf-8')); md5.hexdigest();
    - urllib
        - urllib提供了一系列用于操作URL的功能。
    - os 
        - os 模块中主要包含创建和管理进程或者文件系统内容(比如文件和目录)的函数
        - os.getcwd()  os.chdir() os.getenv() os.listdir()  os.walk() os.makedir()创建单层目录
        - os.makedirs() 创建多层目录  os.remove()  os.rmdir()  os.rename() 
    - os.path 模块
        - os.path.basename() 
        - os.path.dirname()
        - os.path.exists()
        - os.path.isdir()
        - os.path.isfile()
        - os.path.join()
        - os.path.split()
        - os.path.splitext() 获取路径的后缀
    - sys 模块
        - sys 模块提供了特定系统的配置和操作
        - sys.platform  sys.version  sys.args[]  
        - sys.path  sys.exit(n)
    - logging 模块 
    
- **常用第三方模块**
    - Pillow: Python平台事实上的图像处理标准库了
    - 在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块
    - pymysql 
    - pymongo
    - redis
    - selenium  - 自动化真正的浏览器
    - parammiko  
        - 可以实现远程的带密码登录，解决ssh远程登陆需要交互的问题
    - fabric 
        - fabric是基于Python实现的SSH命令行工具，简化了SSH的应用程序部署及系统管理任务，它提供了系统基础的操作组件，
        可以实现本地或远程shell命令，包括命令执行，文件上传，下载及完整执行日志输出等功能。
    - scrapy
    - BeautifulSoup 
    - pyquery 
    - scrapy-redis
    - requests 用于访问网络资源
    - 用chardet检测编码   
    - threading – Python标准库的线程运行。对于I/O密集型任务很有效。对于CPU绑定的任务没用，因为python GIL。
    - multiprocessing – 标准的Python库运行多进程。
    - celery – 基于分布式消息传递的异步任务队列/作业队列。            
            
        
        
                 
    
    