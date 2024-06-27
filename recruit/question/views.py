import os
import subprocess
from datetime import timezone
import json
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


def execute_code(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            code = data.get('code')
            question_id = data.get('question_id')
            # print("Received code:\n", code)
            # print("Question ID:", question_id)

            if not code:
                return JsonResponse({'error': 'No code provided'}, status=400)

            # 创建解决方案文件
            solution_filename = f'{question_id}_solution.py'
            solution_filepath = os.path.join(
                os.path.dirname(__file__), solution_filename)

            # 保存提交的代码
            with open(solution_filepath, 'w') as solution_file:
                solution_file.write(code)

            # 测试脚本路径
            test_script = f'test_files/test_question_{question_id}.py'
            test_filepath = os.path.join(
                os.path.dirname(__file__), test_script)

            # 执行测试脚本
            result = subprocess.run(
                ['python', test_filepath, solution_filepath],
                capture_output=True,
                text=True,
                timeout=10
            )

            # 删除解决方案文件
            os.remove(solution_filepath)

            print(result.stdout)

            return JsonResponse({
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode
            })

        except Exception as e:
            print(f"Error: {str(e)}")
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
