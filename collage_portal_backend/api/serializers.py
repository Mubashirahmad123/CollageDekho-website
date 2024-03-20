from rest_framework import serializers

from .models import *


class CollegeSerializer(serializers.ModelSerializer):
    
    # courses = CourseSerializer(many=True, read_only=True)
    # department = DepartmentSerializer(many=True, read_only=True)
    class Meta:
        model = College
        fields = '__all__'
        
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
    
    # Optionally include only necessary fields from College model
    # college = CollegeSerializer()

    def create(self, validated_data):
        # Extract college ID from validated data
        college_id = validated_data.pop('college')
        
        # Retrieve the college object or raise an error if not found
        college = College.objects.get(id=college_id)
        
        # Create the course associated with the college
        course = Course.objects.create(college=college, **validated_data)
        return course


class SpecializationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Specialization
        fields = '__all__'
                
        


class DepartmentSerializer(serializers.ModelSerializer):
    
    courses = CourseSerializer(many=True, read_only=True)
    specializations = SpecializationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Department
        fields = '__all__'
        
class FeeSerializer(serializers.ModelSerializer):
    
    department = DepartmentSerializer()
    
    
    
    class Meta:
        model = Fee
        fields = '__all__'
        
        
class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = '__all__'        
        


class   ReviewSerializer(serializers.ModelSerializer):
    
    # country = CountrySerializer()
    # course = CourseSerializer()
    # college = CollegeSerializer() Dont add these three
     
    class Meta:
        model = Review
        fields = '__all__' 