# 仿CSDN博客开发文档 #
[TOC]
## 一、基本框架 ##
    1. 用户管理
        1.1 账号信息
            1.1.1 用户名    --user=models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
            1.1.2 密码      --User.password
            1.1.3 注册时间  --created=models.DateTimeField(default=timezone.now)
        1.2 基本资料
            1.2.1 姓名      --User.username
            1.2.2 年龄      --age=models.IntegerField()
            1.2.3 生日      --birth=models.DateField(blank=True, null=True)
            1.2.4 性别      --sex=models.CharField(max_length=200, choices=(('M','男'),('W','女')))
            1.2.5 头像      --photo=models.ImageField(blank=True, null=True)
        1.3 详细资料
            1.3.1 电话      --phone = models.CharField(max_length=200, blank=True, null=True)
            1.3.2 邮箱      --User.email
            1.3.3 职业      --profession = models.CharField(max_length=100, blank=True)
            1.3.3 公司      --company = models.CharField(max_length=100, blank=True)
            1.3.4 学校      --school = models.CharField(max_length=100, blank=True)
            1.3.5 简介      --aboutme = models.TextField(blank=True)
        1.4 其他
            1.4.1 博主积分
            1.4.2 博主等级
            1.4.3 博主排名
            1.4.4 访客总量
        1.5 用户行为
            1.5.1 关注
            1.5.2 粉丝
            1.5.3 收藏
            1.5.4 喜欢  
             
    2. 文章管理
        2.1 栏目管理
            2.1.1 所属用户  --user=models.ForeignKey(User, related_name='article_column', on_delete=models.CASCADE)
            2.1.2 栏目名称  --column = models.CharField(max_length=200)
            2.1.3 创建时间  --created = models.DateTimeField(auto_now=True)
            2.1.4 修改时间  --update = models.DateTimeField(auto_now=True)
        2.2 标签管理
            2.2.1 所属用户  --user=models.ForeignKey(User, related_name='article_tag', on_delete=models.CASCADE)
            2.2.2 标签名称  --tag = models.CharField(max_length=200)
            2.2.3 创建时间  --created = models.DateTimeField(auto_now=True)
            2.2.4 修改时间  --update = models.DateTimeField(auto_now=True)
        2.3 博客管理
            2.3.1 所属用户  --user=models.ForeignKey(User, related_name='article', on_delete=models.CASCADE)
            2.3.2 所属栏目  --column=models.ForeignKey(ArticleColumn, on_delete=models.DO_NOTHING, related_name='article_column')
            2.3.3 博客标签  --tags = models.ManyToManyField(ArticleTag, related_name='article_tags', blank=True)
            2.3.4 博客标题  --title = models.CharField(max_length=200)
            2.3.5 博客内容  --body = models.TextField()
            2.3.6 点赞数    -- Redis
            2.3.7 阅读量    -- Redis
            2.3.8 文章路由  --slug = models.SlugField(max_length=200)
            2.3.9 创建时间  --created = models.DateTimeField(auto_now=True)
            2.3.10 修改时间 --update = models.DateTimeField(auto_now=True)
        2.4 评论管理
            2.4.1 所属用户  --user=models.ForeignKey(User, related_name='article', on_delete=models.CASCADE)
            2.4.2 所属文章  --article=models.ForeignKey(ArticlePost, related_name='comments', on_delete=models.DO_NOTHING)
            2.4.3 评论内容  --body = models.TextField()
            2.4.4 创建时间  --created = models.DateTimeField(auto_now_add=True)
    

## 二、视图架构 ##
- 用户界面
    - 登录
    - 退出
    - 注册
    - 个人信息
        - 信息展示
        - 信息修改
        - 头像修改



- 超级用户后台
    - 用户管理
        - 添加
        - 编辑
        - 删除
    - 栏目管理
        - 添加
        - 编辑
        - 删除
    - 标签管理
        - 添加
        - 编辑
        - 删除
    - 文章管理
        - 添加
        - 编辑
        - 删除                
     
     
        
- 普通用户后台
    - 栏目管理
        - 栏目创建
        - 栏目列表展示
            - 栏目修改
            - 栏目删除
    - 标签管理
        - 标签创建
        - 标签列表展示
            - 标签修改
            - 标签删除
    - 文章管理   
        - 文章发布
        - 文章点赞
        - 文章列表展示
            - 文章修改
            - 文章删除
     
     
            
- 博客展示
    - 首页展示
        - 左侧
            - 首页
            - 关注
            - 粉丝
            - 收藏
            - 赞
        - 中间
            - 所有用户博客
                - 标题
                - 作者
                - 标签
                - 发布日期
                - 阅读量
                - 评论量
                - 博客摘要
            - 特定用户博客 
                - 标题
                - 作者
                - 标签
                - 发布日期
                - 阅读量
                - 评论量                
                - 博客摘要       
            - 特定标签博客    
                - 标题
                - 作者
                - 标签
                - 发布日期
                - 阅读量
                - 评论量                
                - 博客摘要 
            - 特定栏目博客   
                - 标题
                - 作者
                - 标签
                - 发布日期
                - 阅读量
                - 评论量                
                - 博客摘要                          
        - 右侧  
            - 特定作者信息
            - 热门榜单
            - 最新发布
            - 推荐栏 
            - 公告栏 
            - 广告栏 

    - 文章详情展示
        - 左侧
            - 作者信息
        - 中间
            - 文章信息
                - 文章标题
                - 发布时间量
                - 作者
                - 标签
                - 阅读量
                - 评论量
                - 点赞量
                - 所属栏目
            - 文章正文
        - 右侧
            - 相似推荐


