from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Resume, Jobseeker
from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from .serializers import ResumeSerializer
class ResumeView(APIView):
    """新建或修改个人简历"""
    def post(self, request, *args, **kwargs):
        jobseeker_id = request.data.get('jobseeker_id')
        education = request.data.get('education', '')
        experience = request.data.get('experience', '')
        skills = request.data.get('skills', '')
        projects = request.data.get('projects', '')
        certifications = request.data.get('certifications', '')
        jobseeker = get_object_or_404(Jobseeker, id=jobseeker_id)
        # 检查简历是否存在
        resume, created = Resume.objects.update_or_create(
            jobseeker=jobseeker,
            defaults={
                'education': education,
                'experience': experience,
                'skills': skills,
                'projects': projects,
                'certifications': certifications,
            }
        )
        if created:
            return Response({"detail": "简历创建成功"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "简历更新成功"}, status=status.HTTP_200_OK)
class ResumeListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """职位申请列表页"""
    queryset = Resume.objects.all().order_by('id')[:0]
    serializer_class = ResumeSerializer
    def get_queryset(self):
        # 获取查询参数
        jobseeker_id = self.request.query_params.get("jobseeker_id")
        # 初始查询集
        queryset = super().get_queryset()
        # 过滤求职者
        if jobseeker_id:
            queryset = queryset.filter(jobseeker__id=jobseeker_id)
        return queryset
# Create your views here.
