from import_export import resources, fields
from user.models import Jobseeker

class JobseekerResource(resources.ModelResource):
    class Meta:
        model = Jobseeker
        fields = ('id', 'name', 'user', 'gender', 'resume', 'skills')
        # 如果需要指定不同的列名，可以取消注释以下代码
        # id = fields.Field(attribute='id', column_name='ID')
        # name = fields.Field(attribute='name', column_name='姓名')
        # user = fields.Field(attribute='user', column_name='用户')
        # gender = fields.Field(attribute='gender', column_name='性别')
        # resume = fields.Field(attribute='resume', column_name='简历')
        # skills = fields.Field(attribute='skills', column_name='技能')
