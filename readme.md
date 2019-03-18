# [Django 学习笔记](<https://docs.djangoproject.com/en/2.1/#index-first-steps>，"官方文档") #
=============================================================================================

## Django简介##

>[官网：https://www.djangoproject.com](<https://www.djangoproject.com>) \
>[官方文档：https://docs.djangoproject.com](<https://docs.djangoproject.com>)

## Django安装 ##

> - 安装环境：python3.6.3 \
> - Django版本：2.1.7
>   - pip安装：`pip install django` \
>   - 源码安装：\
>    [github地址：https://github.com/django/django/releases](<https://github.com/django/django/releases>) \
>    下载完成后到解压目录执行： `python setup install` \
>   - 获取Django版本号：进入python运行环境，执行以下代码：\
>   ```
>   import django 
>   django.get_version()
>   ```

## [Django任务命令行工具](<https://docs.djangoproject.com/en/2.1/ref/django-admin/>) ##
- [django-admin](<https://docs.djangoproject.com/en/2.1/ref/django-admin/>)
    > ```
    > Type 'django-admin help <subcommand>' for help on a specific subcommand.
    > 
    > Available subcommands:
    >     
    >     [django]
    >         check
    >         compilemessages
    >         createcachetable
    >         dbshell
    >         diffsettings
    >         dumpdata
    >         flush
    >         inspectdb
    >         loaddata
    >         makemessages
    >         makemigrations
    >         migrate
    >         runserver
    >         sendtestemail
    >         shell
    >         showmigrations
    >         sqlflush
    >         sqlmigrate
    >         sqlsequencereset
    >         squashmigrations
    >         startapp
    >         startproject
    >         test
    >         testserver
    >     Note that only Django core commands are listed as settings are not properly configured (error: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.).
    > ```


- [manager.py](<https://docs.djangoproject.com/en/2.1/ref/django-admin/>)
    > manager.py是对django-amin的简单封装。
    > ```
    > Type 'manage.py help <subcommand>' for help on a specific subcommand.
    > 
    > Available subcommands:
    > 
    > [auth]
    >     changepassword
    >     createsuperuser
    > 
    > [contenttypes]
    >     remove_stale_contenttypes
    > 
    > [django]
    >     check
    >     compilemessages
    >     createcachetable
    >     dbshell
    >     diffsettings
    >     dumpdata
    >     flush
    >     inspectdb
    >     loaddata
    >     makemessages
    >     makemigrations
    >     migrate
    >     sendtestemail
    >     shell
    >     showmigrations
    >     sqlflush
    >     sqlmigrate
    >     sqlsequencereset
    >     squashmigrations
    >     startapp
    >     startproject
    >     test
    >     testserver
    > 
    > [sessions]
    >     clearsessions
    > 
    > [staticfiles]
    >     collectstatic
    >     findstatic
    >     runserver
    > ```

## Django项目创建 ##
- 方法一：
    > 工作目录执行：`django-admin startproject mysite`  \
      mysite为项目名称,可任意命名

    - 目录结构1：
    > 工作目录：
    >> mysite: 根目录
    >>> manage.py \
    mysite:  
    >>>> \_\_init\_\_.py \
        settings.py \
        urls.py \
        wsgi.py


- 方法二：
    > 工作目录执行：`django-admin startproject mysite .` \
      区别在于方法一在项目外层会创建mysite命名的根目录。
    
    - 目录结构2：
    > 工作目录：
    >> manage.py \
       mysite:  
    >>> \_\_init\_\_.py \
       settings.py \
       urls.py \
       wsgi.py
 
         
-  结果测试：
    > 根目录执行： python manager.py runserver \
     根目录下生成项目数据库文件`db.sqlite3` \
     结果如下则表示成功：       
    ```
    Performing system checks...
    
    System check identified no issues (0 silenced).
    
    You have 15 unapplied migration(s). Your project may not work properly until you
     apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    February 28, 2019 - 11:12:52
    Django version 2.1.7, using settings 'mysite.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    ```
                                     

## 创建应用 ##
> Django中具体的功能称为'应用'。 
- 方法一:
    > 工作目录中执行`python manager.py startapp blog`创建名为`blog`的应用。


- 方法二:
    > 工作目录中执行`django-admin startapp blog`创建名为`blog`的应用。
    

- 目录结构: 

    > 工作目录：
    >> mysite:  *__根目录__*
    >>> blog：   *__blog应用目录__*
    >>>> migrations: *__blog应用数据库表结构__*
    >>>>> \_\_init\_\_.py 
    >>>>
    >>>> \_\_init\_\_.py \
         admin.py   *__注册数据模型，自定义后台管理功能等__*\
         apps.py    *__blog应用配置,比如应用后台命名等__*\
         models.py  *__blog应用数据模型__*\
         tests.py   *__编写测试文档来测试所建立的应用__*\
         views.py   *__定义函数视图或类视图。__*
    >>>
    >>> mysite:     *__mysite项目目录__*
    >>>> \_\_init\_\_.py \
        settings.py     *__mysite项目初始化设置（包括数据库，应用添加、中间件等）__*\
        urls.py     *__mysite项目路由配置（视图函数或应用的url.py文件的映射关系）__*\
        wsgi.py     [*__Web Server Gateway Interface__*](<http://wsgi.readthedocs.io/en/latest/index.html>)
    >>>    
    >>> manage.py   *__项目任务命令工具__*\
        db.sqlite3  *__默认数据库文件，名称可以在settings.py文件中定义__*     
    

## settings.py模块##
    > 项目配置，如果不配置相关字段默认值在 django/conf/global_settings.py
    > `python manage.py diffsettings` 可以查看与默认配置的差异
    
- BASE_DIR
    > 项目根目录


- SECRET_KEY
    > 用于安全加密、签名等，不能为空。 \
    > 创建项目时生成，生成方式如下：\
    > ```
    > from django.core.management import utils  
    > utils.get_random_secret_key()  
    > ```
   
    
- DEBUG  
    > 标记`开发模式`或`生产环境`，值True|False。


- ALLOWED_HOSTS
    > 允许访问的域名，DEBUG为True时可以为空。
    

- INSTALLED_APPS
    > 应用注册，创建的应用配置到这里才能使用


- [MIDDLEWARE](<https://docs.djangoproject.com/en/2.1/ref/middleware/>)
    > [中间件](<https://blog.csdn.net/bbwangj/article/details/79993437>) \
    django请求/响应处理的钩子框架，这是一个轻量级的插件系统，\
    用于在全球范围内改变django的输入或输出。\
    django的中间件在settings的MIDDLEWARE列表中配置激活，\
    中间件有严格的依赖顺序，按列表顺序自上而下的执行。
    
    - [中间件方法](<https://blog.csdn.net/shentong1/article/details/78829599>)：
        > [中间件是一个python类。](<https://blog.csdn.net/yinhangxitong36/article/details/79785504>)
        
        在请求阶段依次执行：
        - process_request()   
        - process_view()  
           
        在响应阶段依次执行：
        - process_exception()  
        - process_template_response() 
        - process_response()  
        
        
- ROOT_URLCONF
    > 在settings.py文件中通过ROOT_URLCONF指定根级url的配置。    

 
-  [TEMPLATES](<https://www.cnblogs.com/gregoryli/p/7699352.html>)
    > `'APP_DIRS': True`, 按照app路径下templates路径搜索，\
     `'APP_DIRS': False`, 按照`DIRS`字段设置路径搜索，\
      扩展：[Django如何采用jinja2的模板引擎](<https://www.cnblogs.com/wasayezi/p/8693843.html>)


- [WSGI_APPLICATION](<https://www.cnblogs.com/JanKin-Cui/p/7173541.html>)
    > Django不是完整的web后端框架，它需要和一个WSGI服务器配套，\
    由WSGI服务器负责网络通讯部分, django依赖wsgi接口创建socket方法。\
    该项指向 __mystie__ 项目目录下wsgi.py的application方法。
    

- [DATABASES](<https://docs.djangoproject.com/en/2.1/ref/databases/>)
    > 此项配置数据库引擎 \
    [django多数据库联用配置方式](<https://blog.csdn.net/songfreeman/article/details/70229839>)
    

- [AUTH_PASSWORD_VALIDATORS](<https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators>)
    > 配置密码强度验证方式    


- LANGUAGE_CODE  
    > 语言设置  \
      英语：'en-us'  \
      中文简体：'zh-hans'


- TIME_ZONE
    > 时区设置 \
      世界时间：'UTC' \
      中国时间：'Asia/Shanghai'
      
      
- [USE_I18N](<https://code.ziqiangxuetang.com/django/django-internationalization.html>)  
    > Internationalization, I18N表示I与N之间有18个字母。
    > Django是否开启国际化支持
   
      
- USE_L10N 
    > localization, L10N表示L与N之间有10个字母。
    > Django本地化支持   
    
    
- [USE_TZ](<https://www.cnblogs.com/yanxiatingyu/p/9599676.html>)
    > 跨时区操作，时间强制转换成UTC时间
    > 国内服务可以设置为False
   
   
- [STATIC_URL](<https://blog.csdn.net/geerniya/article/details/78958243>)
    > 静态文件路由
    
    
- STATICFILES_DIRS
    > 开发模式静态文件存放路径
    
- STATIC_ROOT
    > 部署模式静态文件存放路径


- MEDIA_URL
    > 上传文件路由
    

- [MEDIA_ROOT](<https://blog.csdn.net/geerniya/article/details/78958243>)
    > 用户上传目录
    
    
    

## models.py模块 ##    
> 导入Django数据模块 `from django.db import models`
- 字段介绍
    - Field
    - AutoField
    - BigAutoField
    - BigIntegerField
    - BinaryField
    - BooleanField
    - CharField
    - CommaSeparatedIntegerField
    - DateField
    - DateTimeField
    - DecimalField
    - DurationField
    - EmailField
    - FileField
    - FilePathField
    - FloatField
    - GenericIPAddressField
    - IPAddressField
    - ImageField
    - IntegerField
    - ManyToManyField
    - NullBooleanField
    - OneToOneField
    - PositiveIntegerField
    - PositiveSmallIntegerField
    - SlugField
    - SmallIntegerField
    - TextField
    - TimeField
    - URLField
    - UUIDField       

## 建立数据模型 ##    
- 生成ORM模型
    > `python manage.py makemigrations` \
       *__0001\_initial.py__* 脚本中可以查看生成的ORM模型 \
       下面语句可以查看生成的sql语句: \
      `python manage.py sqlmigrate blog 0001` 


- 建立数据表      
    `python manage.py migrate`


- 创建超级用户
    `python manage.py createsuperuser`


- admin 注册数据模型
    > 在 *__admin.py__* 中注册数据模型 
    ```
    from .models import BlogArticles
    # 旧版本中可以采用 admin.site.register(BlogArticles) 的方式注册
    @admin.register(BlogArticles)
    class BlogArticlesAdmin(admin.ModelAdmin):
        pass
    ```
    
    - admin.ModelAdmin字段介绍
        - list_display = ('__str__',)
        - list_display_links = ()
        - list_filter = ()
        - list_select_related = False
        - list_per_page = 100
        - list_max_show_all = 200
        - list_editable = ()
        - search_fields = ()
        - date_hierarchy = None
        - save_as = False
        - save_as_continue = True
        - save_on_top = False
        - paginator = Paginator
        - preserve_filters = True
        - inlines = []
        
        
## 安装模块 ##
- pip install awesome-slugify
- pip install Pillow      