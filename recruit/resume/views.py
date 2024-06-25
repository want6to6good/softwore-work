from django.http import JsonResponse
from rest_framework.decorators import action, api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Resume, Jobseeker,Message
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import mixins, viewsets
from .serializers import ResumeSerializer
@api_view(['POST'])
def change_resume(request):
    username = request.data.get('username')
    name = request.data.get('name')
    gender = request.data.get('sex')
    education = request.data.get('education', '')
    experience = request.data.get('experience', '')
    skills = request.data.get('skills', '')
    projects = request.data.get('projects', '')
    certifications = request.data.get('certifications', '')
    user = get_object_or_404(User, username=username)
    jobseeker = Jobseeker.objects.get(user=user)
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
@api_view(['GET'])
def get_resume(request):
    username = request.query_params.get('username', None)
    print(username)
    if username is not None:
        try:
            user = get_object_or_404(User, username=username)
            jobseeker = Jobseeker.objects.get(user=user)
            resumes = Resume.objects.filter(jobseeker=jobseeker)
            serializer = ResumeSerializer(resumes,many=True)
            return Response(serializer.data)
        except Jobseeker.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"detail": "Username parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
def create_message(request):
    if request.method == 'POST':
        sender_username = request.POST.get('sender_name')
        receiver_username = request.POST.get('receiver_name')
        content = request.POST.get('content')
        sender = get_object_or_404(User, username=sender_username)
        receiver = get_object_or_404(User, username=receiver_username)
        message = Message.objects.create(sender=sender, receiver=receiver, content=content)
        return JsonResponse({'status': 'success', 'message_id': message.id})
    return JsonResponse({'status': 'fail'}, status=400)
# Create your views here.
def get_user_messages(request):
    if request.method == 'PUT':
        username=request.POST.get('username')
        user = get_object_or_404(User, username=username)
        messages = Message.objects.filter(sender=user).union(Message.objects.filter(receiver=user)).order_by('-timestamp')
        messages_data = [{
            'sender': message.sender.username,
            'receiver': message.receiver.username,
            'content': message.content,
            'timestamp': message.timestamp,
            'is_read': message.is_read,
            'id':message.id,
        } for message in messages]
    return JsonResponse({'messages': messages_data})
def mark_message_as_read(request):
    if request.method == 'POST':
        message_id = request.POST.get('message_id')
        message = get_object_or_404(Message, id=message_id)
        message.is_read = True
        message.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)