## 三、开发流程 ##

- 开发环境  

    操作系统|IDLE|Python版本|Django版本
    :------:|:------:|:------:|:------:
    windows7|pycharm|3.6.3|2.1.7
    
    - Python虚拟环境设置  
        ```package
            pip install django
            # ImageField字段需要
            pip install Pillow
            # 标题转换为标准url
            pip install slugify
        ```

- 创建工程 \
    `django-admin startproject SenLianBlog`



- 基本配置
    - 应用注册
        - 新建`SenLianBlog\apps`文件夹
        - 在`settings.py`中添加`sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))`
        - 在`settings.py`的`INSTALLED_APPS`列表中添加已创建的应用
            ```INSTALLED_APPS
                INSTALLED_APPS = [
                    'django.contrib.admin',
                    'django.contrib.auth',
                    'django.contrib.contenttypes',
                    'django.contrib.sessions',
                    'django.contrib.messages',
                    'django.contrib.staticfiles',
                ]
            ```
            
    - 数据库
        - 在`settings.py`的`DATABASES`列表中添加应用的数据库
        
    - 缓存配置
        ```CACHES
            CACHES = {
                'default': {
                    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
                }
            }
        ``` 
           
    - Redis配置
        ```Redis
            REDIS_HOST = '127.0.0.1'
            REDIS_PORT = 6379
            REDIS_DB = 0
        ```   
                 
    - 中间件
        - 在`settings.py`的`MIDDLEWARE`列表中添加中间件
        
    - 模板文件
        - 在`settings.py`的`TEMPLATES`列表中添加模板路径   \
            ` 'DIRS': [os.path.join(BASE_DIR, 'templates')]`
            
        - `APP_DIRS`为`True`, 在各个app路径下templates路径搜索
        - `APP_DIRS`为`False`, 在`DIRS`字段设置路径搜索
    
    - 静态文件
        ```static
            STATIC_URL = '/static/'
            STATIC_ROOT = os.path.join(BASE_DIR, 'statics')
            STATICFILES_DIRS = [
                os.path.join(BASE_DIR, 'debug_statics'),
            ]
        ```   
         
    - 媒体文件
        ```media
            MEDIA_ROOT = os.path.join(BASE_DIR, 'medias')
            MEDIA_URL = '/media/'
        ```   
         
    - 语言、时区、国际化 
        ```Internationalization
            LANGUAGE_CODE = 'zh-hans'
            TIME_ZONE = 'Asia/Shanghai'
            USE_I18N = True
            USE_L10N = True
            USE_TZ = False
        ```
        
    - 邮件配置
        ```EMAIL
            EMAIL_HOST = "smtp.qq.com"
            EMAIL_PORT = 25
            EMAIL_USE_TLS = False
            EMAIL_HOST_USER = "from_now_on820@qq.com"
            EMAIL_HOST_PASSWORD = "pmfrgzmkuznabdif"
            DEFAULT_FROM_EMAIL = "from_now_on820@qq.com"
        ```
    
    
- 生成用户管理数据表 

    ```生成数据表
        # 生成ORM模型
        python manage.py makemigrations
        # 查看生成的ORM模型
        python manage.py showmigrations
        # 创建数据表
        python manage.py migrate
    ```



- 创建超级用户
    ```创建超级用户
        python manage.py createsuperuser
        user: senlian 
        password: 123qweasd    
    ```   


