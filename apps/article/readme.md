# 文章管理 #

[TOC]

## 一、基本框架 ##                                                                                                                                                          
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

## 二、应用创建 ##    

## 三、模型管理 ##    

## 四、表单管理 ##

## 五、视图管理 ##
- 视图架构
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


- 创建视图                                                                                                                                                                                                                                                  