# 用户管理 #

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
           1.4 用户行为                                                                                                     
               1.4.1 关注                                                                                                 
               1.4.2 粉丝                                                                                                 
               1.4.3 收藏                                                                                                 
               1.4.4 喜欢 
           1.5 其他                                                                                                       
               1.5.1 博主积分                                                                                               
               1.5.2 博主等级                                                                                               
               1.5.3 博主排名                                                                                               
               1.5.4 访客总量                                                                                                                                                                                                                                                                                                              


## 二、应用创建 ##    
- 创建应用  
    > `python manage.py startapp account`

- 应用激活
    > 在`settings.py`的`INSTALLED_APPS`列表中添加`account`  

    
## 三、模型管理 ##   
- 模型创建
    > account\models.py 
    - 账号信息（User）
        >`from django.contrib.auth.models import User`
    
    - 基本资料（AccountUserProfileModel）   
    
    - 详细资料（AccountUserDetailModel）


- 模型注册
    > account\admin.py
 
## 四、表单管理 ##
- 表单创建
    > account\forms.py
    - 登陆表单  
    - 注册表单
    - 邮件表单

## 五、视图管理 ##
- 视图架构
    - 用户界面        
        - 登录      
        - 退出      
        - 注册      
        - 密码重置    
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
        
- 创建视图                                                   
    - 登录视图（AccountLoginView）            
    - 退出视图（AccountLogoutView）            
    - 注册视图（AccountRegisterView）
    - 密码重置视图（AccountPasswordRestView）
    - 个人信息

- 路由配置            