
from rest_framework import serializers
from .models import Job,Application
from user.serializers import JobseekerSerializer
from user.models import Jobseeker
class JobSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = ['title', 'description', 'requirements', 'company_name', 'location', 'posted_date', 'salary']
    def get_company_name(self, obj):
        return obj.company.name
class ApplicationSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    jobseeker = JobseekerSerializer(read_only=True)
    job_id = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all(), source='job', write_only=True)
    jobseeker_id = serializers.PrimaryKeyRelatedField(queryset=Jobseeker.objects.all(), source='jobseeker', write_only=True)
    class Meta:
        model = Application
        fields = '__all__'