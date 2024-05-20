from django.contrib.auth.models import User
from rest_framework import serializers
from user.models import Jobseeker, HR,Company
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class JobseekerSerializer(serializers.ModelSerializer):
    # 用于创建的只写字段
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    class Meta:
        model = Jobseeker
        fields = '__all__'
class HRSerializer(serializers.ModelSerializer):
    # 用于创建的只写字段
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), source='company', write_only=True)
    class Meta:
        model = HR
        fields = '__all__'