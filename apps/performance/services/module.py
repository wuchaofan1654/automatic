# -*- coding: utf-8 -*-
"""
Create by sandy at 11:10 24/04/2022
Description: ToDo
"""


class ModuleDataFitLineChart(object):

    def __init__(self, modules):
        self.modules = modules
        self.xAsia = set()
        self.yAsia = {}
        self.result = {}
        self.add_xAsia()
        self.add_yAsia()

    def add_xAsia(self):
        for module in self.modules.values():
            [self.xAsia.add(version) for version in module.keys()]

    def add_yAsia(self):
        self.xAsia = sorted(self.xAsia)
        self.result['xAsia'] = self.xAsia

        for key, value in self.modules.items():
            self.yAsia[key] = []
            for version in self.xAsia:
                element = version in value.keys() and value[version] or 0
                self.yAsia[key].append(element)

        self.result['yAsia'] = self.yAsia


if __name__ == '__main__':
    m = ModuleDataFitLineChart()
    print(m.result)

