from django.db import models

from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=32, verbose_name="姓名", default="")
    image = models.ImageField(upload_to="avatar/%Y/%m/%d", default=u"image/default.png", max_length=128, verbose_name="头像")
    roles = models.ManyToManyField(to='Role', verbose_name='角色')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Role(models.Model):
    """
    角色
    """
    name = models.CharField(max_length=32, unique=True, verbose_name="角色")
    permissions = models.ManyToManyField("Permission", blank=True, verbose_name="权限")
    menus = models.ManyToManyField("Menu", blank=True, verbose_name="菜单")
    desc = models.CharField(max_length=100, blank=True, null=True, verbose_name="描述")

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Permission(models.Model):
    """
    权限
    """
    name = models.CharField(max_length=32, unique=True,verbose_name="权限名称")
    method = models.CharField(max_length=64, unique=True, verbose_name="权限方法")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "权限"
        verbose_name_plural = verbose_name


class Menu(models.Model):
    """
    菜单
    """
    name = models.CharField(max_length=30, unique=True, verbose_name="菜单名")
    path = models.CharField(max_length=128, unique=True, verbose_name="菜单地址")
    icon = models.CharField(max_length=128, null=True, blank=True, verbose_name="图标")
    is_frame = models.BooleanField(default=False, verbose_name="外部链接")
    is_show = models.BooleanField(default=True, verbose_name="显示标记")
    component = models.CharField(max_length=128, null=True, blank=True, verbose_name="组件")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="父菜单")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '菜单'
        verbose_name_plural = verbose_name
