"""
从数据库中获取标注数据
"""
import os
from abc import ABC
from typing import ClassVar


def build_data_action(config):
    def action_func(config, inputs):
        # return a dict object, should be saved as json file
        return {'data': {'name': 'dumeng', 'title': 'frontend engineer'}}
    return action_func


def post_build_data_action(config):
    def action_func(config, inputs):
        # return a Iterable, should be saved as a .pkl file
        l = [f'line {x} \n' for x in range(10)]
        return {'post_data': l}
    return action_func


class BuildDataComponent(ABC):
    ACTION_DICT: ClassVar = {'build_data': build_data_action,
                             'post_build_data': post_build_data_action}
