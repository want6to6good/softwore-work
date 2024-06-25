from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Job,Application
from user.models import Company,Jobseeker
from .serializers import JobSerializer,ApplicationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
import logging

logger = logging.getLogger(__name__)
class JobListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """职位列表页"""
    # 这里要定义一个默认的排序，否则会报错
    queryset = Job.objects.all().order_by('id')[:0]
    # 序列化
    serializer_class = JobSerializer
    # 重写queryset
    def get_queryset(self):
        # 获取查询参数
        company_name = self.request.query_params.get("company_name")
        location = self.request.query_params.get("location")
        min_salary = self.request.query_params.get("min_salary")
        max_salary = self.request.query_params.get("max_salary")
        # 初始查询集
        queryset = Job.objects.all()
        # 过滤公司
        if company_name:
            queryset = queryset.filter(company_name=company_name)
        # 过滤工作地点
        if location:
            queryset = queryset.filter(location=location)
        # 过滤薪资范围
        if min_salary:
            queryset = queryset.filter(salary__gte=min_salary)
        if max_salary:
            queryset = queryset.filter(salary__lte=max_salary)
        # 随机排序
        queryset = queryset.order_by('?')
        return queryset
class ApplicationListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """职位申请列表页"""
    queryset = Application.objects.all().order_by('id')[:0]
    serializer_class = ApplicationSerializer
    def get_queryset(self):
        # 获取查询参数
        job_name = self.request.query_params.get("job_name")
        jobseeker_name = self.request.query_params.get("jobseeker_name")
        # 初始查询集
        queryset = Application.objects.all()
        # 过滤职位
        if job_name:
            queryset = queryset.filter(job__title=job_name)
        # 过滤求职者
        if jobseeker_name:
            queryset = queryset.filter(jobseeker__name=jobseeker_name)
        return queryset
class UpdateApplicationStatusView(APIView):
    """更新职位申请状态"""
    def put(self, request, *args, **kwargs):
        application_id = request.data.get('application_id')
        new_status = request.data.get('status')
        # 校验新的状态是否有效
        valid_statuses = ['applied', 'interview', 'hired', 'rejected']
        if new_status not in valid_statuses:
            return Response({"detail": "无效的申请状态"}, status=status.HTTP_400_BAD_REQUEST)
        application = get_object_or_404(Application, id=application_id)
        # 更新申请状态
        application.status = new_status
        application.save()
        return Response({"detail": "申请状态更新成功"}, status=status.HTTP_200_OK)
class CreateJobView(APIView):
    """增添新的工作岗位"""
    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        description = request.data.get('description')
        requirements = request.data.get('requirements')
        company_name= request.data.get('company_name')
        location = request.data.get('location')
        salary = request.data.get('salary')
        # 校验必填字段
        if not all([title, description, requirements, company_name, location, salary]):
            return Response({"detail": "所有字段都是必填的"}, status=status.HTTP_400_BAD_REQUEST)
        company = get_object_or_404(Company, name=company_name)
        job = Job.objects.create(
            title=title,
            description=description,
            requirements=requirements,
            company=company,
            location=location,
            salary=salary
        )

        return Response({"detail": "工作岗位创建成功", "job_id": job.id}, status=status.HTTP_201_CREATED)
class CreateApplicationView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    
    @action(detail=False, methods=['post'])
    def create_application(self, request, *args, **kwargs):
        name = request.data.get('username')
        job_title = request.data.get('jobname')
        # 校验必填字段
        if not all([name,job_title]):
            return Response({"detail": "所有字段都是必填的"}, status=status.HTTP_400_BAD_REQUEST)
        user = get_object_or_404(User, username=name)
        seeker = Jobseeker.objects.get(user=user)
        job_instance = Job.objects.get(title=job_title)  # 使用正确的模型类和变量名进行查询
        application = Application.objects.create(
            job=job_instance,
            jobseeker=seeker
        )
        return Response({"detail": "简历投递成功"}, status=status.HTTP_201_CREATED)
# Create your views here.
