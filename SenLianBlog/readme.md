# 项目管理 #
[TOC]
## 基本配置 ##
> `SenLianBlog\apps\settings.py`
> `SenLianBlog\apps\settings.py`
- 应用注册
> INSTALLED_APPS

- 中间件
> MIDDLEWARE

- 模板配置
> TEMPLATES

- 静态文件
- 媒体文件
- 邮件配置
- 缓存配置
- Redis配置
- 数据库引擎
> DATABASES

- 国际化
- 用户验证机制
> AUTH_PASSWORD_VALIDATORS
> AUTHENTICATION_BACKENDS

- 其他

## 路由配置 ##
> `SenLianBlog\apps\urls.py`

## WSGI ##
> `SenLianBlog\apps\wsgi.py`

## 小技巧 ##  
- 设置浏览器图标
   - 方法一、django设置icon路由
       ```icon
            from django.views.generic.base import RedirectView
            from django.contrib.staticfiles.views import serve 
            re_path(r'^favicon\.ico$', RedirectView.as_view(url=r'static/common/imgs/s-icon-16x16.ico')),
            path('favicon.ico', serve, {'path': 'common/imgs/s-icon-16x16.ico'}),           
        ```
           
   - 方法二、HTML模板中直接重定向 
        ```html-icon
            <link rel="shortcut icon" href="{% static 'common/imgs/s-icon-16x16.ico' %}">
        ```


- 媒体文件引用
    ```media
        1. settings.TEMPLATES的options列表中添加`'django.template.context_processors.media'`
        2. url配置路由：
            from django.conf import settings
            from django.conf.urls.static import static
            urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```
    
- [SVG](<http://www.ruanyifeng.com/blog/2018/08/svg.html>)    