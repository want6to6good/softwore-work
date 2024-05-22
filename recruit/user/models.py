from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.
class Company(models.Model):
    """公司"""
    name = models.CharField("公司名称", max_length=100)
    industry = models.CharField("行业", max_length=100)
    location = models.CharField("位置", max_length=100)
    class Meta:
        ordering = ['id']
        verbose_name = "公司"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
    def get_hr_list(self):
        return self.hr_set.all()  # 通过反向关系获取所有HR
class HR(models.Model):
    """HR模型类"""
    name = models.CharField("姓名", max_length=20, default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="用户")
    department = models.CharField("部门", max_length=50, blank=True)  # 新增字段，保存HR所在部门
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="公司")  # 新增字段
    class Meta:
        ordering = ['id']
        db_table = 'user_hr'
        verbose_name = 'HR'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
class Jobseeker(models.Model):
    """求职者"""
    GENDER_CHOICES = (
        ('m', '男'),
        ('f', '女')
    )
    name = models.CharField("姓名", max_length=20, default="")
    user = models.OneToOneField(User, verbose_name="用户", on_delete=models.CASCADE)
    gender = models.CharField("性别", max_length=1, choices=GENDER_CHOICES, default="")
    class Meta:
        ordering = ['id']
        db_table = 'user_jobseeker'
        verbose_name = '求职者'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
