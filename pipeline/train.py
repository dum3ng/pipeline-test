from __future__ import print_function
import os
import warnings
import sys
from abc import ABC
from typing import ClassVar

import numpy as np
from sklearn.linear_model import LogisticRegression

import mlflow
import mlflow.sklearn


def train_action(config):
    def action_func(config, inputs):
        X = np.array([-2, -1, 0, 1, 2, 1]).reshape(-1, 1)
        y = np.array([0, 0, 1, 1, 1, 0])
        lr = LogisticRegression()
        lr.fit(X, y)
        score = lr.score(X, y)
        print("Score: %s" % score)
        mlflow.log_metric("score", score)
        mlflow.sklearn.log_model(lr, "sk_models")
        print("Model saved in run %s" % mlflow.active_run().info.run_uuid)
        return {}
    return action_func


def test_action(config):
    def action_func(config, inputs):
        sk_model = mlflow.sklearn.load_model(inputs['model'])
        print('model loaded successfully in test model action.')
        return {}
    return action_func


class TrainComponent(ABC):
    ACTION_DICT: ClassVar = {'train': train_action,
                             'test_model': test_action}
