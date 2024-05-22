from django.db import models
from user.models import Jobseeker
class Resume(models.Model):
    """简历"""
    jobseeker = models.OneToOneField(Jobseeker, on_delete=models.CASCADE, verbose_name="求职者", related_name='resume')
    education = models.TextField("教育经历", blank=True)
    experience = models.TextField("工作经历", blank=True)
    skills = models.TextField("技能", blank=True)
    projects = models.TextField("项目经历", blank=True)
    certifications = models.TextField("认证和证书", blank=True)
    class Meta:
        ordering = ['id']
        verbose_name = '简历'
        verbose_name_plural = verbose_name
    def __str__(self):
        return f"{self.jobseeker.name}的简历"
# Create your models here.
