# 留言板程序
 
 ### 环境
- 系统centos7
- python 3.7
- flask 1.0.2
- mysql 5.7
- pipenv 管理虚拟环境
    - pipenv install (为当前的项目创建虚拟环境)
    - pipenv shell (显示激活虚拟环境)
    
### Installation
```
$ git clone https://github.com/sayhello.git
$ cd sayhello
$ pepenv install --dev
$ pipenv shell
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```    
    
### Web程序开发流程
- 程序功能设计
    - 概述：SayHello是一个类似于留言板的程序，用来让用户发表问候。
    - 主页：主页是SayHello唯一的页面，页面包含创建留言的表单以及所有的问候消息。
    - 问候表单：包含姓名和问候消息两个字段。
    - 问候消息列表：问候消息列表的上方显示所有消息数量。
    - 错误页面：包含404错误页面和500错误页面。
- 前端页面开发
    - 根据功能规格书画页面草图
    - 根据草图做交互式原型图
    - 根据原型图开发前端页面
    - 常用的工具Axure RP
- 后端程序开发
    - 数据库建模
    - 创建表单类
    - 编写视图函数
    - 编写模板            
    
- 功能概述
    - sayhello 是一个类似于留言板的程序，用来让用户发表问候，对任何人任何事的问候。
    - 主要包括：主页，问候表单， 问候消息列表， 错误页面

- 哪些技术
    - 使用包组织代码
    - Bootstrap 简化页面编写，利用鋐快速渲染页面
    - Flask-Moment 本地化日期和时间
    - 使用Faker模块生成虚拟数据
    - Flask-DebugToolbar调试程序
- [在线Demo](http://seven.synvn.com)   
- Docker 部署    