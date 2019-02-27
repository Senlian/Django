## Django 项目练习 ##
- 创建django工程

''' django-admin startproject prj_name '''

- 创建站点app

'''
cd prj_name
python manage.py startapp AppName
'''

- 启动站点

'''
python manage.py runserver 127.0.0.1:8000
'''

- 全局变量默认设置在文件

''' django/conf/global_settings.py '''

> 在manage.py中设置使用哪个settings.py,其他脚本中如果需要引用设定项也可设置

''' os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pydjango.settings") '''

> 察看当前settings.py与默认设置的不同

''' python manage.py diffsettings '''

> 避免直接倒入默认或自定义的settings.py文件，不要在其他文件导入参数后修改参数的值
> 添加app,添加模板路径，添加静态文件路径

- models数据模型建立
> 保存记录文件

''' python manage.py makemigrations '''

> 保存修改

''' python manage.py migrate '''

- admin 注册数据模型

'''
from . import models
admin.sit.register(models.User)
'''

- 创建超级用户

''' python manage.py createsuperuser '''
