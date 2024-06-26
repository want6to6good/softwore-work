from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from user.models import Jobseeker, Company,HR
from user.serializers import JobseekerSerializer, UserDetailSerializer, CompanySerializer, HRSerializer
# Create your views here.
class CustomBackend(ModelBackend):
    """自定义用户验证"""
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
def jwt_response_payload_handler(token, user=None, request=None):
    """设置jwt登录之后返回token和user信息"""
    try:
        jobseeker = Jobseeker.objects.get(user=user)
        return {
            'token': token,
            'user': UserDetailSerializer(user, context={'request': request}).data,
            'jobseeker': JobseekerSerializer(jobseeker, context={'request': request}).data
        }
    except Jobseeker.DoesNotExist:
        try:
            hr = HR.objects.get(user=user)
            return {
                'token': token,
                'user': UserDetailSerializer(user, context={'request': request}).data,
                'hr': HRSerializer(hr, context={'request': request}).data
            }
        except HR.DoesNotExist:
            return None
class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """用户注册"""
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    def create(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.data['username'])
        if user:
            return Response({'msg': '用户名已存在'}, status=status.HTTP_201_CREATED)
        user_detail = UserDetailSerializer(data=request.data)
        if user_detail.is_valid():
            user_detail.save()
        user = User.objects.get(username=request.data['username'])
        # 密码转成密文存储
        user.password = make_password(user.password)
        user.save()
        # 看是hr还是求职者
        if request.data.get('role') == 'jobseeker':
            jobseeker = Jobseeker(user=user, name=request.data['name'])
            if jobseeker:
                jobseeker.save()
        elif request.data.get('role') == 'hr':
            company = Company.objects.get(id=request.data['company_id'])
            hr = HR(user=user, name=request.data['name'], company=company,
                    department=request.data.get('department', ''))
            if hr:
                hr.save()
        return Response(user_detail.errors)
class UpdatePwdApi(APIView):
    """修改用户密码"""
    def patch(self, request):
        # 获取参数
        old_pwd = request.data['oldpwd']
        new_pwd = request.data['newpwd']
        user_id = request.data['userid']
        # 获得请求用户
        user = User.objects.get(id=user_id)
        # 检查原始密码是否正确
        if user.check_password(old_pwd):
            user.set_password(new_pwd)
            user.save()
        else:
            return Response(data={'msg': 'fail'}, status=status.HTTP_200_OK)
        # 返回数据
        return Response(data={'msg': 'success'}, status=status.HTTP_200_OK)
class JobseekerViewSet(viewsets.ModelViewSet):
    """求职者信息"""
    queryset = Jobseeker.objects.all().order_by('id')
    serializer_class = JobseekerSerializer
@api_view(['GET'])
def get_personal_info(request):
    username = request.query_params.get('username', None)
    if username:
        try:
            user = get_object_or_404(User, username=username)
            jobseeker = Jobseeker.objects.get(user=user)
            serializer = JobseekerSerializer(jobseeker)
            return Response(serializer.data)
        except Jobseeker.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"detail": "Username parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
class HRViewSet(viewsets.ModelViewSet):
    """HR信息"""
    # 查询集
    queryset = HR.objects.all().order_by('id')
    # 序列化
    serializer_class = HRSerializer
class CompanyViewSet(viewsets.ModelViewSet):
    """公司信息"""
    # 查询集
    queryset = Company.objects.all().order_by('id')
    # 序列化
    serializer_class = CompanySerializer
