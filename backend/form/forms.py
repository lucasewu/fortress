#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wuyy

class Form(object):
    def __init__(self):
        self.value_dict = {}
        self.error_dict = {}
        self.valid_status = True

    def validate(self, request, depth=10, pre_key=""):

        self.initialize()
        self.__valid(self, request, depth, pre_key)

    def initialize(self):
        pass

    def __valid(self, form_obj, request, depth, pre_key):
        """
        验证用户表单请求的数据
        :param form_obj: Form对象（Form派生类的对象）
        :param request: Http请求上下文（用于从请求中获取用户提交的值）
        :param depth: 对Form内容的深度的支持
        :param pre_key: Html中name属性值的前缀（多层Form时，内部递归时设置，无需理会）
        :return: 是否验证通过，True：验证成功；False：验证失败
        """

        depth -= 1
        if depth < 0:
            return None
        form_field_dict = form_obj.__dict__
        for key, field_obj in form_field_dict.items():
            print
            key, field_obj
            if isinstance(field_obj, Form) or isinstance(field_obj, Field):
                if isinstance(field_obj, Form):
                    # 获取以key开头的所有的值，以参数的形式传至
                    self.__valid(field_obj, request, depth, key)
                    continue
                if pre_key:
                    key = "%s.%s" % (pre_key, key)

                if isinstance(field_obj, CheckBoxField):
                    post_value = request.get_arguments(key, None)
                elif isinstance(field_obj, FileField):
                    post_value = []
                    file_list = request.request.files.get(key, None)
                    for file_item in file_list:
                        post_value.append(file_item['filename'])
                else:
                    post_value = request.get_argument(key, None)

                print
                post_value
                # 让提交的数据 和 定义的正则表达式进行匹配
                field_obj.match(key, post_value)
                if field_obj.id_valid:
                    self.value_dict[key] = field_obj.value
                else:
                    self.error_dict[key] = field_obj.error
                    self.valid_status = False


class ListForm(object):
    def __init__(self, form_type):
        self.form_type = form_type
        self.valid_status = True
        self.value_dict = {}
        self.error_dict = {}

    def validate(self, request):
        name_list = request.request.arguments.keys() + request.request.files.keys()
        index = 0
        flag = False
        while True:
            pre_key = "[%d]" % index
            for name in name_list:
                if name.startswith(pre_key):
                    flag = True
                    break
            if flag:
                form_obj = self.form_type()
                form_obj.validate(request, depth=10, pre_key="[%d]" % index)
                if form_obj.valid_status:
                    self.value_dict[index] = form_obj.value_dict
                else:
                    self.error_dict[index] = form_obj.error_dict
                    self.valid_status = False
            else:
                break

            index += 1
            flag = False


class MainForm(Form):
    def __init__(self):
        # self.ip = IPField(required=True)
        # self.port = IntegerField(required=True)
        # self.new_ip = IPField(required=True)
        # self.second = SecondForm()
        self.fff = FileField(required=True)
        super(MainForm, self).__init__()

#
# class SecondForm(Form):
#
#     def __init__(self):
#         self.ip = IPField(required=True)
#         self.new_ip = IPField(required=True)
#
#         super(SecondForm, self).__init__()

