# accounts应用 #

## 模型建立 ##
> models.py中定义应用模型

- [重写用户模型](<'https://www.jianshu.com/p/b993f4feff83'>)


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

[Django-admin官方文档](<'https://docs.djangoproject.com/en/2.1/ref/contrib/admin/'>)

[Django内置admin字段介绍1](<'https://www.cnblogs.com/metianzing/p/7688546.html'>)

[Django内置admin字段介绍2](<'https://www.cnblogs.com/navysummer/p/10200247.html'>)


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


## 视图管理 ##    
- 登录视图

- 退出视图

- 注册视图

- 修改密码

- 重置密码

- 函数视图

- 模板视图

## 路由管理 ##
