# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 7:41 下午
# @Author  : all is well
# @File    : custom_permission.py
# @Software: PyCharm

import re
from baby_ops.settings import JWT_AUTH
from rest_framework.permissions import BasePermission
from rest_framework_jwt.utils import jwt_decode_handler
from rbac.models import UserProfile


class CustomRbacPermission(BasePermission):
    """
    自定义权限
    """
    def has_permission(self, request, view):
        # 获取用户信息
        header_method = request.META.get('REQUEST_METHOD')
        header_token = request.META.get('HTTP_AUTHORIZATION')
        header_prefix = JWT_AUTH['JWT_AUTH_HEADER_PREFIX']
        token = header_token.lstrip(header_prefix)
        token_info = jwt_decode_handler(token)
        user_obj = UserProfile.objects.filter(username=token_info['username']).first()

        # 判断是否是超级管理员
        # if user_obj.is_superuser:
        #     return True

        # 获取用户权限
        permissions_list = []
        for perm_dict in user_obj.roles.values('permissions__method').distinct():
            permissions_list.append(perm_dict['permissions__method'])

        if permissions_list:
            perms_map = {'GET': 'list', 'POST': 'create', 'PUT': 'edit', 'DELETE': 'delete'}
            print(permissions_list)
            for perm in permissions_list:
                check_perm = re.search('{}'.format(perms_map[header_method]), perm)
                if check_perm is not None:
                    return True
        return False



