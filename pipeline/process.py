"""
process data
"""
import os
from abc import ABC
from typing import ClassVar


def process_data_action(config):
    def action_func(config, inputs):
        # inputs is now a Map[string][Generator], because it is saved as `pkl` file from 'post_build_data`
        gene = inputs['post_data']
        env = config['env']
        lines = []
        for l in gene():
            lines.append(l)
        lines.insert(
            0, 'I am the line inserted by `process_data_action`: {}'.format(env))
        # and return a model
        return {'processed_data': lines}
    return action_func


class ProcessDataComponent(ABC):
    ACTION_DICT: ClassVar = {'process_data': process_data_action}
