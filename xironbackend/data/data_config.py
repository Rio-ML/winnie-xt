import requests


class global_var:
    Id = '0'
    first_menu = '1'
    second_menu = '2'
    tab = '3'
    pre = '5'
    url = '6'
    request_way = '7'
    header = '8'
    case_depend = '9'
    data_depend = '10'
    field_depend = '11'
    data = '12'
    expect = '13'
    result = '14'
    run = '15'


def get_id():
    return global_var.Id


def get_first_menu():
    return global_var.first_menu


def get_second_menu():
    return global_var.second_menu


def get_tab():
    return global_var.tab


def get_pre():
    return global_var.pre


def get_url():
    return global_var.url


def get_request_way():
    return global_var.request_way


def get_header():
    return global_var.header


def get_case_depend():
    return global_var.case_depend


def get_data_depend():
    return global_var.data_depend


def get_field_depend():
    return global_var.field_depend


def get_data():
    return global_var.data


def get_expect():
    return global_var.expect


def get_result():
    return global_var.result


def get_run():
    return global_var.run


# 小铁登录的 header
# def get_login_header_value():
#     header = {
#             'Content-Type': 'application/json',
#             'Xi-App-Id': '0a8020002101b2ddc7626fca179adf70'
#         }
#     return header


# 小铁获取 session——token 的值
# def get_pc_session_token(user):
#     login_url = 'http://debug2.wegui.cn/v1/login'
#
#     data_order = {
#         "username": user,
#         "password": "123456"
#     }
#
#     login_headers = {
#         'Content-Type': 'application/json',
#         'Xi-App-Id': '0a8020002101b2ddc7626fca179adf70'
#     }
#
#     login = requests.post(login_url, json=data_order, headers=login_headers)
#
#     pc_SessionToken = login.json()['sessionToken']
# #     print('pc端的session值', pc_SessionToken)
#     return pc_SessionToken


# 小铁返回带 session-token 的 header
# def pc_headers(user):
#     pc_header = {
#         'Content-Type': 'application/json',
#         'Xi-App-Id': '0a8020002101b2ddc7626fca179adf70',
#         'Xi-Session-Token': get_pc_session_token(user)
#     }
#
#     return pc_header


# 酒吧登录的header
def get_login_header_value():
    header = {
            'Content-Type': 'application/json'
        }
    return header


# 酒吧获取key的值
def get_pc_key(user):
    login_url = 'http://berry-server.wegui.cn/auth/login/'

    data_order = {
        "username": user,
        "email": "",
        "password": "moternmotern"
    }

    login_headers = {
        'Content-Type': 'application/json'
    }

    login = requests.post(login_url, json=data_order, headers=login_headers)

    pc_key = login.json()['key']
    csrf = login.cookies.get('csrftoken')

    # res = list()
    # res.append(pc_key)
    # res.append(csrf)

    res_dict = dict()
    res_dict['pc_key'] = pc_key
    res_dict['csrf'] = csrf

    return res_dict


# 酒吧返回带key的header
def pc_headers(user):
    # pc_header = {
    #     'Content-Type': 'application/json',
    #     'Authorization': 'Token ' + get_pc_key(user)[0],
    #     'X-CSRFToken': get_pc_key(user)[1]
    # }

    pc_header = {
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + get_pc_key(user).get('pc_key'),
        'X-CSRFToken': get_pc_key(user).get('csrf')
    }

    return pc_header
