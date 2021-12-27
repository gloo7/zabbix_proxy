import requests
from datetime import datetime, timedelta


url = "http://10.76.138.38/zabbix/api_jsonrpc.php"
headers = {'Content-Type': 'application/json-rpc'}
item_mapping = {
    52514: {'hostname': 'HZISBG04BHW', 'group': 'HXW_GENERAL_HW_CSCF_P2', 'indicators_name': 'S-CSCF 注册用户数'},
    52515: {'hostname': 'HZISBG05BHW', 'group': 'HXW_GENERAL_HW_CSCF_P2', 'indicators_name': 'S-CSCF 注册用户数'},
    52516: {'hostname': 'HZISBG06BHW', 'group': 'HXW_GENERAL_HW_CSCF_P2', 'indicators_name': 'S-CSCF 注册用户数'},
    52517: {'hostname': 'HZISBG08BHW', 'group': 'HXW_GENERAL_HW_CSCF_P2', 'indicators_name': 'S-CSCF 注册用户数'},
    52518: {'hostname': 'HZISBG07BHW', 'group': 'HXW_GENERAL_HW_CSCF_P2', 'indicators_name': 'S-CSCF 注册用户数'},
    52519: {'hostname': 'HZISBG09BHW', 'group': 'HXW_GENERAL_HW_CSCF_P2', 'indicators_name': 'S-CSCF 注册用户数'},
    52520: {'hostname': 'HZISBG10BHW', 'group': 'HXW_GENERAL_HW_CSCF_P2', 'indicators_name': 'S-CSCF 注册用户数'},
    52521: {'hostname': 'HZISBG11BHW', 'group': 'HXW_GENERAL_HW_CSCF_P2', 'indicators_name': 'S-CSCF 注册用户数'},
    52522: {'hostname': 'HZISBG12BHW', 'group': 'HXW_GENERAL_HW_CSCF_P2', 'indicators_name': 'S-CSCF 注册用户数'},
    52523: {'hostname': 'HZISBG13BHW', 'group': 'HXW_GENERAL_HW_CSCF_P2', 'indicators_name': 'S-CSCF 注册用户数'},
    52524: {'hostname': 'HZISBG14BHW', 'group': 'HXW_GENERAL_HW_CSCF_P2', 'indicators_name': 'S-CSCF 注册用户数'},
    52525: {'hostname': 'HZISBG15BHW', 'group': 'HXW_GENERAL_HW_CSCF_P2', 'indicators_name': 'S-CSCF 注册用户数'},
    71066: {'hostname': 'HZPSBC01BHW', 'group': 'HXW_GENERAL_HW_PSBC_P2', 'indicators_name': '注册用户数'},
    71067: {'hostname': 'HZPSBC02BHW', 'group': 'HXW_GENERAL_HW_PSBC_P2', 'indicators_name': '注册用户数'},
    71068: {'hostname': 'HZPSBC03BHW', 'group': 'HXW_GENERAL_HW_PSBC_P2', 'indicators_name': '注册用户数'},
    71069: {'hostname': 'HZPSBC04BHW', 'group': 'HXW_GENERAL_HW_PSBC_P2', 'indicators_name': '注册用户数'},
    71070: {'hostname': 'HZPSBC09BHW', 'group': 'HXW_GENERAL_HW_PSBC_P2', 'indicators_name': '注册用户数'},
    71071: {'hostname': 'HZPSBC10BHW', 'group': 'HXW_GENERAL_HW_PSBC_P2', 'indicators_name': '注册用户数'},
    71072: {'hostname': 'HZPSBC11BHW', 'group': 'HXW_GENERAL_HW_PSBC_P2', 'indicators_name': '注册用户数'},
    71073: {'hostname': 'HZPSBC12BHW', 'group': 'HXW_GENERAL_HW_PSBC_P2', 'indicators_name': '注册用户数'},
    71074: {'hostname': 'HZPSBC13BHW', 'group': 'HXW_GENERAL_HW_PSBC_P2', 'indicators_name': '注册用户数'},
    71075: {'hostname': 'HZPSBC14BHW', 'group': 'HXW_GENERAL_HW_PSBC_P2', 'indicators_name': '注册用户数'},
    71076: {'hostname': 'HZPSBC15BHW', 'group': 'HXW_GENERAL_HW_PSBC_P2', 'indicators_name': '注册用户数'},
    71077: {'hostname': 'HZPSBC16BHW', 'group': 'HXW_GENERAL_HW_PSBC_P2', 'indicators_name': '注册用户数'},
    283107: {'hostname': 'HZPSBC17BHW', 'group': 'HXW_GENERAL_HW_PSBC_P2', 'indicators_name': '注册用户数'},
    283172: {'hostname': 'HZPSBC18BHW', 'group': 'HXW_GENERAL_HW_PSBC_P2', 'indicators_name': '注册用户数'},
    283237: {'hostname': 'HZPSBC19BHW', 'group': 'HXW_GENERAL_HW_PSBC_P2', 'indicators_name': '注册用户数'},
    283302: {'hostname': 'HZPSBC20BHW', 'group': 'HXW_GENERAL_HW_PSBC_P2', 'indicators_name': '注册用户数'},
    30432: {'hostname': 'HZVOLTEAS01BHW', 'group': 'HXW_GENERAL_HW_ATS_P2', 'indicators_name': 'ATS 注册用户数'},
    30433: {'hostname': 'HZVOLTEAS02BHW', 'group': 'HXW_GENERAL_HW_ATS_P2', 'indicators_name': 'ATS 注册用户数'},
    30434: {'hostname': 'HZVOLTEAS03BHW', 'group': 'HXW_GENERAL_HW_ATS_P2', 'indicators_name': 'ATS 注册用户数'},
    30435: {'hostname': 'HZVOLTEAS04BHW', 'group': 'HXW_GENERAL_HW_ATS_P2', 'indicators_name': 'ATS 注册用户数'},
    30436: {'hostname': 'HZVOLTEAS05BHW', 'group': 'HXW_GENERAL_HW_ATS_P2', 'indicators_name': 'ATS 注册用户数'},
    30437: {'hostname': 'HZVOLTEAS06BHW', 'group': 'HXW_GENERAL_HW_ATS_P2', 'indicators_name': 'ATS 注册用户数'},
    30438: {'hostname': 'HZVOLTEAS07BHW', 'group': 'HXW_GENERAL_HW_ATS_P2', 'indicators_name': 'ATS 注册用户数'},
    30439: {'hostname': 'HZVOLTEAS08BHW', 'group': 'HXW_GENERAL_HW_ATS_P2', 'indicators_name': 'ATS 注册用户数'},
    30440: {'hostname': 'HZVOLTEAS09BHW', 'group': 'HXW_GENERAL_HW_ATS_P2', 'indicators_name': 'ATS 注册用户数'},
    30441: {'hostname': 'HZVOLTEAS10BHW', 'group': 'HXW_GENERAL_HW_ATS_P2', 'indicators_name': 'ATS 注册用户数'},
    30442: {'hostname': 'HZVOLTEAS11BHW', 'group': 'HXW_GENERAL_HW_ATS_P2', 'indicators_name': 'ATS 注册用户数'},
    30443: {'hostname': 'HZVOLTEAS12BHW', 'group': 'HXW_GENERAL_HW_ATS_P2', 'indicators_name': 'ATS 注册用户数'},
}


