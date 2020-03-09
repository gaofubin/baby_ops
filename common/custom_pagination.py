# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 4:02 下午
# @Author  : all is well
# @File    : custom_pagination.py
# @Software: PyCharm

from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from collections import OrderedDict


class LargeResultsSetPagination(LimitOffsetPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000

    def get_paginated_response(self, data):
        code = 200
        msg = 'success'
        if not data:
            code = 404
            msg = "Data Not Found"

        return Response(OrderedDict([
            ('meta', {
                'code': code,
                'msg': msg,
                'count': self.count,
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            }
             ),
            ('data', data),
        ]))
