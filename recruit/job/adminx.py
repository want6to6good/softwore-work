import xadmin
from .models import Application,Job

class JobAdmin(object):
    list_display = ['id', 'title', 'company', 'location', 'posted_date', 'salary']
    list_filter = ['company', 'location', 'posted_date']
    search_fields = ['id', 'title', 'company__name', 'location', 'requirements']
    list_display_links = ['title']
    list_per_page = 10
    model_icon = 'fa fa-briefcase'  # 使用公文包图标表示职位
class ApplicationAdmin(object):
    list_display = ['id', 'job', 'jobseeker', 'applied_date', 'status']
    list_filter = ['job', 'jobseeker', 'status', 'applied_date']
    search_fields = ['id', 'job__title', 'jobseeker__name', 'status']
    list_display_links = ['job', 'jobseeker']
    list_per_page = 10
    model_icon = 'fa fa-envelope'  # 使用信封图标表示职位申请

xadmin.site.register(Job, JobAdmin)
xadmin.site.register(Application, ApplicationAdmin)
