import logging

import allure


def step(title: str):
    return allure.step(title)


def attach(name: str, msg: str):
    allure.attach(msg, name=name)
