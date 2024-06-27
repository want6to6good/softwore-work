import os
import subprocess
from datetime import timezone

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from question.models import Choice, Fill, Judge, Subjective
from question.serializers import ChoiceSerializer, FillSerializer, JudgeSerializer, SubjectiveSerializer
# Create your views here.

class ChoiceListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """选择题列表页"""
    # 这里要定义一个默认的排序，否则会报错
    queryset = Choice.objects.all().order_by('id')[:0]
    # 序列化
    serializer_class = ChoiceSerializer
    # 重写queryset
    def get_queryset(self):
        # 题目数量
        choice_number = int(self.request.query_params.get("choice_number"))
        level = int(self.request.query_params.get("level", 1))

        if choice_number:
            self.queryset = Choice.objects.all().filter(level=level).order_by('?')[:choice_number]
        return self.queryset
class FillListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """填空题列表页"""
    # 这里要定义一个默认的排序，否则会报错
    queryset = Fill.objects.all().order_by('id')[:0]
    # 序列化
    serializer_class = FillSerializer

    # 重写queryset
    def get_queryset(self):
        # 题目数量
        fill_number = int(self.request.query_params.get("fill_number"))
        level = int(self.request.query_params.get("level", 1))

        if fill_number:
            self.queryset = Fill.objects.all().filter(level=level).order_by('?')[:fill_number]
        return self.queryset
class JudgeListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """判断题列表页"""
    # 这里要定义一个默认的排序，否则会报错
    queryset = Judge.objects.all().order_by('?')[:0]
    # 序列化
    serializer_class = JudgeSerializer
    # 重写queryset
    def get_queryset(self):
        # 题目数量
        judge_number = int(self.request.query_params.get("judge_number"))
        level = int(self.request.query_params.get("level", 1))

        if judge_number:
            self.queryset = Judge.objects.all().filter(level=level).order_by('?')[:judge_number]
        return self.queryset
class SubjectiveListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """主观题列表页"""
    # 这里定义一个默认的排序，否则会报错
    queryset = Subjective.objects.all().order_by('?')[:0]
    # 序列化
    serializer_class = SubjectiveSerializer
    # 重写queryset
    def get_queryset(self):
        # 题目数量
        subjective_number = int(self.request.query_params.get("subjective_number"))
        level = int(self.request.query_params.get("level", 1))

        if subjective_number:
            self.queryset = Subjective.objects.all().filter(level=level).order_by('?')[:subjective_number]
        return self.queryset
@csrf_exempt
# @api_view(['POST'])
def execute_code(request):
    if request.method == 'POST':
        try:
            code = request.POST.get('code')
            print(code)
            if not code:
                return JsonResponse({'error': 'No code provided'}, status=400)
            # 创建一个唯一的文件名
            timestamp = timezone.now().strftime('%Y%m%d%H%M%S%f')
            filename = f'code_{timestamp}.py'
            filepath = os.path.abspath(__file__)
            # 将代码保存为文件
            with open(filepath, 'w') as code_file:
                code_file.write(code)
            # 执行代码
            result = subprocess.run(['python', filepath], capture_output=True, text=True, timeout=10)
            # 删除文件
            os.remove(filepath)
            return JsonResponse({
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)