from rest_framework import serializers
from .models import Doctor

class DoctorRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        return Doctor.objects.create_user(**validated_data)

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization', 'qualifications', 'email', 'office_number', 'bio', 'password']
        extra_kwargs = {'password': {'write_only': True}}



class DoctorSerializer(serializers.ModelSerializer):
    qualification_name=serializers.CharField(source='qualifications.name',read_only=True)
    class Meta:
        model=Doctor
        fields=['id','name','qualification_name','specialization','email','office_number',]
        extra_kwargs = {'password': {'write_only': True}}