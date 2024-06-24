from django.db import models
from user.models import Jobseeker
from django.contrib.auth.models import AbstractUser, User
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
class Message(models.Model):
    """消息表"""
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE, verbose_name="发送方")
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE, verbose_name="接收方")
    content = models.TextField("消息内容")
    timestamp = models.DateTimeField("发送时间", auto_now_add=True)
    is_read = models.BooleanField("是否已读", default=False)
    def __str__(self):
        return f'Message from {self.sender} to {self.receiver} at {self.timestamp}'
    class Meta:
        verbose_name = "消息"
        verbose_name_plural = "消息"
        ordering = ['-timestamp']
# Create your models here.
