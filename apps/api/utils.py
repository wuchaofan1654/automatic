# -*- coding: utf-8 -*-
"""
Create by sandy at 16:17 21/04/2022
Description: ToDo
"""

import json

import logging

logger = logging.getLogger(__name__)


def import_api_by_file(file_path) -> list:
    try:
        content = json.loads(open(file_path, 'rb').read())
        entries = content['log']['entries']

        def get_params(entry, params=None):
            if entry['request']['method'] == 'POST':
                params = entry['request']['postData']['params']

            elif entry['request']['method'] == 'GET':
                params = entry['request']['queryString']

            return params and {param['name']: param['value'] for param in params} or {}

        return [
            {
                "method": entry['request']['method'],
                "url": entry['request']['url'],
                "params": get_params(entry)
            } for entry in entries]

    except Exception as error:
        logger.exception(error)
        return []


if __name__ == '__main__':
    _file = '/Users/wuchaofan/Documents/github/automatic/media/system/2022-04-21/cacf8c51-6f1e-4649-8b9b-52b0ba47a8e5.har'
    results = import_api_by_file(_file)
    print(results)
