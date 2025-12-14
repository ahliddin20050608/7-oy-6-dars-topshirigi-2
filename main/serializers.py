from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


from .models import Employee, Project, Company, GenderChoice, ProfessionChoice
from django.utils import timezone
class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    slug = serializers.SlugField(read_only=True)
    phone = serializers.CharField(max_length=100)
    is_active = serializers.BooleanField(default=True)
    
    def validate_name(self, name):
        if len(name) < 3:
            raise serializers.ValidationError("Ism juda qisqa!")
            
        return name
    def validate_phone(self, phone):
        if not phone.startswith("+998"):
            raise serializers.ValidationError("Telefon raqam '+998' bilan boshlanishi kerak! ")
        return phone
    
    
    def create(self, validated_data):
        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length = 100)
    phone = serializers.CharField(max_length = 50)
    gender = serializers.ChoiceField(choices=GenderChoice.choices)
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    profession = serializers.ChoiceField(choices=ProfessionChoice.choices)
    
    def validate_phone(self, phone):
        if not phone.isdigit():
            raise serializers.ValidationError("Telefon raqam faqat raqamlardan iborat bo'lishi kerak!")
        return phone
    
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.company = validated_data.get('company', instance.company)
        instance.profession = validated_data.get('profession', instance.profession)
        instance.save()
        return instance
            
    def __str__(self):
        return self.name
    

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
    def validate_end_date(self, end_date):
        hozirgi_vaqt = timezone.now()
        if end_date <= hozirgi_vaqt:
            raise serializers.ValidationError("end_date hozirgi vaqtdan katta bo'lishi kerak!")
        return end_date