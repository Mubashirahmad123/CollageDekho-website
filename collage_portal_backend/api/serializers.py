from rest_framework import serializers

from .models import *


class CollegeSerializer(serializers.ModelSerializer):
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
        
        
        