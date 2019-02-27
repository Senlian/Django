from django.db import models
from django.utils.html import format_html


# Create your models here.
class dbServer(models.Model):
    STATUDS_CHOICE = (
        ("T", "正常"),
        ("F", "异常"),
    )
    pid = models.AutoField(verbose_name="序号", primary_key=True)

    host = models.GenericIPAddressField(verbose_name="IP地址", default="127.0.0.1", blank=False, unique=False)
    port = models.IntegerField(verbose_name="端口号", default=7800, null=False)
    username = models.CharField(verbose_name="用户名", max_length=128, blank=True, null=True)
    passwd = models.CharField(verbose_name="密码", max_length=256, blank=True, null=True)
    count = models.BigIntegerField(verbose_name="数据量", max_length=256, default=0)
    status = models.CharField(verbose_name="状态", max_length=64, choices=STATUDS_CHOICE, default="T", blank=False)
    describtion = models.TextField(verbose_name="描述", max_length=512, blank=True, null=True)

    ctime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __str__(self):
        return self.host

    def colored_status(self):
        if self.status == "F":
            color_code = "red"
            value = "异常"
        else:
            color_code = "blue"
            value = "正常"
        return format_html('<span style="color: {};">{}</span>',
                           color_code,
                           value,
                           )

    colored_status.short_description = status.verbose_name

    # colored_status.admin_order_field = status.verbose_name

    class Meta:
        # 联合唯一键
        unique_together = ("host", "port")
        # 通过哪个键获取最后创建数据
        get_latest_by = "ctime"
        # 排序方式，前边如果加-表示降序
        ordering = ["pid", "host", "ctime"]
        #  外层容器名
        verbose_name_plural = "Redis数据库列表"
        # 里层容器名
        verbose_name = "数据库"
