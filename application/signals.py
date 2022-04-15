# -*- coding: utf-8 -*-
"""
Create by sandy at 13:41 18/03/2022
Description: ToDo
"""

from django.dispatch import Signal


# 埋点相关信号
# mitmproxy截取到符合条件的url触发信号
mitmproxy_matched_signal = Signal(providing_args=['request_data', 'group_name'])
# 保存埋点触发信号
save_point_signal = Signal(providing_args=['point'])
# 检查埋点触发信号
check_point_signal = Signal(providing_args=['point'])



