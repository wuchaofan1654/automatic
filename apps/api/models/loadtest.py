# -*- coding: utf-8 -*-
"""
Create by sandy at 16:52 18/04/2022
Description: ToDo
"""
from frames.models import BaseModel


class Loadtest(BaseModel):
    apis = ''
    report = ''
    start_datetime = ''
    end_datetime = ''

