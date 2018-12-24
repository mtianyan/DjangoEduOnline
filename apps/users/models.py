from django.db import models
from datetime import datetime

# Create your models here.
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    自定义扩展的用户model
    """
    # 自定义的性别选择规则
    GENDER_CHOICES = (
        ("male", "男"),
        ("female", "女")
    )
    # 昵称
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    # 生日，可以为空
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    # 性别 只能男或女，默认女
    gender = models.CharField(
        max_length=5,
        verbose_name="性别",
        choices=GENDER_CHOICES,
        default="female")
    # 地址
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    # 电话
    mobile = models.CharField(max_length=11, null=True, blank=True)
    # 头像 默认使用default.png
    image = models.ImageField(
        upload_to="image/%Y/%m",
        default="image/default.png",
        max_length=100
    )

    # meta信息，即后台栏目名
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # python3重载str方法，打印实例会打印username，username为父类AbstractUser的字段
    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    """
    邮箱验证码model
    """
    # 可供发送验证码类型选择
    SEND_CHOICES = (
        ("register", "注册用户"),
        ("forget", "找回密码"),
        ("update_email", "修改邮箱"),
    )
    # 验证码
    code = models.CharField(max_length=20, verbose_name="验证码")
    # 默认email不可为空；未设置null = true blank = true
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    # 发送验证码类型
    send_type = models.CharField(choices=SEND_CHOICES, max_length=20, verbose_name="验证码类型")
    # 这里的now得去掉(),不去掉会根据编译时间，而不是根据实例化时间。
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")

    class Meta:
        verbose_name = "邮箱验证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    """
    首页轮播图model
    """
    # 轮播图标题
    title = models.CharField(max_length=100, verbose_name="标题")
    # 图片
    image = models.ImageField(
        upload_to="banner/%Y/%m",
        verbose_name="轮播图",
        max_length=100)
    # 点击后的访问地址
    url = models.URLField(max_length=200, verbose_name="访问地址")
    # 默认index很大靠后，想要靠前修改index值。
    index = models.IntegerField(default=100, verbose_name="顺序")
    # 添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "首页轮播"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}(位于第{1}位)'.format(self.title, self.index)
