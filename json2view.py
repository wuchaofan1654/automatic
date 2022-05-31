# -*- coding: utf-8 -*-
"""
Create by sandy at 15:38 26/04/2022
Description: ToDo
"""

from json2html import json2html


response = {
    "code": 200,
    "data": {
        "count": 2,
        "next": None,
        "previous": None,
        "results": [
            {
                "id": 1,
                "interval_list": {
                    "id": 1,
                    "every": 5,
                    "period": "seconds"
                },
                "crontab_list": {},
                "name": "定时获取系统监控信息",
                "task": "apps.monitor.tasks.get_monitor_info",
                "args": "[]",
                "kwargs": "{}",
                "queue": None,
                "exchange": None,
                "routing_key": None,
                "headers": "{}",
                "priority": None,
                "expires": None,
                "expire_seconds": None,
                "one_off": False,
                "start_time": None,
                "enabled": False,
                "last_run_at": None,
                "total_run_count": 0,
                "date_changed": "2022-03-28T15:50:47.034558+08:00",
                "description": "",
                "interval": 1,
                "crontab": None,
                "solar": None,
                "clocked": None
            },
            {
                "id": 2,
                "interval_list": {},
                "crontab_list": {
                    "id": 1,
                    "minute": "0",
                    "hour": "1",
                    "day_of_week": "*",
                    "day_of_month": "*",
                    "month_of_year": "*"
                },
                "name": "定时清理多余-系统监控信息",
                "task": "apps.monitor.tasks.clean_surplus_monitor_info",
                "args": "[]",
                "kwargs": "{}",
                "queue": None,
                "exchange": None,
                "routing_key": None,
                "headers": "{}",
                "priority": None,
                "expires": None,
                "expire_seconds": None,
                "one_off": False,
                "start_time": None,
                "enabled": True,
                "last_run_at": "2022-04-25T17:00:00.003314+08:00",
                "total_run_count": 3,
                "date_changed": "2022-04-26T01:02:35.446115+08:00",
                "description": "",
                "interval": None,
                "crontab": 1,
                "solar": None,
                "clocked": None
            }
        ]
    },
    "msg": "success",
    "status": "success"
}


html = json2html.convert(response)
print(html)


