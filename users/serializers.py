from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import User
from main.models import Group

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password":{
                "write_only":True,
            }
        }
        read_only_fields = ("id","role")
    def create(self, validated_data):
        validated_data["role"] = "Teacher"
        return User.objects.create_user(**validated_data)

class GroupSerializer(serializers.ModelSerializer):
    teacher = serializers.IntegerField(required=True)
    class Meta:
        model = Group
        fields = ('id','name','teacher','created_at','updated_at')

        extra_kwargs = {
            'teacher':{'required':True},
        }

    def create(self, validated_data):
        teacher =None
        if validated_data.get('teacher'):
            teacher_id = validated_data.pop('teacher')
            teacher = get_object_or_404(User,id=teacher_id,role="Teacher")
        group = Group.objects.create(**validated_data)
        if teacher:
            teacher.groups.add(group)
        return group