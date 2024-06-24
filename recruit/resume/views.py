from rest_framework.decorators import action
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
        username = request.data.get('name')
        gender = request.data.get('sex')
        education = request.data.get('education', '')
        experience = request.data.get('experience', '')
        skills = request.data.get('skills', '')
        projects = request.data.get('projects', '')
        certifications = request.data.get('certifications', '')
        jobseeker = get_object_or_404(Jobseeker, name=username)
        gender_map = {
            '男': 'm',
            '女': 'f'
        }
        if gender in ['男', '女']:  # 检查性别值是否有效
            jobseeker.gender = gender_map[gender]
            jobseeker.save()
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
    queryset = Resume.objects.all().order_by('id')
    serializer_class = ResumeSerializer
    @action(detail=False, methods=['put'])
    def get_resume(self, request):
        username = request.data.get('username', None)
        if username is not None:
            try:
                jobseeker = Jobseeker.objects.get(name=username)
                serializer = self.get_serializer(jobseeker)
                return Response(serializer.data)
            except Jobseeker.DoesNotExist:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"detail": "Username parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
