from rest_framework import serializers

from .models import Course


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name", "code", "status"]


class CourseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
