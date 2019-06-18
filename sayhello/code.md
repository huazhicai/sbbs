## Python 面试编程题

- **请写一个Python逻辑，计算一个文件中的大写字母数量**
    ```
    import os 
    
    def cal_upper_alpha(file):
        if os.path.exists(file):
            with open(file) as foo:
                count = 0
                for i in foo.read():
                    if i.isupper():
                        count += 1
                return count
        else:
            return 'file not exist!'
            
    print(cal_upper_alpha('seven.txt')                            
    ```

- **如何以就地操作方式打乱一个列表的元素？**
    ```
    import random
    # shuffle 洗牌
    random.shuffle(mylist)
    ```

- **替换掉目标字符串中**
    ```
    str1 = "北京市麦达技术数字有限公司"
    str2 = str1.replace("北京市","").replace("技术","").replace("有限","").replace("公司","")
    ```

- **打印文件夹中文件的路径以及包含文件夹中文件的路径**
    ```
    def print_directory_contents(sPath):
        import os 
        for sChild in os.listdir(sPath):
            sChildPath = os.path.join(sPath, sChild)
            if os.path.isdir(sChildPath):
                print_directory_contents(sChildPath)
            else:
                print(sChildPath) 
    ```

- **多进程**
    ```
    import os, time
    from multiprocessing import Pool
    
    def worker(arg):
        print("child process start>>> pid={} ".format(os.getpid())
        time.sleep(1)
        print("child process end>>> pid{}".format(os.getpid())
        
    def main():
        print("main process start>>> pid={}".format(os.getpid())
        ps = Pool(4)
        for i in range(10):
            # ps.apply(worker, args=(i,))   # 同步执行
            ps.apply_async(worker, args(i,))  # 异步执行
        
        # 关闭进程池，停止接受其他进程
        ps.close()
        # 阻塞进程
        ps.join()
        print("主进程终止")
        
    if __name__ == '__main__':
        main()        
    ```

- **发送邮件**
    ```
    import sys
    import time 
    import poplib 
    import smtplib
    # 邮件发送函数
    def send_mail():
        try:
            handler = smtplib.SMTP('smtp.136.com', 25)
            handler.login('huazhicai110@163.com', '110huazhicai')
            msg = 'Hello World!'
            handler.send_message()
  
    ```
- **发送邮件**
    ```
    
    ```
- **发送邮件**
    ```
    
    ```
- **发送邮件**
    ```
    
    ```
- **发送邮件**
    ```
    
    ```
- **发送邮件**
    ```
    
    ```
- **发送邮件**
    ```
    
    ```
- **发送邮件**
    ```
    
    ```
- **发送邮件**
    ```
    
    ```
- **发送邮件**
    ```
    
    ```
- **发送邮件**
    ```
    
    ```

