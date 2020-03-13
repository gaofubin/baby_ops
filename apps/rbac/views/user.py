# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 12:15 下午
# @Author  : all is well
# @File    : user.py
# @Software: PyCharm

from rest_framework_jwt.utils import jwt_decode_handler
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from common.custom_json_response import JsonResponse
from common.custom_viewset_base import CustomViewSet
from common.custom_permission import CustomRbacPermission
from rest_framework import status
from rbac.models import UserProfile
from apps.rbac.serializers.user_serializer import UserProfileSerializer
from rbac.utils.init_permission_menu import init_permission, init_menu

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserLoginView(APIView):
    '''
    用户登录token认证
    '''
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return JsonResponse(data={'token': token}, code=200, msg="success", status=status.HTTP_200_OK)
        else:
            return JsonResponse(code=400, msg="用户名或密码错误", status=status.HTTP_400_BAD_REQUEST)


class UserInfoView(APIView):
    '''
    获取用户信息，权限信息，菜单信息，前端可直接渲染
    '''
    def get(self, request):
        token = request.GET.get('token')
        token_info = jwt_decode_handler(token)
        user_obj = UserProfile.objects.filter(username=token_info['username']).first()
        permission_list = init_permission(request, user_obj)
        menu_list = init_menu(request, user_obj)
        data = {
            'id': user_obj.id,
            'username': user_obj.username,
            'name': user_obj.name,
            'email': user_obj.email,
            'image': request._request._current_scheme_host + '/media/' + str(user_obj.image),
            'is_active': user_obj.is_active,
            'permission': permission_list,
            'menus': menu_list
        }
        return JsonResponse(data=data, msg="success", code=200, status=status.HTTP_200_OK)


class UserProfileView(CustomViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (CustomRbacPermission,)
