# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 12:05 下午
# @Author  : all is well
# @File    : urls.py
# @Software: PyCharm

from django.urls import path, include
from rest_framework import routers
from rbac.views import user

router = routers.SimpleRouter()
router.register('users', user.UserProfileView, basename='users')

urlpatterns = [
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/', include(router.urls)),
    path(r'auth/login/', user.UserLoginView.as_view()),
    path(r'auth/userinfo/', user.UserInfoView.as_view()),
]

