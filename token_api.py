#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   token_api.py    
@Contact :   zqqqqz2000@sina.cn
@License :   (C)Copyright 2017-2021 ICCD

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/1 19:05   ICCD       1.0         None
"""
from typing import Dict, Union

import requests

from config import APIKEY


def get_token_data_from_server(token_name: str) -> Dict:
    url = f"https://services.tokenview.com/vipapi/coin/marketInfo/{token_name}?apikey=" + APIKEY
    r = requests.get(url)
    json_data = r.json()
    if json_data['code'] != 1:
        raise Exception(json_data['msg'])
    return json_data['data']


def get_token_data_multi_from_server(token_name: str, type_: str = 'daily_marketcap') -> Dict:
    url = f"https://services.tokenview.com/vipapi/chart/{token_name}/{type_}?splice=100&apikey={APIKEY}"
    r = requests.get(url)
    json_data = r.json()
    return json_data['data']


def get_btc_addr_data_from_server(pub_addr: str) -> Dict:
    url = f"https://services.tokenview.com/vipapi/addr/b/btc/{pub_addr}?apikey=" + APIKEY
    r = requests.get(url)
    json_data = r.json()
    if json_data['code'] != 1:
        raise Exception(json_data['msg'])
    return json_data


if __name__ == '__main__':
    print(get_token_data_from_server("btc"))
