import requests


class ExcelField:
    Id = '0'
    first_menu = '1'
    second_menu = '2'
    tab = '3'
    test_point = '4'
    pre = '5'
    url = '6'
    request_method = '7'
    header = '8'
    case_depend = '9'
    data = '10'
    expect = '11'
    result = '12'
    run = '13'


def get_id():
    return ExcelField.Id


def get_first_menu():
    return ExcelField.first_menu


def get_second_menu():
    return ExcelField.second_menu


def get_tab():
    return ExcelField.tab


def get_pre():
    return ExcelField.pre


def get_url():
    return ExcelField.url


def get_request_method():
    return ExcelField.request_method


def get_header():
    return ExcelField.header


def get_case_depend():
    return ExcelField.case_depend


def get_data():
    return ExcelField.data


def get_expect():
    return ExcelField.expect


def get_result():
    return ExcelField.result


def get_run():
    return ExcelField.run


'''
酒吧登录的header
'''


# def get_login_header_value():
#     header = {
#             'Content-Type': 'application/json'
#         }
#     return header


# # 酒吧获取key的值
# def get_pc_key(user):
#     # login_url = 'http://berry-server.wegui.cn/auth/login/'
#     login_url = 'https://api.dawanplus.com/auth/login/'
#
#     data_order = {
#         "username": user,
#         "email": "",
#         "password": "dxs123456"
#     }
#
#     login_headers = {
#         'Content-Type': 'application/json'
#     }
#
#     login = requests.post(login_url, json=data_order, headers=login_headers)
#
#     pc_key = login.json()['key']
#     csrf = login.cookies.get('csrftoken')
#
#     res_dict = dict()
#     res_dict['pc_key'] = pc_key
#     res_dict['csrf'] = csrf
#
#     return res_dict
#
#
# # 酒吧返回带key的header
# def pc_headers(user):
#
#     pc_header = {
#         'Content-Type': 'application/json',
#         'Authorization': 'Token ' + get_pc_key(user).get('pc_key'),
#         'X-CSRFToken': get_pc_key(user).get('csrf')
#     }
#
#     return pc_header


'''
小铁登录的header
'''


def get_login_header_value():
    header = {
            'Content-Type': 'application/json',
            'Xi-App-Id': '0a8020002101b2ddc7626fca179adf70'
        }
    return header


def get_pc_key(user):
    login_url = 'http://debug2.wegui.cn/v1/login'
    data_order = {
        "username": user,
        "password": "abc123"
    }
    login_headers = {
        'Content-Type': 'application/json',
        'Xi-App-Id': '0a8020002101b2ddc7626fca179adf70'
    }
    login = requests.post(login_url, json=data_order, headers=login_headers)
    pc_sessionToken = login.json()['sessionToken']
    return pc_sessionToken


def pc_headers(user):
    pc_header = {
        'Content-Type': 'application/json',
        'Xi-App-Id': '0a8020002101b2ddc7626fca179adf70',
        'Xi-Session-Token': get_pc_key(user)
    }
    return pc_header


def wx_headers():
    wx_header = {
        'Content-Type': 'application/json',
        'Xi-App-Id': '0a8020002101b2ddc7626fca179adf70',
        'Xi-Session-Token': 'r:5a0f5337d64ab50dd3236e59b780b49e'
    }
    return wx_header