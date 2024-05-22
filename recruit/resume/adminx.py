import xadmin

from xadmin.views import CommAdminView, BaseAdminView
from .models import Resume

class GlobalSetting(object):
    # 全局设置
    site_title = '招聘后台管理系统'
    site_footer = 'Design by EMT'
    # 菜单默认收缩
    # menu_style = 'accordion'
class BaseSetting(object):
    # 启动主题管理器
    enable_themes = True
    # 使用主题
    use_bootswatch = True
class ResumeAdmin(object):
    list_display = ['id', 'jobseeker', 'education', 'experience', 'skills', 'projects', 'certifications']
    list_filter = ['jobseeker']
    search_fields = ['id', 'jobseeker__name', 'education', 'experience', 'skills', 'projects', 'certifications']
    list_display_links = ['jobseeker']
    list_per_page = 10
    model_icon = 'fa fa-file-text'  # 指定简历模型的图标

xadmin.site.register(CommAdminView, GlobalSetting)
xadmin.site.register(BaseAdminView, BaseSetting)
xadmin.site.register(Resume, ResumeAdmin)