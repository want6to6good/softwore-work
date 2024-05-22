from django.db import models
from user.models import Company,Jobseeker
class Job(models.Model):
    """职位"""
    title = models.CharField("职位名称", max_length=100)
    description = models.TextField("职位描述")
    requirements = models.TextField("职位要求")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="公司")
    location = models.CharField("工作地点", max_length=100)
    posted_date = models.DateField("发布日期", auto_now_add=True)
    salary = models.DecimalField("薪资", max_digits=10, decimal_places=2)
    class Meta:
        ordering = ['id']
        verbose_name = "职位"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
class Application(models.Model):
    """职位申请"""
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="职位")
    jobseeker = models.ForeignKey(Jobseeker, on_delete=models.CASCADE, verbose_name="求职者")
    applied_date = models.DateField("申请日期", auto_now_add=True)
    status = models.CharField("申请状态", max_length=20, choices=[
        ('applied', '已申请'),
        ('interview', '面试中'),
        ('hired', '已录用'),
        ('rejected', '已拒绝')
    ], default='applied')
    class Meta:
        ordering = ['id']
        verbose_name = "职位申请"
        verbose_name_plural = verbose_name
    def __str__(self):
        return f"{self.jobseeker.name} - {self.job.title}"
# Create your models here.
