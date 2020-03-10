# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 10:35 下午
# @Author  : all is well
# @File    : init_permission_menu.py
# @Software: PyCharm


def init_permission(request, user_obj):
    """
    初始化用户权限, 写入session
    """
    permission_list = []
    user_permission_obj = user_obj.roles.values('permissions__method').distinct()
    for perm in user_permission_obj:
        permission_list.append(perm['permissions__method'])
    return permission_list


def init_menu(request, user_obj):
    """
    初始化用户菜单信息，写入session
    """
    user_menu_obj = user_obj.roles.values('menus__id',
                                          'menus__name',
                                          'menus__path',
                                          'menus__icon',
                                          'menus__is_frame',
                                          'menus__is_show',
                                          'menus__component',
                                          'menus__parent').distinct()
    menu_dict = {}
    for menu in user_menu_obj:
        # 判断是否为最外部
        if menu['menus__parent'] is None:
            parent_menu_format = {
                'id': menu['menus__id'],
                'name': menu['menus__name'],
                'path': "/{}".format(menu['menus__path']),
                'component': menu['menus__component'],
                'redirect': 'noredirect',
                'alwaysShow': True,
                'meta': {
                    'title': menu['menus__name'],
                    'icon': menu['menus__icon']
                },
                'parent_id': menu['menus__parent'],
                'children': []
            }
            menu_dict[menu['menus__id']] = parent_menu_format
        else:
            children_menu_format = {
                'id': menu['menus__id'],
                'name': menu['menus__name'],
                'path': menu['menus__path'],
                'component': 'Layout' if menu['menus__is_frame'] else menu['menus__component'],
                'meta': {
                    'title': menu['menus__name'],
                    'icon': menu['menus__icon'],
                    'noCache': False if menu['menus__is_show'] else True
                },
                'hidden': False if menu['menus__is_show'] else True,
                'parent_id': menu['menus__parent'],
                'children': []
            }
            menu_dict[menu['menus__id']] = children_menu_format

    children_id_list = []
    for key, val in menu_dict.items():
        parent_id = val['parent_id']
        if parent_id:
            children_id_list.append(key)
            menu_dict[parent_id]['children'].append(val)

    for children_id in children_id_list:
        menu_dict.pop(children_id)


    menu_list = []
    for v in menu_dict.values():
        menu_list.append(v)
    return menu_list

