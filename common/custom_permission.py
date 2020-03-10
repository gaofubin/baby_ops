# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 7:41 下午
# @Author  : all is well
# @File    : custom_permission.py
# @Software: PyCharm

from rest_framework.permissions import BasePermission


class CustomRbacPermission(BasePermission):
    """
    自定义权限
    """
    def has_permission(self, request, view):
        # print(request.user.roles)
        # permission_list = request.user.roles.values('permission__method')
        # print(permission_list)

        return True

