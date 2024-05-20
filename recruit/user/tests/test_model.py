from django.test import TestCase
# from index.models import User
from user.models import Company,HR,Jobseeker
from django.contrib.auth.models import User


# Create your tests here.
class CompanyModelTest(TestCase):
    """公司模型测试"""
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Company.objects.create(name='Tech Co.', industry='Technology', location='Beijing')
    def test_name_label(self):
        company = Company.objects.get(id=1)
        field_label = company._meta.get_field('name').verbose_name
        self.assertEquals(field_label, "公司名称")
    def test_industry_label(self):
        company = Company.objects.get(id=1)
        field_label = company._meta.get_field('industry').verbose_name
        self.assertEquals(field_label, "行业")
    def test_location_label(self):
        company = Company.objects.get(id=1)
        field_label = company._meta.get_field('location').verbose_name
        self.assertEquals(field_label, "位置")
    def test_name_max_length(self):
        company = Company.objects.get(id=1)
        max_length = company._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)
    def test_industry_max_length(self):
        company = Company.objects.get(id=1)
        max_length = company._meta.get_field('industry').max_length
        self.assertEquals(max_length, 100)
    def test_location_max_length(self):
        company = Company.objects.get(id=1)
        max_length = company._meta.get_field('location').max_length
        self.assertEquals(max_length, 100)
    def test_object_name(self):
        company = Company.objects.get(id=1)
        expected_object_name = company.name
        self.assertEquals(expected_object_name, str(company))
class HRModelTest(TestCase):
    """HR模型测试"""
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        company = Company.objects.create(name='Tech Co.', industry='Technology', location='Beijing')
        User.objects.create(username='user0', password='6543210')
        HR.objects.create(name='张三', user=User.objects.get(id=1), department='人力资源部', company=company)
    def test_name_label(self):
        hr = HR.objects.get(id=1)
        field_label = hr._meta.get_field('name').verbose_name
        self.assertEquals(field_label, "姓名")
    def test_user_label(self):
        hr = HR.objects.get(id=1)
        field_label = hr._meta.get_field('user').verbose_name
        self.assertEquals(field_label, "用户")
    def test_department_label(self):
        hr = HR.objects.get(id=1)
        field_label = hr._meta.get_field('department').verbose_name
        self.assertEquals(field_label, "部门")
    def test_company_label(self):
        hr = HR.objects.get(id=1)
        field_label = hr._meta.get_field('company').verbose_name
        self.assertEquals(field_label, "公司")
    def test_name_max_length(self):
        hr = HR.objects.get(id=1)
        max_length = hr._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)
    def test_department_max_length(self):
        hr = HR.objects.get(id=1)
        max_length = hr._meta.get_field('department').max_length
        self.assertEquals(max_length, 50)
    def test_object_name(self):
        hr = HR.objects.get(id=1)
        expected_object_name = '%s' % (hr.name)
        self.assertEquals(expected_object_name, str(hr))
class JobseekerModelTest(TestCase):
    """求职者模型测试"""
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(username='user1', password='6543210')
        Jobseeker.objects.create(name='李四', user=User.objects.get(id=1), gender='m', resume='经验丰富的开发者', skills='Python, Django, JavaScript')
    def test_name_label(self):
        jobseeker = Jobseeker.objects.get(id=1)
        field_label = jobseeker._meta.get_field('name').verbose_name
        self.assertEquals(field_label, "姓名")
    def test_user_label(self):
        jobseeker = Jobseeker.objects.get(id=1)
        field_label = jobseeker._meta.get_field('user').verbose_name
        self.assertEquals(field_label, "用户")
    def test_gender_label(self):
        jobseeker = Jobseeker.objects.get(id=1)
        field_label = jobseeker._meta.get_field('gender').verbose_name
        self.assertEquals(field_label, "性别")
    def test_resume_label(self):
        jobseeker = Jobseeker.objects.get(id=1)
        field_label = jobseeker._meta.get_field('resume').verbose_name
        self.assertEquals(field_label, "简历")
    def test_skills_label(self):
        jobseeker = Jobseeker.objects.get(id=1)
        field_label = jobseeker._meta.get_field('skills').verbose_name
        self.assertEquals(field_label, "技能")
    def test_name_max_length(self):
        jobseeker = Jobseeker.objects.get(id=1)
        max_length = jobseeker._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)
    def test_gender_max_length(self):
        jobseeker = Jobseeker.objects.get(id=1)
        max_length = jobseeker._meta.get_field('gender').max_length
        self.assertEquals(max_length, 1)
    def test_skills_max_length(self):
        jobseeker = Jobseeker.objects.get(id=1)
        max_length = jobseeker._meta.get_field('skills').max_length
        self.assertEquals(max_length, 200)
    def test_object_name(self):
        jobseeker = Jobseeker.objects.get(id=1)
        expected_object_name = '%s' % (jobseeker.name)
        self.assertEquals(expected_object_name, str(jobseeker))