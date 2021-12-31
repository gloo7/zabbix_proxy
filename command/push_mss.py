import requests
from datetime import datetime, timedelta


url = "http://10.76.138.38/zabbix/api_jsonrpc.php"
headers = {'Content-Type': 'application/json-rpc'}
item_mapping = {
    62766: {'hostname': 'HUZGS21', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_HUZPOOL_P2'},
    62767: {'hostname': 'HUZGS22', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_HUZPOOL_P2'},
    62768: {'hostname': 'HUZGS23', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_HUZPOOL_P2'},
    62769: {'hostname': 'HUZGS24', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_HUZPOOL_P2'},
    62777: {'hostname': 'HZGS31', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL1_P2'},
    62778: {'hostname': 'HZGS32', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL1_P2'},
    62779: {'hostname': 'HZGS33', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL1_P2'},
    62780: {'hostname': 'HZGS34', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL1_P2'},
    62781: {'hostname': 'HZGS35', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL1_P2'},
    62794: {'hostname': 'HZGS1', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL3_P2'},
    62795: {'hostname': 'HZGS10', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL3_P2'},
    62796: {'hostname': 'HZGS13', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL3_P2'},
    62797: {'hostname': 'HZGS15', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL3_P2'},
    62789: {'hostname': 'HZGS22', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL2_P2'},
    62790: {'hostname': 'HZGS36', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL2_P2'},
    62791: {'hostname': 'HZGS37', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL2_P2'},
    62792: {'hostname': 'HZGS38', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL2_P2'},
    62793: {'hostname': 'HZGS39', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL2_P2'},
    62804: {'hostname': 'JIHGS1', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL2_P2'},
    62798: {'hostname': 'JIHGS2', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL1_P2'},
    62805: {'hostname': 'JIHGS3', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL2_P2'},
    62799: {'hostname': 'JIHGS4', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL1_P2'},
    62806: {'hostname': 'JIHGS5', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL2_P2'},
    62800: {'hostname': 'JIHGS6', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL1_P2'},
    62801: {'hostname': 'JIHGS7', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL1_P2'},
    62807: {'hostname': 'JIHGS8', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL2_P2'},
    62802: {'hostname': 'JIHGS9', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL1_P2'},
    62803: {'hostname': 'JIHGS10', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL1_P2'},
    62808: {'hostname': 'JIHGS11', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL2_P2'},
    62809: {'hostname': 'JIHGS12', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL2_P2'},
    62810: {'hostname': 'JXIGS21', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_JXIPOOL_P2'},
    62811: {'hostname': 'JXIGS22', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_JXIPOOL_P2'},
    62812: {'hostname': 'JXIGS23', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_JXIPOOL_P2'},
    62813: {'hostname': 'JXIGS24', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_JXIPOOL_P2'},
    62814: {'hostname': 'JXIGS25', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_JXIPOOL_P2'},
    62815: {'hostname': 'LSHGS1', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_LSHPOOL1_P2'},
    62816: {'hostname': 'LSHGS2', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_LSHPOOL1_P2'},
    62817: {'hostname': 'LSHGS4', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_LSHPOOL1_P2'},
    62818: {'hostname': 'LSHGS5', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_LSHPOOL1_P2'},
    62819: {'hostname': 'QUZGS1', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_QUZPOOL1_P2'},
    62820: {'hostname': 'QUZGS2', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_QUZPOOL1_P2'},
    62821: {'hostname': 'QUZGS3', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_QUZPOOL1_P2'},
    62822: {'hostname': 'QUZGS4', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_QUZPOOL1_P2'},
    62823: {'hostname': 'SHXGS1', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_SHXPOOL1_P2'},
    62824: {'hostname': 'SHXGS2', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_SHXPOOL1_P2'},
    62825: {'hostname': 'SHXGS4', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_SHXPOOL1_P2'},
    62826: {'hostname': 'SHXGS5', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_SHXPOOL1_P2'},
    62827: {'hostname': 'SHXGS6', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_SHXPOOL1_P2'},
    62828: {'hostname': 'SHXGS7', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_SHXPOOL1_P2'},
    62829: {'hostname': 'SHXGS8', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_SHXPOOL1_P2'},
    62830: {'hostname': 'SHXGS9', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_SHXPOOL1_P2'},
    62831: {'hostname': 'TZHGS21', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_TZHPOOL_P2'},
    62832: {'hostname': 'TZHGS22', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_TZHPOOL_P2'},
    62833: {'hostname': 'TZHGS23', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_TZHPOOL_P2'},
    62834: {'hostname': 'TZHGS24', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_TZHPOOL_P2'},
    62835: {'hostname': 'TZHGS25', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_TZHPOOL_P2'},
    62836: {'hostname': 'TZHGS26', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_TZHPOOL_P2'},
    62837: {'hostname': 'WZHGS30', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_WZHPOOL_P2'},
    62838: {'hostname': 'WZHGS31', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_WZHPOOL_P2'},
    62839: {'hostname': 'WZHGS32', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_WZHPOOL_P2'},
    62840: {'hostname': 'WZHGS33', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_WZHPOOL_P2'},
    62841: {'hostname': 'WZHGS34', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_WZHPOOL_P2'},
    62842: {'hostname': 'WZHGS35', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_WZHPOOL_P2'},
    62843: {'hostname': 'WZHGS36', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_WZHPOOL_P2'},
    62844: {'hostname': 'WZHGS37', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_WZHPOOL_P2'},
    62845: {'hostname': 'WZHGS38', 'indicators_name': 'VLR存储用户数', 'group': 'HXW_GENERAL_HW_MSC_WZHPOOL_P2'},
    329653: {'hostname': 'HUZGS21', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_HUZPOOL_P2'},
    329654: {'hostname': 'HUZGS22', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_HUZPOOL_P2'},
    329655: {'hostname': 'HUZGS23', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_HUZPOOL_P2'},
    329656: {'hostname': 'HUZGS24', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_HUZPOOL_P2'},
    329664: {'hostname': 'HZGS31', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL1_P2'},
    329665: {'hostname': 'HZGS32', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL1_P2'},
    329666: {'hostname': 'HZGS33', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL1_P2'},
    329667: {'hostname': 'HZGS34', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL1_P2'},
    329668: {'hostname': 'HZGS35', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL1_P2'},
    329681: {'hostname': 'HZGS1', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL3_P2'},
    329682: {'hostname': 'HZGS10', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL3_P2'},
    329683: {'hostname': 'HZGS13', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL3_P2'},
    329684: {'hostname': 'HZGS15', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL3_P2'},
    329676: {'hostname': 'HZGS22', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL2_P2'},
    329677: {'hostname': 'HZGS36', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL2_P2'},
    329678: {'hostname': 'HZGS37', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL2_P2'},
    329679: {'hostname': 'HZGS38', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL2_P2'},
    329680: {'hostname': 'HZGS39', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_HZPOOL2_P2'},
    329691: {'hostname': 'JIHGS1', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL2_P2'},
    329685: {'hostname': 'JIHGS2', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL1_P2'},
    329692: {'hostname': 'JIHGS3', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL2_P2'},
    329686: {'hostname': 'JIHGS4', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL1_P2'},
    329693: {'hostname': 'JIHGS5', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL2_P2'},
    329687: {'hostname': 'JIHGS6', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL1_P2'},
    329688: {'hostname': 'JIHGS7', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL1_P2'},
    329694: {'hostname': 'JIHGS8', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL2_P2'},
    329689: {'hostname': 'JIHGS9', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL1_P2'},
    329690: {'hostname': 'JIHGS10', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL1_P2'},
    329695: {'hostname': 'JIHGS11', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL2_P2'},
    329696: {'hostname': 'JIHGS12', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_JIHPOOL2_P2'},
    329697: {'hostname': 'JXIGS21', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_JXIPOOL_P2'},
    329698: {'hostname': 'JXIGS22', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_JXIPOOL_P2'},
    329699: {'hostname': 'JXIGS23', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_JXIPOOL_P2'},
    329700: {'hostname': 'JXIGS24', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_JXIPOOL_P2'},
    329701: {'hostname': 'JXIGS25', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_JXIPOOL_P2'},
    329702: {'hostname': 'LSHGS1', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_LSHPOOL1_P2'},
    329703: {'hostname': 'LSHGS2', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_LSHPOOL1_P2'},
    329704: {'hostname': 'LSHGS4', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_LSHPOOL1_P2'},
    329705: {'hostname': 'LSHGS5', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_LSHPOOL1_P2'},
    329706: {'hostname': 'QUZGS1', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_QUZPOOL1_P2'},
    329707: {'hostname': 'QUZGS2', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_QUZPOOL1_P2'},
    329708: {'hostname': 'QUZGS3', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_QUZPOOL1_P2'},
    329709: {'hostname': 'QUZGS4', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_QUZPOOL1_P2'},
    329710: {'hostname': 'SHXGS1', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_SHXPOOL1_P2'},
    329711: {'hostname': 'SHXGS2', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_SHXPOOL1_P2'},
    329712: {'hostname': 'SHXGS4', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_SHXPOOL1_P2'},
    329713: {'hostname': 'SHXGS5', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_SHXPOOL1_P2'},
    329714: {'hostname': 'SHXGS6', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_SHXPOOL1_P2'},
    329715: {'hostname': 'SHXGS7', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_SHXPOOL1_P2'},
    329716: {'hostname': 'SHXGS8', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_SHXPOOL1_P2'},
    329717: {'hostname': 'SHXGS9', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_SHXPOOL1_P2'},
    329718: {'hostname': 'TZHGS21', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_TZHPOOL_P2'},
    329719: {'hostname': 'TZHGS22', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_TZHPOOL_P2'},
    329720: {'hostname': 'TZHGS23', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_TZHPOOL_P2'},
    329721: {'hostname': 'TZHGS24', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_TZHPOOL_P2'},
    329722: {'hostname': 'TZHGS25', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_TZHPOOL_P2'},
    329723: {'hostname': 'TZHGS26', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_TZHPOOL_P2'},
    329724: {'hostname': 'WZHGS30', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_WZHPOOL_P2'},
    329725: {'hostname': 'WZHGS31', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_WZHPOOL_P2'},
    329726: {'hostname': 'WZHGS32', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_WZHPOOL_P2'},
    329727: {'hostname': 'WZHGS33', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_WZHPOOL_P2'},
    329728: {'hostname': 'WZHGS34', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_WZHPOOL_P2'},
    329729: {'hostname': 'WZHGS35', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_WZHPOOL_P2'},
    329730: {'hostname': 'WZHGS36', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_WZHPOOL_P2'},
    329731: {'hostname': 'WZHGS37', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_WZHPOOL_P2'},
    329732: {'hostname': 'WZHGS38', 'indicators_name': 'VLR容量', 'group': 'HXW_GENERAL_HW_MSC_WZHPOOL_P2'},
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
print(time_from.timestamp())
print(time_till.timestamp())


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
                "table": "mms_hw",
                "fields": ['hostname', 'indicators_name', 'indicators_value', 'time', 'group'],
            }
        ]
    )
    return obj
