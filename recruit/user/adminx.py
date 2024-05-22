import xadmin
from user.models import Jobseeker, HR, Company
from import_export import resources
from user.resource import JobseekerResource

class CompanyAdmin(object):
    list_display = ['id', 'name', 'industry', 'location']
    list_filter = ['industry', 'location']
    search_fields = ['id', 'name', 'industry', 'location']
    list_display_links = ['name']
    list_per_page = 10
    model_icon = 'fa fa-building'  # xadmin中显示的图标
class JobseekerAdmin(object):
    list_display = ['id', 'name', 'user', 'gender']
    list_filter = ['gender']
    search_fields = ['id', 'name']
    list_display_links = ['name']
    list_per_page = 10
    model_icon = 'fa fa-user'
    relfield_style = 'fk-ajax'
    import_export_args = {'import_resource_class': JobseekerResource}
class HRAdmin(object):
    list_display = ['id', 'name', 'user', 'department', 'company']
    list_filter = ['company', 'department']
    search_fields = ['id', 'name', 'department', 'company__name']
    list_display_links = ['name']
    list_per_page = 10
    model_icon = 'fa fa-users'

xadmin.site.register(Jobseeker, JobseekerAdmin)
xadmin.site.register(HR, HRAdmin)
xadmin.site.register(Company, CompanyAdmin)