- 运行开发环境
    - 运行脚本 
        > `python manage.py runserver`
            
    - 结果显示
        ```console
        Performing system checks...
        
        System check identified no issues (0 silenced).
        March 27, 2019 - 15:35:32
        Django version 2.1.7, using settings 'SenLianBlog.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.
        [27/Mar/2019 15:35:40] "GET /admin/ HTTP/1.1" 302 0
        [27/Mar/2019 15:35:40] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 1819
        [27/Mar/2019 15:35:41] "GET /static/admin/css/base.css HTTP/1.1" 200 16225
        [27/Mar/2019 15:35:41] "GET /static/admin/css/login.css HTTP/1.1" 200 1203
        [27/Mar/2019 15:35:41] "GET /static/admin/css/responsive.css HTTP/1.1" 200 17976
        [27/Mar/2019 15:35:41] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
        Not Found: /favicon.ico
        [27/Mar/2019 15:35:41] "GET /favicon.ico HTTP/1.1" 404 1977
        [27/Mar/2019 15:35:41] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 80304
        [27/Mar/2019 15:35:41] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 81348
        [27/Mar/2019 15:35:48] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
        [27/Mar/2019 15:35:48] "GET /admin/ HTTP/1.1" 200 3044
        [27/Mar/2019 15:35:48] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 412
        [27/Mar/2019 15:35:48] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
        [27/Mar/2019 15:35:48] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380
        [27/Mar/2019 15:35:48] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 82564
        Performing system checks...
        
        System check identified no issues (0 silenced).
        March 27, 2019 - 15:38:17
        Django version 2.1.7, using settings 'SenLianBlog.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.
        ```
    
    - 浏览
        > [http://127.0.0.1:8000/](<http://127.0.0.1:8000/>)
        

- account应用
    - 创建应用  
        > `python manage.py startapp account`
    - 应用激活
        > 在`settings.py`的`INSTALLED_APPS`列表中添加`account`
    - 模型建立
        > models.py中创建模型类
        ```account.models.py
            from django.db import models
            from django.contrib.auth.models import User
            from django.utils import timezone
            
            
            # Create your models here.
            
            class AccountUserProfileModel(models.Model):
                SEXES = (
                    ('male', '男'),
                    ('female', '女')
                )
            
                user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, verbose_name='账户')
                age = models.IntegerField(blank=True, null=True, verbose_name='年龄')
                birth = models.DateField(blank=True, null=True, verbose_name='生日')
                sex = models.CharField(max_length=2, choices=SEXES, default='male', verbose_name='性别')
                # 上传到MEDIA_ROOT路径下的photos/%Y/%m/%d文件夹
                photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
                created = models.DateTimeField(auto_now_add=timezone.now(), verbose_name='注册日期')
            
                class Meta:
                    verbose_name = '基本资料'
                    verbose_name_plural = verbose_name
                    ordering = ['-created']
            
                def __str__(self):
                    return 'UserName:{0}'.format(self.user.username)
            
            
            class AccountUserDetailModel(models.Model):
                user = models.OneToOneField('AccountUserProfileModel', unique=True, on_delete=models.CASCADE, verbose_name='账户')
                phone = models.CharField(max_length=200, blank=True, null=True, verbose_name='电话')
                profession = models.CharField(max_length=200, blank=True, null=True, verbose_name='电话')
                company = models.CharField(max_length=200, blank=True, null=True, verbose_name='公司')
                school = models.CharField(max_length=200, blank=True, null=True, verbose_name='学校')
                intro = models.TextField(blank=True, null=True, verbose_name='个人简介')
            
                class Meta:
                    verbose_name = '基本资料'
                    verbose_name_plural = verbose_name
            
                def __str__(self):
                    return 'UserName:{0}'.format(self.user.username)
            
        ```
    - 创建数据表
        > `python manage.py migrations `
        ```migrations
            Migrations for 'account':
              apps\account\migrations\0001_initial.py
                - Create model AccountUserDetailModel
                - Create model AccountUserProfileModel
                - Add field user to accountuserdetailmodel
        ``` 
        > `python manage.py migrate`
        ```migrate
            Operations to perform:
              Apply all migrations: account, admin, auth, contenttypes, sessions
            Running migrations:
              Applying account.0001_initial... OK
        ```
        
    - 后台注册
        > admin.py中注册管理模型
        ```admin
            from django.contrib import admin
            from .models import AccountUserProfileModel, AccountUserDetailModel
            
            # Register your models here.
            @admin.register(AccountUserProfileModel)
            class AccountUserProfileModelAdmin(admin.ModelAdmin):
                list_display = ['id', 'user_id', 'age', 'birth', 'sex', 'photo', 'created']
                list_display_links = ['age', 'birth', 'sex']
            
            
            @admin.register(AccountUserDetailModel)
            class AccountUserDetailModelAdmin(admin.ModelAdmin):
                list_display = ['id', 'user_id', 'phone', 'profession', 'company', 'school', 'intro']
                list_display_links = ['phone', 'profession', 'company', 'school', 'intro']

        ```

    - 表单模块
        - 登陆表单
                
    - 应用视图
        - 登录视图
        - 注册视图
        - 退出视图
        - 忘记密码
            - 邮件找回
        - 修改密码
        
- blog应用
    - 创建应用  
        > `python manage.py startapp blog`    
    - 应用激活
        > 在`settings.py`的`INSTALLED_APPS`列表中添加`blog`
    - 模型创建
    - 后台注册
    - 应用视图
    
## 小技巧 ##
- 设置浏览器图标
   - django设置icon路由
       ```icon
            from django.views.generic.base import RedirectView
            from django.contrib.staticfiles.views import serve 
            re_path(r'^favicon\.ico$', RedirectView.as_view(url=r'static/common/imgs/s-icon-16x16.ico')),
            path('favicon.ico', serve, {'path': 'common/imgs/s-icon-16x16.ico'}),           
        ```
    
   - HTML模板中直接重定向
    ```html-icon
        <link rel="shortcut icon" href="{% static 'common/imgs/s-icon-16x16.ico' %}">
    ```