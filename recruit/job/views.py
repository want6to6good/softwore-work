from django.shortcuts import render
from rest_framework import mixins, viewsets
from .models import Job,Application
from user.models import Company,Jobseeker
from .serializers import JobSerializer,ApplicationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class JobListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """职位列表页"""
    # 这里要定义一个默认的排序，否则会报错
    queryset = Job.objects.all().order_by('id')[:0]
    # 序列化
    serializer_class = JobSerializer
    # 重写queryset
    def get_queryset(self):
        # 获取查询参数
        company_id = self.request.query_params.get("company_id")
        location = self.request.query_params.get("location")
        min_salary = self.request.query_params.get("min_salary")
        max_salary = self.request.query_params.get("max_salary")
        # 初始查询集
        queryset = Job.objects.all()
        # 过滤公司
        if company_id:
            queryset = queryset.filter(company_id=company_id)
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
        job_id = self.request.query_params.get("job_id")
        jobseeker_id = self.request.query_params.get("jobseeker_id")
        # 初始查询集
        queryset = Application.objects.all()
        # 过滤职位
        if job_id:
            queryset = queryset.filter(job_id=job_id)
        # 过滤求职者
        if jobseeker_id:
            queryset = queryset.filter(jobseeker_id=jobseeker_id)
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
        company_id = request.data.get('company_id')
        location = request.data.get('location')
        salary = request.data.get('salary')
        # 校验必填字段
        if not all([title, description, requirements, company_id, location, salary]):
            return Response({"detail": "所有字段都是必填的"}, status=status.HTTP_400_BAD_REQUEST)
        company = get_object_or_404(Company, id=company_id)
        job = Job.objects.create(
            title=title,
            description=description,
            requirements=requirements,
            company=company,
            location=location,
            salary=salary
        )

        return Response({"detail": "工作岗位创建成功", "job_id": job.id}, status=status.HTTP_201_CREATED)
class CreateApplicationView(APIView):
    def post(self, request, *args, **kwargs):
        name = request.data.get('username')
        job = request.data.get('jobname')
        # 校验必填字段
        if not all([name,job]):
            return Response({"detail": "所有字段都是必填的"}, status=status.HTTP_400_BAD_REQUEST)
        seeker=Jobseeker.objects.get(name=name)
        job=job.objects.get(title=job)
        application = Application.objects.create(
            job=job,
            jobseeker=seeker
        )
        return Response({"detail": "简历投递成功"}, status=status.HTTP_201_CREATED)
# Create your views here.
