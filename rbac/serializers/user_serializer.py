# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 12:15 下午
# @Author  : all is well
# @File    : user_serializer.py
# @Software: PyCharm

from rest_framework import serializers
from rbac.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'name', 'email', 'image', 'is_active', 'roles']
        depth = 2
