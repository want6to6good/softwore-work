
from rest_framework import serializers
from .models import Job,Application
from user.serializers import JobseekerSerializer
from user.models import Jobseeker
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
class ApplicationSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    jobseeker = JobseekerSerializer(read_only=True)
    job_id = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all(), source='job', write_only=True)
    jobseeker_id = serializers.PrimaryKeyRelatedField(queryset=Jobseeker.objects.all(), source='jobseeker', write_only=True)
    class Meta:
        model = Application
        fields = '__all__'