from django.test import TestCase
from user.adminx import CompanyAdmin, JobseekerAdmin, HRAdmin
from user.models import Company, Jobseeker, HR
import xadmin
from user.resource import JobseekerResource
class CompanyAdminTest(TestCase):
    def test_company_admin_config(self):
        company_admin = CompanyAdmin(Company, xadmin.site)
        self.assertEqual(company_admin.list_display, ['id', 'name', 'industry', 'location'])
        self.assertEqual(company_admin.list_filter, ['industry', 'location'])
        self.assertEqual(company_admin.search_fields, ['id', 'name', 'industry', 'location'])
        self.assertEqual(company_admin.list_display_links, ['name'])
        self.assertEqual(company_admin.list_per_page, 10)
        self.assertEqual(company_admin.model_icon, 'fa fa-building')
class JobseekerAdminTest(TestCase):
    def test_jobseeker_admin_config(self):
        jobseeker_admin = JobseekerAdmin(Jobseeker, xadmin.site)
        self.assertEqual(jobseeker_admin.list_display, ['id', 'name', 'user', 'gender', 'resume', 'skills'])
        self.assertEqual(jobseeker_admin.list_filter, ['gender', 'skills'])
        self.assertEqual(jobseeker_admin.search_fields, ['id', 'name', 'skills'])
        self.assertEqual(jobseeker_admin.list_display_links, ['name'])
        self.assertEqual(jobseeker_admin.list_per_page, 10)
        self.assertEqual(jobseeker_admin.model_icon, 'fa fa-user')
        self.assertEqual(jobseeker_admin.relfield_style, 'fk-ajax')
        self.assertEqual(jobseeker_admin.import_export_args, {'import_resource_class': JobseekerResource})
class HRAdminTest(TestCase):
    def test_hr_admin_config(self):
        hr_admin = HRAdmin(HR, xadmin.site)
        self.assertEqual(hr_admin.list_display, ['id', 'name', 'user', 'department', 'company'])
        self.assertEqual(hr_admin.list_filter, ['company', 'department'])
        self.assertEqual(hr_admin.search_fields, ['id', 'name', 'department', 'company__name'])
        self.assertEqual(hr_admin.list_display_links, ['name'])
        self.assertEqual(hr_admin.list_per_page, 10)
        self.assertEqual(hr_admin.model_icon, 'fa fa-users')

