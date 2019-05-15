# SCSDN开发文档 #

[TOC]
## 简介 ##
> 四川专业IT交流社区（SiChuan Software Developer Network）,

> 学习开发的仿CSDN的博客系统

## 开发环境 ##  
操作系统|IDLE|Python版本|Django版本|BootStrap版本|LayerUI版本               
:------:|:------:|:------:|:------:|:------:|:------:        
windows7|pycharm|3.7.3|2.2|4.0|2.4.5
  

## 系统框架 ##
- 用户管理（accounts）
        
- 文章管理（articles）
    
- 行为管理（blog）

- RestfulAPI


- 后台系统
    - 超管后台
    - 用户后台
    
 
    

## 模型管理 ##
- accounts
    - 基本资料
    - 详细资料
    
    
- articles
    - 分类
    - 栏目
    - 标签
    - 文章
    
    
- blog

## 视图管理 ## 
- accounts
    - 登录
    - 退出
    - 注册
    - 密码重设
    - 密码修改
    - 注销账号
    - 个人主页
    - 头像修改  
    
- articles

  
- blog
    - 主页展示
    - 条件页面展示
    

## 资料链接 ##
[力扣](<https://leetcode.com/>)

[力扣中国](<https://leetcode-cn.com/>)

[RFC6570-URI模板](<https://tools.ietf.org/html/rfc6570#page-3>)

[numpy中文教程](<https://www.runoob.com/numpy/numpy-tutorial.html>)

[matplotlib中文文档](<https://www.matplotlib.org.cn/>)

[django官方文档](<https://docs.djangoproject.com/en/2.2/>) 

[自学课堂](<https://code.ziqiangxuetang.com/django/django-tutorial.html>) 

[django-markdown](<https://blog.csdn.net/duke10/article/details/81033686>)

[xadmin官方文档](<https://sshwsfc.github.io/xadmin/>)

[xadmin学并思](<http://x.xuebingsi.com/>)

[xadmin下载地址](<https://github.com/sshwsfc/xadmin>)

[layui官方文档](<https://www.layui.com/>)

[bootstrap官方文档](<https://v2.bootcss.com/javascript.html#modals>)

[RestFramework官网](<https://www.django-rest-framework.org/>)

[RestfulApi设计指南](<http://www.ruanyifeng.com/blog/2014/05/restful_api.html>)

[Github的Api设计文档3](<https://developer.github.com/v3/>)

[Github的Api设计文档4](<https://developer.github.com/v3/>)

[SVG图像入门](<http://www.ruanyifeng.com/blog/2018/08/svg.html>)

[GraphQL](<http://graphql.cn/>)

[Sphinx使用手册](<https://zh-sphinx-doc.readthedocs.io/en/latest/markup/index.html>)


## 知识点 ##
- sphinx 自动生成项目文档
    - pip install sphinx
    - mkdir docs
    - cd docs
    - sphinx-quickstart
        > 生成sphinx工程目录
    - sphinx-autogen         
    - sphinx-apidoc 
    
        `usage: sphinx-apidoc [OPTIONS] -o <OUTPUT_PATH> <MODULE_PATH> [EXCLUDE_PATTERN, ...]`
        > 根据代码块注释生成rst文档
        > -o <OUTPUT_PATH> 指定rst输出目录
        > <MODULE_PATH> 项目或文件目录 
        > [EXCLUDE_PATTERN, ...] 包含的文档构成的列表
        
    - sphinx-build
        
        `usage: sphinx-build [OPTIONS] SOURCEDIR OUTPUTDIR [FILENAMES...]`
        > sphinx-build -b html source build
    - make.bat
        
        `make html`
        > sphinx-build 的封装.SOURCEDIR=source,OUTPUTDIR=build   


- 导出安装模块                                                   
    > pip freeze > requirements.txt                        
     
                                                           
- 导入安装模块                                                   
    > pip install -r requirements.txt   
    
           
## 项目进度 ##
- 2019/05/09
    - accounts应用
        - 注册后台管理
        - 登录视图
        - 注册视图
        - 忘记密码视图
        - 修改密码视图
        - 个人中心视图
            - 信息展示
                - 个人资料
                    - 头像
                    - 个人信息
                - 我的收藏
                - 我的关注
                - 我的粉丝
                - 我的博客                    
            - 信息修改
            - 头像修改
    - blog应用
        - 主页视图
        - 生成验证码视图        
            
  