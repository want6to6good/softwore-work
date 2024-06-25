"""recruit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.contrib import admin
from django.urls import path,include, re_path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from job.views import JobListViewSet, ApplicationListViewSet, UpdateApplicationStatusView, CreateJobView, \
    CreateApplicationView
from resume.views import change_resume,ResumeListViewSet,get_resume,create_message,get_user_messages,mark_message_as_read
from user.views import JobseekerViewSet, HRViewSet, CompanyViewSet,UpdatePwdApi,RegisterViewSet,get_personal_info
from question.views import ChoiceListViewSet,FillListViewSet,JudgeListViewSet,SubjectiveListViewSet

router = DefaultRouter()

router.register(r'choices', ChoiceListViewSet)
router.register(r'fills', FillListViewSet)
router.register(r'judges', JudgeListViewSet)
router.register(r'subjective', SubjectiveListViewSet)
router.register(r'job', JobListViewSet)
router.register(r'application', ApplicationListViewSet)
router.register(r'application_create', CreateApplicationView)
router.register(r'get_personal_info_list', JobseekerViewSet)
router.register(r'get_resume_list',ResumeListViewSet)
router.register(r'hr', HRViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'register', RegisterViewSet)


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('jwt-auth/', obtain_jwt_token),
    path('update-pwd/', UpdatePwdApi.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('update/', UpdateApplicationStatusView),
    path('create/', CreateJobView),
    path('change_resume/', change_resume),
    path('create_message/',create_message),
    path('get_messsage/',get_user_messages),
    path('markread/',mark_message_as_read),
    path('get_resume/',get_resume),
    path('get_personal_info/',get_personal_info),
    re_path('^', include(router.urls))
]
