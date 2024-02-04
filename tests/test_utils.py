from src.utils import *
import pytest


def test_get_executed_operations():
    assert json_EXECUTED_operations([{"state": "EXECUTED"}]) == [{"state": "EXECUTED"}]
    assert json_EXECUTED_operations([{}]) == []


def test_sort_date_operations():
    assert sort_date_operations([{"date": "2018-03-23T10:45:06.972075"},
                                 {"date": "2019-04-04T23:20:05.206878"},
                                 {"date": "2018-12-20T16:43:26.929246"},
                                 {"date": "2019-03-23T01:09:46.296404"},
                                 {"date": "2019-07-12T20:41:47.882230"}]) == [{"date": "2019-07-12T20:41:47.882230"},
                                                                              {"date": "2019-04-04T23:20:05.206878"},
                                                                              {"date": "2019-03-23T01:09:46.296404"},
                                                                              {"date": "2018-12-20T16:43:26.929246"},
                                                                              {"date": "2018-03-23T10:45:06.972075"}]



def test_change_date():
    assert change_date([{"date": "2019-07-12T20:41:47.882230"}]) == ['12.07.2019']


def test_mask_card_number():
    assert mask_card_number([{"from": "Visa Classic 2842878893689012",
                              "description": "Перевод организации"}]) == ['Visa Classic 2842 87** **** 9012']
    assert mask_card_number([{"from": "Maestro 7810846596785568",
                              "description": "Перевод организации"}]) == ['Maestro 7810 84** **** 5568']

def test_mask_amount_number():
    assert mask_amount_number([{"to": "Счет 46765464282437878125"}]) == ['**7812']