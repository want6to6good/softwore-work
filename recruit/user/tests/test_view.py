from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from user.models import Jobseeker, Company, HR

class CustomBackendTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 创建用户用于测试
        User.objects.create_user(username='test_user', password='test_password')
    def test_authenticate(self):
        # 测试用户认证功能
        client = APIClient()
        response = client.post(reverse('login'), {'username': 'test_user', 'password': 'test_password'}, format='json')
        self.assertEqual(response.status_code, 200)
class RegisterViewSetTest(TestCase):
    def test_create_jobseeker(self):
        # 测试创建求职者用户
        client = APIClient()
        response = client.post(reverse('register'), {'username': 'jobseeker', 'password': 'test_password', 'name': 'Jobseeker', 'role': 'jobseeker'}, format='json')
        self.assertEqual(response.status_code, 201)
    def test_create_hr(self):
        # 测试创建HR用户
        company = Company.objects.create(name='Test Company', industry='IT', location='Test Location')
        client = APIClient()
        response = client.post(reverse('register'), {'username': 'hr', 'password': 'test_password', 'name': 'HR', 'role': 'hr', 'company_id': company.id}, format='json')
        self.assertEqual(response.status_code, 201)
class UpdatePwdApiTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 创建用户用于测试
        User.objects.create_user(username='test_user', password='test_password')
    def test_update_password(self):
        # 测试修改密码功能
        client = APIClient()
        client.login(username='test_user', password='test_password')
        response = client.patch(reverse('update-pwd'), {'userid': 1, 'oldpwd': 'test_password', 'newpwd': 'new_password'}, format='json')
        self.assertEqual(response.status_code, 200)
class JobseekerViewSetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 创建求职者用于测试
        Jobseeker.objects.create(name='Test Jobseeker', user=User.objects.create_user(username='jobseeker', password='test_password'))
    def test_get_jobseekers(self):
        # 测试获取所有求职者信息
        client = APIClient()
        client.login(username='jobseeker', password='test_password')
        response = client.get(reverse('jobseeker-list'))
        self.assertEqual(response.status_code, 200)
class HRViewSetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 创建HR用于测试
        company = Company.objects.create(name='Test Company', industry='IT', location='Test Location')
        HR.objects.create(name='Test HR', user=User.objects.create_user(username='hr', password='test_password'), company=company)
    def test_get_hrs(self):
        # 测试获取所有HR信息
        client = APIClient()
        client.login(username='hr', password='test_password')
        response = client.get(reverse('hr-list'))
        self.assertEqual(response.status_code, 200)
class CompanyViewSetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 创建公司用于测试
        Company.objects.create(name='Test Company', industry='IT', location='Test Location')
    def test_get_companies(self):
        # 测试获取所有公司信息
        client = APIClient()
        response = client.get(reverse('company-list'))
        self.assertEqual(response.status_code, 200)