def get_auth() -> dict:
    login_info = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": "dev_lj",
            "password": "zJIct189080*)"
        },
        "id": 1,
        "auth": None
    }
    resp = requests.post(url, json=login_info, headers={'Content-Type': 'application/json-rpc'})
    assert resp.status_code == 200, "login error"
    result = resp.json()

    return dict(auth=result['result'], id=result['id'])


now = datetime.now()
time_till = now - timedelta(minutes=now.minute, seconds=now.second, microseconds=now.microsecond)
time_from = time_till - timedelta(hours=1)

print(time_till, time_from)

data = {
    "jsonrpc": "2.0",
    "method": "history.get",
    "params": {
        "output": "extend",
        "history": 0,
        "itemids": list(item_mapping.keys()),
        "sortfield": "clock",
        "time_from": time_from.timestamp(),
        "time_till": time_till.timestamp(),
        "sortorder": "DESC",
        "countOutput": True,
    }
}

data.update(get_auth())


def get_obj(*args):
    obj = dict(
        collector={
            "mode": "api",
            "url": url,
            "method": "post",
            "json_data": data,
            "headers": headers,
            "index": "result"
        },
        rewriters=[
            {
                "mode": "mapping",
                "key": "itemid",
                "mapping": item_mapping,
                "is_update": True
            },
            {
                "mode": "timestamp",
                "key": "clock",
                "fmt": "%Y-%m-%d %H:%M"
            },
            {
                "mode": "rename",
                "key": "clock",
                "new": "time",
            },
            {
                "mode": "rename",
                "key": "value",
                "new": "indicators_value",
            }
        ],
        handlers=[
            {
                "mode": "mysql",
                "host": "10.212.172.248",
                "port": 8005,
                "user": "sre@data",
                "password": "wnaEhqoYCuqSrM2c",
                "database": "report_data",
                "table": "volte_ims_hw",
                "fields": ['hostname', 'indicators_name', 'indicators_value', 'time', 'group'],
            }
        ]
    )

    return obj
