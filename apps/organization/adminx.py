# !/usr/bin/python
# -*-coding:utf-8-*-
__author__ = 'mtianyan'
__date__ = '2018-12-24 13:40'
"""
            　┏┓　　　┏┓+ +
  　　　　　　　┏┛┻━━━┛┻┓ + +
  　　　　　　　┃　　　　　　　┃ 　
  　　　　　　　┃　　　━　　　┃ ++ + + +
  　　　　　　 ████━████ ┃+
  　　　　　　　┃　　　　　　　┃ +
  　　　　　　　┃　　　┻　　　┃
  　　　　　　　┃　　　　　　　┃ + +
  　　　　　　　┗━┓　　　┏━┛
  　　　　　　　　　┃　　　┃　　　　　　　　　　　
  　　　　　　　　　┃　　　┃ + + + +
  　　　　　　　　　┃　　　┃　　　　Code is far away from bug with the animal protecting　　　　　　　
  　　　　　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
  　　　　　　　　　┃　　　┃
  　　　　　　　　　┃　　　┃　　+　　　　　　　　　
  　　　　　　　　　┃　 　　┗━━━┓ + +
  　　　　　　　　　┃ 　　　　　　　┣┓
  　　　　　　　　　┃ 　　　　　　　┏┛
  　　　　　　　　　┗┓┓┏━┳┓┏┛ + + + +
  　　　　　　　　　　┃┫┫　┃┫┫
  　　　　　　　　　　┗┻┛　┗┻┛+ + + +
"""
import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    """机构所在城市的admin类"""
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    """课程机构信息管理器"""
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'city__name', 'address', 'add_time']


class TeacherAdmin(object):
    """讲师信息管理类"""
    list_display = ['name', 'org', 'work_years', 'work_company', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company']
    list_filter = ['org__name', 'name', 'work_years', 'work_company', 'click_nums', 'fav_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
