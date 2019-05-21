# accounts应用 #

## 模型建立 ##
> models.py中定义应用模型

- [重写用户模型](<https://www.jianshu.com/p/b993f4feff83>)


- 自定义表名
    > Meta中`db_table`定义表名，默认为小写的`应用名+模型类名`.
    
    
- 应用配置
    > `apps.py`中定义用户配置器，在`__init__.py`中指定配置器`default_app_config = 'accounts.apps.AccountsConfig'`
    
    
- settings修改
    ```settings
        # 指定用户管理模型
        AUTH_USER_MODEL = 'accounts.UserProfile'
        
        # 指定用户认证方法
        # AUTHENTICATION_BACKENDS=[]
    ```


## 后台注册 ##
> 在admin.py中注册模型到管理后台

[Django-admin官方文档](<https://docs.djangoproject.com/en/2.1/ref/contrib/admin/>)

[Django内置admin字段介绍1](<https://www.cnblogs.com/metianzing/p/7688546.html>)

[Django内置admin字段介绍2](<https://www.cnblogs.com/navysummer/p/10200247.html>)


## 权限管理 ##
- is_superuser
    > 超级用户，拥有所有权限
- is_staff
    > 职员状态，是否可以访问后台
- is_active
    > 有效用户，账户是否可用    
- groups
    > 组，django创建表时给拥有多对多字段`auth.Group`的表自动创建对应的table_groups表.
- user_permissions
    > 权限，django创建表时给拥有多对多字段`auth.Permission`的表自动创建对应的table_user_permissions表.   
    
    > django创建表时自动在`auth_permissions`权限表中自动添加`add`,`delete`,`change`,`view`四个权限.

## 表单管理 ##
- 登录表单
- 注册表单
- 设置密码表单
- 修改密码表单
- 邮件表单

## 视图管理 ##    
- 登录视图
    - 内置登录
        > `from django.contrib.auth import login`
    - 下次自动登录
        > [session机制](<https://www.cnblogs.com/sss4/p/7071334.html>)
    - 验证码
        > 利用`PIL`和`random`制作含噪点的随机密码，前端使用`ajax`动态刷新
    - 用户名、手机、邮箱多途径登录   
        ```Q查询
            from django.db.models import Q
            from django.contrib.auth import get_user_model
            
            User = get_user_model()
            User.objects.filter(Q(username=username) | Q(email=username) | Q(phone=username))
        ```
        
        
- 退出视图
    - 内置退出方法
        - 在`LogoutView`中利用`next_page`设置退出后的跳转地址,
        - 或利用`settings.LOGOUT_REDIRECT_URL`指定跳转地址，但这个会影响所有的`LogoutView`视图.


- 注册视图
    - 利用form.ModelForm
    - 注册验证码邮件通知
        > 转发送邮件视图（邮箱未注册）
    - 注册成功邮件通知
        > 利用AbstractUser自带发送邮件功能
    
    
- 发送邮件视图
    - 邮箱已注册
        - 重设密码邮件（附重设密码链接）
            - 生成身份标识
                - uid
                    > 经base64编码的用户主键
                    ```uid
                        from django.utils.http import urlsafe_base64_encode
                        from django.utils.encoding import force_bytes
                        urlsafe_base64_encode(force_bytes(user.pk))
                    ```
                - token
                    > 经hashlib.sha1和hmac双重加密的用户信息
                    ```token
                        from django.contrib.auth.tokens import default_token_generator as token_generator
                        token_generator.make_token(user)
                    ```
            - 生成主域名
                - protocol
               
                    > https or http
                    
                    > [SECURE_PROXY_SSL_HEADER 配置](<http://program.dengshilong.org/2016/11/18/Django%E4%B9%8BSECURE-PROXY-SSL-HEADER%E8%AE%BE%E7%BD%AE/>)
                    
                    `protocol = 'https://' if self.request.is_secure() else 'http://'`
                - domain
                    > 如127.0.0.1:8000
                    ```domain
                        from django.contrib.sites.shortcuts import get_current_site
                        current_site.domain
                    ```
            - 完整的重设密码链接
                ```uri
                    视图中：
                    uri + resolve_url('accounts:reset', uidb64=uid, token=token)
                    模板中：
                    {{ protocol }}://{{ domain }}{% url 'reset' uidb64=uid token=token %}
                ```
                   
    - 邮箱未注册
        - 注册验证码邮件
            > `timeout`有效期
            ```验证码设置
                from django.core.cache import cache
                cache.set(key, value, timeout)
            ```


- 重设密码视图
    - 内置重置方法
    - 身份验证
        - uid base64解码获取账号
    - 链接有效性验证
        - 用户身份获取失败判断无效
        - token验证
            > 用户+时间戳生成的token如果和得到的token相同则有效
        - 时间验证
            > token解析出的时间戳如果超出`settings.PASSWORD_RESET_TIMEOUT_DAYS`则失效
        - 修改密码后删除token,使链接失效
            > `del self.request.session[INTERNAL_RESET_SESSION_TOKEN]`
    - 重设密码后自动登录
        > `post_reset_login=True`
     
                   
- 修改密码视图
    - 内置修改方法
    - 未登录跳转到登录页面
        ```PasswordChangeView
            @method_decorator(login_required)        
            def dispatch(self, *args, **kwargs):
        ```
    - 获取用户信息
        > `self.request.user`

    
- 个人信息
    - 我的资料
        - 信息展示
        - 头像展示
        - 头像修改
            - cropper头像裁剪插件
        - 资料修改
        - 个人主页
            


## 路由管理 ##
- 登录
- 退出
- 注册
- 重设密码
- 修改密码
- 邮件通知

- 个人中心
    - 我的资料
    - 我的收藏
    - 我的关注
    - 我的粉丝
    - 我的博客
    - 我的相册
    - 头像修改
    